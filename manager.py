import sys

from PyQt5.QtWidgets import QApplication

from frontend.Main import Main

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.processEvents()

    window = Main()
    window.show()
    sys.exit(app.exec_())