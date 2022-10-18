import json
import threading
from typing import Any


class JsonHelper:

    @classmethod
    def loadJson(cls, path: str) -> Any:
        with open(path) as f:
            o = json.load(f)
            return o

    @classmethod
    def dumpToJsonTask(cls, o, path: str):
        with open(path, "w") as f:
            json.dump(o, f)

    @classmethod
    def dumpToJson(cls, o, path: str):
        t = threading.Thread(target=cls.dumpToJsonTask, args=[o, path])

        t.start()

