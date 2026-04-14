from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any


@dataclass
class Event:
    topic: str
    event_id: str
    timestamp: str
    payload: Dict[str, Any]

    @staticmethod
    def create(topic: str, event_id: str, payload: Dict[str, Any]):
        return Event(
            topic=topic,
            event_id=event_id,
            timestamp=datetime.utcnow().isoformat(),
            payload=payload
        )