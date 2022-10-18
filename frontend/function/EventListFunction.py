import datetime

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QInputDialog, QListWidgetItem, QLabel, QVBoxLayout, QWidget

from backend.controller.MainController import mainController
from frontend.function.MainFunction import MainFunction


class EventListFunction(MainFunction):

    def addEvent(self):
        text, ok = QInputDialog.getMultiLineText(self, "输入", "请输入文本:", "摸鱼")

        if not ok:
            return

        mainController.addEvent(text)

        date = datetime.datetime.now().strftime("%Y-%m-%d")

        self.addEventItem(text, date)

    def createEventWidget(self, text: str, date: str, fontSize: int):
        widget = QWidget()

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 0, 5)

        textLabel = QLabel(text)
        textLabel.setStyleSheet("font:" + str(fontSize) + "px")
        textLabel.adjustSize()
        a = textLabel.height()

        layout.addWidget(textLabel)

        dateLabel = QLabel(date)
        dateLabel.setStyleSheet("font:15px")
        dateLabel.adjustSize()
        b = dateLabel.height()

        layout.addWidget(dateLabel)

        widget.setLayout(layout)

        margins = layout.getContentsMargins()

        height = textLabel.height() + dateLabel.height() + layout.spacing() + margins[1] + margins[3]
        widget.setFixedHeight(height)

        return widget

    def addEventItem(self, text: str, date: str, fontSize: int = 20):
        widget = self.createEventWidget(text, date, fontSize)

        item = QListWidgetItem()
        item.setSizeHint(QSize(self.eventList.width() - 10, widget.height()))

        self.eventList.addItem(item)

        self.eventList.setItemWidget(item, widget)

