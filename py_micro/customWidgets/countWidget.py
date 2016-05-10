from PyQt5.QtWidgets import QFrame, QWidget, QLCDNumber, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class CountWidget(QFrame):

    def __init__(self, parent, name = "-----", key = "?"):
        super().__init__(parent)

        #TODO, find the box enum value
        self.setFrameShape(1)

        self.up = QWidget(self)
        self.vlayout = QVBoxLayout(self)
        self.hlayout = QHBoxLayout(self.up)

        self.name_lab = QLabel(self.up)
        self.key_lab = QLabel(self.up)
        self.name_lab.setText("<i>" + name + "</i>")
        self.key_lab.setText("<b>" + key + "</b>")

        self.hlayout.addWidget(self.name_lab)
        self.hlayout.addWidget(self.key_lab)

        self.counter = QLCDNumber(self)

        self.vlayout.addWidget(self.up)
        self.vlayout.addWidget(self.counter)

        self.setToolTip('This is my own widget')

    def set_name(self, name):
        self.name_lab.setText("<i>" + name + "</i>")

    def set_key(self, key):
        self.key_lab.setText("<b>" + key + "</b>")
