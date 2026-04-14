from src.utils.event_generator import generate_image_submitted_event
from src.broker.redis_client import RedisBroker


def main():
    event = generate_image_submitted_event(
        image_id="img_001",
        path="images/sample.jpg",
        source="camera_A"
    )

    print("Generated event:")
    print(event)

    broker = RedisBroker()

    print("\nBroker initialized successfully.")
    print("Ready to publish once professor provides online Redis credentials.")


if __name__ == "__main__":
    main()