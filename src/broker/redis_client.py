import json
import redis


class RedisBroker:
    def __init__(self, host="localhost", port=6379, password=None, decode_responses=True):
        self.client = redis.Redis(
            host=host,
            port=port,
            password=password,
            decode_responses=decode_responses
        )

    def publish(self, topic: str, event: dict):
        self.client.publish(topic, json.dumps(event))

    def create_pubsub(self):
        return self.client.pubsub()

    def subscribe(self, pubsub, topic: str):
        pubsub.subscribe(topic)