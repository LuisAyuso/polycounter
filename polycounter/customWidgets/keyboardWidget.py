from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout

from customWidgets.countWidget import CountWidget
from tools.keyboard import get_char

class KeyboardWidget(QFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.setFrameShape(1)
        self.setGeometry(10, 10, 780, 580)

        self.hlay = QHBoxLayout(self)
        self.hlay.setSpacing(5);


        # three blocks, 9 keys each
        self.leftW = QFrame(self)
        self.leftW.setFrameShape(1)
        self.centerW = QFrame(self)
        self.centerW.setFrameShape(1)
        self.rightW = QFrame(self)
        self.rightW.setFrameShape(1)

        self.hlay.addWidget(self.leftW)
        self.hlay.addWidget(self.centerW)
        self.hlay.addWidget(self.rightW)

        self.leftLay = QGridLayout(self.leftW)
        self.centerLay = QGridLayout(self.centerW)
        self.rightLay = QGridLayout(self.rightW)

        self.leftLay.setContentsMargins(0,0,0,0)
        self.centerLay.setContentsMargins(0,0,0,0)
        self.rightLay.setContentsMargins(0,0,0,0)

        self.leftLay.setSpacing(1);
        self.centerLay.setSpacing(1);
        self.rightLay.setSpacing(1);

        for i in range(0, 3):
            for j in range(0, 3):
                self.leftLay.addWidget(CountWidget(self.leftW, "hola", get_char(i,j)), i, j)

        for i in range(0, 3):
            for j in range(0, 3):
                self.centerLay.addWidget(CountWidget(self.leftW, "hola", get_char(i,3 + j)), i, j)

        for i in range(0, 3):
            for j in range(0, 3):
                self.rightLay.addWidget(CountWidget(self.leftW, "hola", get_char(i,6 + j)), i, j)


