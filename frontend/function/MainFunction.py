import re

from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QLabel, QVBoxLayout

from frontend.window.window import Ui_Form
from backend.controller.MainController import mainController


class MainFunction(QWidget, Ui_Form):

    def __init__(self):
        super(MainFunction, self).__init__()
        self.setupUi(self)

        self.selectedIndex: int = 0

        self.init()

    def init(self):
        index = 0
        for event in mainController.getEvents():
            self.addEventItem(event.text, event.updateTime, event.fontSize)

            if event.isCompleted:
                self.changeEventColorToBlack(index)
            index += 1

        self.optinsWindow.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        # 持久化数据
        mainController.saveChanges()

    def getTextLabelFromEventItem(self, index):
        return self.eventList.itemWidget(self.eventList.item(index)).layout().itemAt(0).widget()

def test():
    s = "QListWidget::item:selected{background-color: rgba(0,0,0,0.5);}" \
        "QListWidget::item{background-color: rgba(0,0,0,0.5);font: 1}"

    pattern = re.compile(r"[^{]*\{[^}]*\}")

    r = pattern.findall(s)

    pass


if __name__ == "__main__":
    test()



