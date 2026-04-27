from src.broker.redis_client import RedisBroker


def run_inference_service():
    broker = RedisBroker()
    pubsub = broker.create_pubsub()

    input_topic = "image.submitted"
    output_topic = "inference.completed"

    broker.subscribe(pubsub, input_topic)

    print(f"Listening on: {input_topic}")

    for message in pubsub.listen():
        if message["type"] == "message":
            print("Received image event")

            inference_result = {
                "image_id": "img_001",
                "objects": [
                    {"label": "tower", "confidence": 0.95},
                    {"label": "city", "confidence": 0.88}
                ]
            }

            broker.publish(output_topic, inference_result)

            print(f"Published to: {output_topic}")


if __name__ == "__main__":
    run_inference_service()