from src.broker.redis_client import RedisBroker


def start_listener():
    broker = RedisBroker()
    pubsub = broker.create_pubsub()

    topic = "image.submitted"
    broker.subscribe(pubsub, topic)

    print(f"Listening on topic: {topic}...")

    for message in pubsub.listen():
        if message["type"] == "message":
            print("Received message:")
            print(message["data"])


if __name__ == "__main__":
    start_listener()
    