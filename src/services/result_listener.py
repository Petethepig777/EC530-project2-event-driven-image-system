import json

from src.broker.redis_client import RedisBroker


def run_result_listener():
    broker = RedisBroker()
    pubsub = broker.create_pubsub()

    topic = "embedding.created"
    broker.subscribe(pubsub, topic)

    print(f"Listening on: {topic}")

    for message in pubsub.listen():
        if message["type"] == "message":
            result = json.loads(message["data"])

            print("Final pipeline result received:")
            print(result)


if __name__ == "__main__":
    run_result_listener()