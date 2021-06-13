# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget, QApplication,QPushButton,QGridLayout
import sys
'''
Pyqt 动态的添加控件
'''

class DynAddObject(QWidget):
    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)
        addButton = QPushButton(u"添加控件")
        self.layout = QGridLayout()
        self.layout.addWidget(addButton, 1, 0)
        self.setLayout(self.layout)
        self.connect(addButton, SIGNAL("clicked()"), self.add)

    def add(self):
        btncont= self.layout.count()
        widget = QPushButton(str(btncont), self)
        self.layout.addWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DynAddObject()
    form.show()
    app.exec_()