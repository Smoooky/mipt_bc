from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from .schemas.EventCreate import EventCreate
from .models import Event, EventSpeakers, Speaker
from ...core.logging.logger import logger
from ...core.lib import handle_exception

class EventService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_event(self, event_in: EventCreate):
        try: 
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
                        raise NoResultFound(f"Speaker with id {speaker_id} not found")
                    
                    link = EventSpeakers(eventId=event.id, speakerId=speaker.id)
                    self.session.add(link)

            await self.session.commit()
            await self.session.refresh(event)
            
            logger.info("Event created successfully", extra_data={event})
            return event
        except Exception as e:
            handle_exception(e, context={{"cause": "Event create error", "event_title": event_in.title}})