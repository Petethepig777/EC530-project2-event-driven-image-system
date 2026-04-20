from src.utils.event_generator import generate_image_submitted_event
from src.broker.redis_client import RedisBroker


def main():
    broker = RedisBroker()

    event = generate_image_submitted_event(
        image_id="img_001",
        path="images/sample.jpg",
        source="camera_A"
    )

    print("Publishing event...")
    broker.publish(event.topic, event.__dict__)
    print("Event published successfully!")


if __name__ == "__main__":
    main()