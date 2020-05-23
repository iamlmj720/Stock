from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print("Ui_class입니다.")

        self.app = QApplication(sys.argv)  # 어플리케이션을 초기화 하는 용도

        self.kiwoom = Kiwoom()

        self.app.exec()


## class명의 첫문자는 대문자로 만들어야한다. (약속)