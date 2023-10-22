import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication
from src.utils.sys_parameters import IMAGE_PATH


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setWindowTitle('QMainWindow Explorer')
        self.setWindowIcon(QIcon(IMAGE_PATH + '/icon/ic_main_window.png'))
        self.setFixedSize(800, 400)

    def setupUi(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())