from src.models.event_schema import Event


def test_valid_event_creation():
    event = Event.create(
        topic="image.submitted",
        event_id="evt_001",
        payload={"image_id": "img_001", "path": "images/test.jpg"}
    )

    assert event.topic == "image.submitted"
    assert event.event_id == "evt_001"
    assert "image_id" in event.payload
    assert "path" in event.payload
    assert event.payload["image_id"] == "img_001"
    assert isinstance(event.timestamp, str)