from PyQt5.QtCore import QModelIndex, QSize
from PyQt5.QtWidgets import QLabel, QInputDialog

from frontend.function.MainFunction import MainFunction
from backend.controller.MainController import mainController


class OptionsWindowFunction(MainFunction):

    def openOptionsWindow(self, index: QModelIndex):
        self.optinsWindow.show()
        self.selectedIndex = index.row()
        self.indexLabel.setText(str(self.selectedIndex))

        self.fontSizeLabel.setText(str(self.getTextLabelFromEventItem(index.row()).height()))

    def changeEventText(self):
        textLabel: QLabel = self.getTextLabelFromEventItem(self.selectedIndex)

        text, ok = QInputDialog.getMultiLineText(self, "输入", "请输入文本:", textLabel.text())

        if not ok:
            return

        mainController.changeEventTextByIndex(self.selectedIndex, text)

        textLabel.setText(text)

    def removeEvent(self):
        mainController.removeEventByIndex(self.selectedIndex)

        self.eventList.takeItem(self.selectedIndex)

        self.optinsWindow.close()

    def completeEvent(self):
        if mainController.completeEventWithIndex(self.selectedIndex):
            self.changeEventColorToBlack(self.selectedIndex)
        else:
            self.changeEventColorToWhite(self.selectedIndex)

    def changeEventColorToBlack(self, index):
        self.changeEventColor(index, 0)

    def changeEventColorToWhite(self, index):
        self.changeEventColor(index, 1)

    def changeEventColor(self, index, plan):
        plans = ["background-color:rgba(0,0,0,1);color: rgba(255,255,255,1);",
                 "background-color:rgba(255,255,255,1);color: rgba(0,0,0,1);"]

        color = plans[plan]

        widget = self.eventList.itemWidget(self.eventList.item(index))

        widget.setStyleSheet(color)

    def increaseEventFontSize(self):
        curSize = eval(self.fontSizeLabel.text())

        curSize += 1
        self.fontSizeLabel.setText(str(curSize))
        self.changeEventFontSize(curSize, 1)

    def decreaseEventFontSize(self):
        curSize = eval(self.fontSizeLabel.text())

        curSize -= 1

        if curSize <= 0:
            return

        self.fontSizeLabel.setText(str(curSize))
        self.changeEventFontSize(curSize, -1)

    def changeEventFontSize(self, fontSize, offset):
        mainController.changeEventFontSizeByIndex(self.selectedIndex, fontSize)

        item = self.eventList.item(self.selectedIndex)
        widget = self.eventList.itemWidget(item)
        textLabel = self.getTextLabelFromEventItem(self.selectedIndex)

        textLabel.setStyleSheet("font:" + str(fontSize) + "px")
        textLabel.adjustSize()

        widget.setFixedHeight(widget.height() + offset)

        item.setSizeHint(QSize(self.eventList.width() - 10, widget.height()))