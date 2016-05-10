#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout

from customWidgets.countWidget import CountWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setToolTip('This is a <b>QWidget</b> widget')
        myown = CountWidget(self)

        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('this is it')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    wid = MyWidget()
    sys.exit(app.exec_())
