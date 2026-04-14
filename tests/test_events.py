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

from src.utils.event_generator import generate_image_submitted_event


def test_generate_image_submitted_event():
    event = generate_image_submitted_event(
        image_id="img_123",
        path="images/sample.jpg",
        source="camera_A"
    )

    assert event.topic == "image.submitted"
    assert event.event_id == "evt_img_123"
    assert event.payload["image_id"] == "img_123"
    assert event.payload["path"] == "images/sample.jpg"
    assert event.payload["source"] == "camera_A"
    assert isinstance(event.timestamp, str)