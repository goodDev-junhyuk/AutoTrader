from PyQt5.QtWidgets import *
from PyQt5 import uic

import sys

form_class = uic.loadUiType("TestProgramUI.ui")[0]
class MyWwindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWwindow()
    window.show()
    app.exec()