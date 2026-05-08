def test_malformed_event_missing_topic():
    malformed_event = {
        "event_id": "evt_002",
        "payload": {"image_id": "img_002"}
    }

    assert "topic" not in malformed_event


def test_malformed_event_missing_payload():
    malformed_event = {
        "topic": "image.submitted",
        "event_id": "evt_003"
    }

    assert "payload" not in malformed_event
    