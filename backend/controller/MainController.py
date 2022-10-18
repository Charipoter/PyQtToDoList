from typing import List

from backend.model.Event import Event
from backend.service.PastService import pastService
from backend.service.TodayService import todayService


class MainController:

    def addEvent(self, text: str):
        todayService.addEvent(text)

    def changeEventTextByIndex(self, index: int, text: str):
        todayService.changeEventTextByIndex(index, text)

    def changeEventFontSizeByIndex(self, index: int, fontSize: int):
        todayService.changeEventFontSizeByIndex(index, fontSize)

    def removeEventByIndex(self, index: int):
        todayService.removeEventByIndex(index)

    def getEvents(self) -> List[Event]:
        return todayService.getEvents()

    def completeEventWithIndex(self, index: int) -> bool:
        if todayService.isEventCompleted(index):
            todayService.deCompleteEventByIndex(index)
            return False

        todayService.completeEventByIndex(index)
        return True

    def saveChanges(self):
        todayService.saveChanges()


mainController = MainController()