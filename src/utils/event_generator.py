from src.models.event_schema import Event
from src.models.topics import TOPICS


def generate_image_submitted_event(image_id: str, path: str, source: str):
    return Event.create(
        topic=TOPICS["IMAGE_SUBMITTED"],
        event_id=f"evt_{image_id}",
        payload={
            "image_id": image_id,
            "path": path,
            "source": source
        }
    )
    