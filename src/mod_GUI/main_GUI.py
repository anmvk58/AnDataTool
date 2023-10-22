from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from window_one import Ui_MainWindow
from window_two import Ui_MainWindow2

class Window2(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.change_to_windows2)

    def change_to_windows2(self):
        widget.setCurrentIndex(1)
        print(widget.currentIndex())


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
WindowOne = AppWindow()
widget.resize(WindowOne.frameSize())
widget.addWidget(WindowOne)

WindowTwo = Window2()
widget.addWidget(WindowTwo)
widget.setCurrentWidget(WindowOne)
widget.show()

print(widget.currentIndex())
sys.exit(app.exec())
