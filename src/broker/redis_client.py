import json
import os

import redis
from dotenv import load_dotenv

load_dotenv()


class RedisBroker:
    def __init__(self):
        self.client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            password=os.getenv("REDIS_PASSWORD"),
            decode_responses=True
        )

    def publish(self, topic: str, event: dict):
        self.client.publish(topic, json.dumps(event))

    def create_pubsub(self):
        return self.client.pubsub()

    def subscribe(self, pubsub, topic: str):
        pubsub.subscribe(topic)