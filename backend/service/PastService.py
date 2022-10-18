import datetime

from backend.model.Record import Record
from backend.dao.PastDao import pastDao
from backend.dao.TodayDao import todayDao


class PastService:

    def addRecord(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        last = pastDao.getLastRecord()
        # 不要重复添加记录
        if last and date <= last.recordTime:
            return

        record = Record(todayDao.getEvents(), date)

        pastDao.insertRecordIntoCache(record)

    def removeRecordByIndex(self, index: int):
        pastDao.deleteRecordByIndexFromCache(index)

    def removeAllRecords(self):
        pastDao.deleteAll()

    def saveRecords(self):
        pastDao.persist()


pastService = PastService()

if __name__ == "__main__":
    pastService.removeAllRecords()
    pastService.addRecord()
    pastService.addRecord()
    pastService.saveChanges()
    pass