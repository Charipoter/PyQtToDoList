import datetime
from typing import List

from backend.dao.TodayDao import todayDao
from backend.model.Event import Event


class TodayService:

    def addEvent(self, text: str):
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        event = Event(text, date, False, 20)

        todayDao.insertEventIntoCache(event)

    def changeEventTextByIndex(self, index, text):
        event = todayDao.getEventByIndex(index)

        event.text = text

        todayDao.setEventByIndexFromCache(index, event)

    def changeEventFontSizeByIndex(self, index, fontSize):
        event = todayDao.getEventByIndex(index)

        event.fontSize = fontSize

        todayDao.setEventByIndexFromCache(index, event)

    def isEventCompleted(self, index) -> bool:
        event = todayDao.getEventByIndex(index)

        if not event:
            return False

        return event.isCompleted

    def completeEventByIndex(self, index):
        event = todayDao.getEventByIndex(index)

        event.isCompleted = True

        todayDao.setEventByIndexFromCache(index, event)

    def deCompleteEventByIndex(self, index):
        event = todayDao.getEventByIndex(index)

        event.isCompleted = False

        todayDao.setEventByIndexFromCache(index, event)

    def getEvents(self) -> List[Event]:
        return todayDao.getEvents()

    def removeEventByIndex(self, index: int):
        todayDao.deleteEventByIndexFromCache(index)

    def removeAllEvents(self):
        todayDao.deleteAll()

    def saveChanges(self):
        todayDao.persist()


todayService = TodayService()

if __name__ == "__main__":
    todayService.removeAllEvents()
    todayService.addEvent("asadsd")
    todayService.saveChanges()

    pass
