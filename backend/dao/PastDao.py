from typing import List

from backend.model.Record import Record
from backend.model.Event import Event
from backend.utils.JsonHelper import JsonHelper
from config import PAST_PATH


class PastDao:

    def __init__(self):
        self.cache = JsonHelper.loadJson(PAST_PATH)

    def getRecords(self) -> List[Record]:
        l = []
        for d in self.cache["records"]:
            l.append(Record.deSerialize(d))

        return l

    def getRecordByIndex(self, index: int) -> Record:
        l = self.cache["records"]

        if index < 0 or index >= len(l):
            return

        return Record.deSerialize(l[index])

    def getLastRecord(self) -> Record:
        l = self.cache["records"]

        if len(l) == 0:
            return

        return Record.deSerialize(l[len(l) - 1])

    def insertRecordIntoCache(self, record: Record):
        self.cache["records"].append(record.serialize())

    def deleteRecordByIndexFromCache(self, index: int):
        l = self.cache["records"]

        if index < 0 or index >= len(l):
            return

        del l[index]

    def deleteAll(self):
        self.cache = {"records": []}

    def persist(self):
        JsonHelper.dumpToJson(self.cache, PAST_PATH)


pastDao = PastDao()

if __name__ == "__main__":
    e = Event("", "", True)
    l = [e, e]
    pastDao.insertRecordIntoCache(Record(l, "2020"))
    pastDao.deleteRecordByIndexFromCache(0)
    pastDao.persist()
    pass