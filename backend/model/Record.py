from typing import List, Dict

from backend.model.Event import Event


class Record:

    def __init__(self, events: List[Event], recordTime: str):
        self.events = events
        self.recordTime = recordTime

    @classmethod
    def deSerialize(self, o):
        l = o["events"]

        events = []

        for d in l:
            events.append(Event.deSerialize(d))

        return Record(events, o["recordTime"])

    def serialize(self) -> Dict:
        l = []
        for event in self.events:
            l.append(event.serialize())

        return {
            "events": l,
            "recordTime": self.recordTime
        }
