from unittest.mock import Mock
from src.broker.redis_client import RedisBroker


def test_publish_calls_redis_publish():
    broker = RedisBroker()
    broker.client = Mock()

    event = {
        "topic": "image.submitted",
        "event_id": "evt_001",
        "timestamp": "2026-04-14T12:00:00",
        "payload": {
            "image_id": "img_001",
            "path": "images/test.jpg"
        }
    }

    broker.publish("image.submitted", event)

    broker.client.publish.assert_called_once()