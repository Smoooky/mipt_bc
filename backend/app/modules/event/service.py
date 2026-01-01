from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy import delete
from sqlalchemy.orm import selectinload
from .schemas import EventCreate, SpeakerCreate, EventSearchParams, SpeakerSearchParams, PaginationSettings, EventUpdate, SpeakerUpdate
from .models import Event, EventSpeaker, Speaker
from app.core.logging.logger import logger
from app.core.lib import handle_exception, ApiErrors
from typing import List

class EventService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_event(self, event_in: EventCreate) -> Event:
        try:
            async with self.session.begin():
                event_data = event_in.model_dump(exclude={"speaker_ids"})
                logger.info("Event data before creation", extra_data=event_data)
                event = Event(**event_data)

                self.session.add(event)
                await self.session.flush() 

                if event_in.speaker_ids:
                    for speaker_id in event_in.speaker_ids:
                        stmt = select(Speaker).where(Speaker.id == speaker_id)
                        result = await self.session.execute(stmt)
                        speaker = result.scalars().first()

                        if not speaker:
                            raise ApiErrors.NotFound(
                                f"Speaker with id {speaker_id} not found"
                            )

                        link = EventSpeaker(
                            event_id=event.id,
                            speaker_id=speaker.id
                        )
                        self.session.add(link)

            stmt = (
                select(Event)
                .options(selectinload(Event.speakers))
                .where(Event.id == event.id)
                )
            result = await self.session.execute(stmt)
            event_with_speakers = result.scalar_one()

            logger.info(
                "Event created successfully",
                extra_data={"event_id": event.id}
            )
            return event_with_speakers

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "EVENT_CREATE_ERROR",
                    "event_title": event_in.title,
                },
            )
    
    async def update_event(self, event_id: int, event_in: EventUpdate) -> Event:
        try:
            async with self.session.begin():
                stmt = select(Event).where(Event.id == event_id)
                result = await self.session.execute(stmt)
                event = result.scalars().first()

                if not event:
                    raise ApiErrors.NotFound(f'Event with id {event_id} not found')
                
                update_data = event_in.model_dump(
                    exclude_unset=True,
                    exclude={'speakers'}
                )

                for field, value in update_data.items():
                    setattr(event, field, value)
                
                if event_in.speakers:
                    speakers = event_in.speakers

                    if speakers.speakers_to_delete:
                        await self.session.execute(
                            delete(EventSpeaker).where(
                                EventSpeaker.event_id == event_id,
                                EventSpeaker.speaker_id.in_(
                                    speakers.speakers_to_delete
                                )
                            )
                        )

                    if speakers.speakers_to_connect:
                        for speaker_id in speakers.speakers_to_connect:
                            stmt = select(Speaker).where(Speaker.id == speaker_id)
                            result = await self.session.execute(stmt)
                            speaker = result.scalar_one_or_none()

                            if not speaker:
                                raise ApiErrors.NotFound(f'Speaker with id ${speaker_id} not found')
                            
                            stmt = select(EventSpeaker).where(
                                EventSpeaker.event_id == event_id,
                                EventSpeaker.speaker_id == speaker_id
                            )
                            result = await self.session.execute(stmt)
                            link_exists = result.scalar_one_or_none()

                            if link_exists:
                                continue
                        
                            self.session.add(
                                EventSpeaker(
                                    event_id=event.id,
                                    speaker_id=speaker.id
                                )
                            )

            stmt = (
                select(Event)
                .options(selectinload(Event.speakers))
                .where(Event.id == event.id)
            )            
            result = await self.session.execute(stmt)
            return result.scalar_one()

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "EVENT_UPDATE_ERROR",
                    "event_id": event_id,
                },
            )

    async def get_event(self, event_id: int) -> Event:
        try:
            stmt = select(Event).options(selectinload(Event.speakers)).where(Event.id == event_id)
            result = await self.session.execute(stmt)
            event = result.scalars().first()

            if not event:
                raise ApiErrors.NotFound(f"Event with id ${event_id} not found")
        
            return event

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "EVENT_CREATE_ERROR",
                    "event_title": event_id,
                },
            )

    async def search_events(self, params: EventSearchParams, settings: PaginationSettings) -> List[Event]:
        try:
            stmt = select(Event).options(selectinload(Event.speakers))
            filters = []

            if params.title:
                filters.append(Event.title.ilike(f"%{params.title}%"))
            if params.description:
                filters.append(Event.description.ilike(f"%{params.description}%"))
            if params.status:
                filters.append(Event.status == params.status)
            if params.start_date_from:
                filters.append(Event.start_date >= params.start_date_from)
            if params.start_date_to:
                filters.append(Event.start_date <= params.start_date_to)
            if params.end_date_from:
                filters.append(Event.start_date >= params.end_date_from)
            if params.end_date_to:
                filters.append(Event.start_date <= params.end_date_to)
            if params.irl_meeting_space:
                filters.append(Event.irl_meeting_space.ilike(f"%{params.irl_meeting_space}%"))
            if params.online_meeting_space:
                filters.append(Event.online_meeting_space.ilike(f"%{params.online_meeting_space}%"))
            
            if filters:
                stmt = stmt.where(and_(*filters))
            
            stmt = stmt.limit(settings.limit).offset(settings.offset)

            result = await self.session.execute(stmt)
            events = result.scalars().all()
            return events

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "EVENT_SEARCH_ERROR",
                }
            )

    async def delete_event(self, event_id: int) -> None:
        try:
            ex_stmt = select(Event).where(Event.id == event_id)
            result = await self.session.execute(ex_stmt)
            existence = result.scalars().first()

            if not existence:
                raise ApiErrors.NotFound(f'Event with id {event_id} not found')

            stmt = delete(Event).where(Event.id == event_id)
            await self.session.execute(stmt)
            await self.session.commit()

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "EVENT_DELETE_ERROR",
                    "event_id": event_id
                }
            )
    
    async def create_speaker(self, speaker_in: SpeakerCreate) -> Speaker:
        try:
            async with self.session.begin():
                speaker = Speaker(**speaker_in.model_dump())
                self.session.add(speaker)

            await self.session.refresh(speaker)

            logger.info(
                "Speaker created successfully",
                extra_data={"speaker_id": speaker.id}
            )
            return speaker

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "SPEAKER_CREATE_ERROR",
                    "speaker_name": speaker_in.full_name,
                },
            )

    async def update_speaker(self, speaker_id: int, speaker_in: SpeakerUpdate) -> Speaker:
        try:
            async with self.session.begin():
                stmt = select(Speaker).where(Speaker.id == speaker_id)
                result = await self.session.execute(stmt)
                speaker = result.scalars().first()

                if not speaker:
                    raise ApiErrors.NotFound(f'Speaker with id {speaker_id} not found')
            
                update_data = speaker_in.model_dump(
                    exclude_unset=True
                )

                for field, value in update_data.items():
                    setattr(speaker, field, value)

            return speaker
        
        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "SPEAKER_UPDATE_ERROR",
                    "speaker_id": speaker_id,
                },
            )

    async def get_speaker(self, speaker_id: int) -> Speaker:
        try:
            stmt = select(Speaker).where(Speaker.id == speaker_id)
            result = await self.session.execute(stmt)
            speaker = result.scalars().first()

            if not speaker:
                raise ApiErrors.NotFound(f"Speaker with id {speaker_id} not found")
            
            return speaker
        
        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "SPEAKER_GET_ERROR",
                    "speaker_id": speaker_id
                }
            )
    
    async def search_speakers(self, params: SpeakerSearchParams, settings: PaginationSettings) -> List[SpeakerSearchParams]:
        try:
            stmt = select(Speaker)
            filters = []

            if params.full_name:
                filters.append(Speaker.full_name.ilike(f"%{params.full_name}%"))
            if params.bio:
                filters.append(Speaker.bio.ilike(f"%{params.bio}%"))
            if params.position:
                filters.append(Speaker.position.ilike(f"%{params.position}%"))
            if params.company:
                filters.append(Speaker.company.ilike(f"%{params.company}%"))

            if filters:
                stmt = stmt.where(and_(*filters))
            
            stmt = stmt.limit(settings.limit).offset(settings.offset)
            
            result = await self.session.execute(stmt)
            speakers = result.scalars().all()
            return speakers
        
        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "SPEAKER_SEARCH_ERROR",
                }
            )


    async def delete_speaker(self, speaker_id: int) -> None:
        try:
            ex_stmt = select(Speaker).where(Speaker.id == speaker_id)
            result = await self.session.execute(ex_stmt)
            existence = result.scalars().first()

            if not existence:
                raise ApiErrors.NotFound(f'Speaker with id {speaker_id} not found')

            stmt = delete(Speaker).where(Speaker.id == speaker_id)
            await self.session.execute(stmt)
            await self.session.commit()
        
        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "SPEAKER_DELETE_ERROR",
                    "speaker_id": speaker_id
                }
            )