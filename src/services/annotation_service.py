import json

from src.broker.redis_client import RedisBroker


def run_annotation_service():
    broker = RedisBroker()
    pubsub = broker.create_pubsub()

    input_topic = "inference.completed"
    output_topic = "annotation.stored"

    broker.subscribe(pubsub, input_topic)

    print(f"Listening on: {input_topic}")

    for message in pubsub.listen():
        if message["type"] == "message":
            inference_result = json.loads(message["data"])

            annotation = {
                "image_id": inference_result["image_id"],
                "objects": inference_result["objects"],
                "status": "stored"
            }

            broker.publish(output_topic, annotation)

            print("Stored annotation:")
            print(annotation)
            print(f"Published to: {output_topic}")


if __name__ == "__main__":
    run_annotation_service()