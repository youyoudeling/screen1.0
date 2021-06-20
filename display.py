import string
import sys
import transfer
from win32api import ShellExecute
from PySide2 import QtGui,QtCore
from PySide2.QtWidgets import QPushButton, QWidget, QApplication,QTextEdit,QPlainTextEdit,QLabel,QDialog,QGridLayout,QVBoxLayout
from PySide2.QtCore import Qt, QMimeData, QPoint
#import test
import time
import screnData
import docx
transfer=transfer.transfer()
class DisplayWidget(QWidget):
    def __init__(self,parent=None):
        super(DisplayWidget,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.resize(500, 300)
        self.label1.move(0, 154)
        pixmap = QtGui.QPixmap("cy.jpg")
        self.label1.setPixmap(pixmap)



        self.label3 = QLabel(self)
        self.label3 = QLabel(self)
        self.label3.resize(300, 500)
        self.label3.move(566, 60)
        pixmap3 = QtGui.QPixmap("mb.jpg")
        self.label3.setPixmap(pixmap3)

        self.label2 = QLabel(self)
        self.label2.resize(500, 300)
        self.label2.move(866, 154)
        pixmap2 = QtGui.QPixmap("ng.jpg")
        self.label2.setPixmap(pixmap2)

        desktop = QApplication.desktop()

        WIDGET = desktop.width()
        HEIGHT = desktop.height()
        # self.resize(WIDGET,HEIGHT)
