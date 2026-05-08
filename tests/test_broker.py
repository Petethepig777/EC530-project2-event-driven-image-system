from unittest.mock import Mock, patch

from src.broker.redis_client import RedisBroker


@patch("src.broker.redis_client.redis.Redis")
def test_publish_calls_redis_publish(mock_redis):
    mock_client = Mock()
    mock_redis.return_value = mock_client

    broker = RedisBroker()

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

    mock_client.publish.assert_called_once()
