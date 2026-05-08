import json

from src.broker.redis_client import RedisBroker
from src.db.vector_index import VectorIndex


vector_index = VectorIndex(dimension=4)


def run_embedding_service():
    broker = RedisBroker()
    pubsub = broker.create_pubsub()

    input_topic = "annotation.stored"
    output_topic = "embedding.created"

    broker.subscribe(pubsub, input_topic)

    print(f"Listening on: {input_topic}")

    for message in pubsub.listen():
        if message["type"] == "message":
            annotation = json.loads(message["data"])

            embedding = {
                "image_id": annotation["image_id"],
                "embedding": [0.12, 0.45, -0.88, 0.31],
                "status": "created"
            }

            vector_index.add_embedding(
                embedding["image_id"],
                embedding["embedding"]
            )

            broker.publish(output_topic, embedding)

            print("Created embedding and added to FAISS:")
            print(embedding)
            print(f"Published to: {output_topic}")


if __name__ == "__main__":
    run_embedding_service()
    