from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .schemas import EventCreate, SpeakerCreate
from .models import Event, EventSpeakers, Speaker
from app.core.logging.logger import logger
from app.core.lib import handle_exception
from app.core.lib.ApiError import ApiErrors

class EventService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_event(self, event_in: EventCreate):
        try:
            async with self.session.begin():
                event_data = event_in.model_dump(exclude={"speakerIds"})
                event = Event(**event_data)

                self.session.add(event)
                await self.session.flush() 

                if event_in.speakerIds:
                    for speaker_id in event_in.speakerIds:
                        stmt = select(Speaker).where(Speaker.id == speaker_id)
                        result = await self.session.execute(stmt)
                        speaker = result.scalars().first()

                        if not speaker:
                            raise ApiErrors.NotFound(
                                f"Speaker with id {speaker_id} not found"
                            )

                        link = EventSpeakers(
                            eventId=event.id,
                            speakerId=speaker.id
                        )
                        self.session.add(link)

            await self.session.refresh(event)

            logger.info(
                "Event created successfully",
                extra_data={"event_id": event.id}
            )
            return event

        except Exception as e:
            handle_exception(
                e,
                context={
                    "cause": "Event create error",
                    "event_title": event_in.title,
                },
            )

    async def get_event(self, event_id: int) -> Event:
        try:
            stmt = select(Event).where(Event.id == event_id)
            result = await self.session.execute(stmt)
            event = result.scalars().first()

            if not event:
                raise ApiErrors.NotFound(f"Event with id {event_id} not found")
            
            return event
        except Exception as e:
            handle_exception(
                e,
                context={
                    "cause": "Get event error",
                    "event_id": event_id
                }
            )
    
    async def create_speaker(self, speaker_in: SpeakerCreate):
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
                    "cause": "Speaker create error",
                    "speaker_name": speaker_in.title,
                },
            )

    async def get_speacker(self, speaker_id: int) -> Speaker:
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
                    "cause": "Get speacker error",
                    "speaker_id": speaker_id
                }
            )