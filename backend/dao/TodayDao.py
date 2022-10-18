import json
from typing import List

from backend.model.Event import Event
from config import TODAY_PATH
from backend.utils.JsonHelper import JsonHelper


class TodayDao:

    def __init__(self):
        self.cache = JsonHelper.loadJson(TODAY_PATH)

    def getEvents(self) -> List[Event]:
        l = []
        for d in self.cache["events"]:
            l.append(Event.deSerialize(d))

        return l

    def getEventByIndex(self, index: int) -> Event:
        l = self.cache["events"]

        if index < 0 or index >= len(l):
            return None

        return Event.deSerialize(l[index])

    def insertEventIntoCache(self, event: Event):
        d = event.serialize()

        self.cache["events"].append(d)

    def setEventByIndexFromCache(self, index: int, event: Event):
        l = self.cache["events"]

        if index < 0 or index >= len(l):
            return

        l[index] = event.serialize()

    def deleteEventByIndexFromCache(self, index: int):
        l = self.cache["events"]

        if index < 0 or index >= len(l):
            return

        del l[index]

    def deleteAll(self):
        self.cache = {"events": []}

    def persist(self):
        JsonHelper.dumpToJson(self.cache, TODAY_PATH)


todayDao = TodayDao()

if __name__ == "__main__":
    e = Event("", "", True)
    # todayDao.insertEventIntoCache(e)
    todayDao.deleteEventByIndexFromCache(1)
    todayDao.persist()
    pass