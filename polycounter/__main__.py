#!/usr/bin/python3

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout

from customWidgets.keyboardWidget import KeyboardWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(800,600)

        self.setToolTip('This is a <b>QWidget</b> widget')
        myown = KeyboardWidget(self)

        self.setWindowTitle('PolyCounter NG')
        app.setWindowIcon(QIcon('assets/chip_icon_normal.png'))
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    wid = MyWidget()
    sys.exit(app.exec_())
