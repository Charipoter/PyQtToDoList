from typing import Dict


class Event:

    def __init__(self, text: str, updateTime: str, isCompleted: bool, fontSize: int):
        self.text = text
        self.updateTime = updateTime
        self.isCompleted = isCompleted
        self.fontSize = fontSize

    @classmethod
    def deSerialize(self, d: Dict):
        return Event(d["text"], d["updateTime"], d["isCompleted"], d["fontSize"])

    def serialize(self) -> Dict:
        return {
            "text": self.text,
            "updateTime": self.updateTime,
            "isCompleted": self.isCompleted,
            "fontSize": self.fontSize
                }
