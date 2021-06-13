import string
import sys

from PySide2 import QtGui,QtCore
from PySide2.QtWidgets import QPushButton, QWidget, QApplication,QTextEdit,QPlainTextEdit,QLabel,QDialog,QGridLayout,QVBoxLayout
from PySide2.QtCore import Qt, QMimeData, QPoint

import time
import screnData

class DraggableButton(QPushButton):
    follow=None
    def __init__(self, title, parent,f):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]
        self.follow=f

    def mousePressEvent(self, e):
        print("ppp", e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]

        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。
        self.parent().textEdit1.setText( (str)(self.mapToParent(cor).x())+" , "+ (str)(self.mapToParent(cor).y()))
        #self.parent().label1.move(self.mapToParent(cor).x(), self.mapToParent(cor).y() + screnData.screenData().unitH())
        self.follow.move(self.mapToParent(cor).x(), self.mapToParent(cor).y() + screnData.screenData().unitH())
        print('drag button event,', time.time(), e.pos(), e.x(), e.y(),self.mapToParent(cor))

    def mouseReleaseEvent(self,e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。
        self.parent().textEdit1.setText((str)(self.mapToParent(cor).x()) + " , " + (str)(self.mapToParent(cor).y()))
        #self.parent().label1.move(self.mapToParent(cor).x(),self.mapToParent(cor).y()+screnData.screenData().unitH())
        self.follow.move(self.mapToParent(cor).x(), self.mapToParent(cor).y() + screnData.screenData().unitH())
        print('mouseReleaseEvent,', time.time(), e.pos(), e.x(), e.y(), self.mapToParent(cor))
        #print("mouseReleaseEvent ")




class DragWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def addbutton(self,text):

        #label
        label1 = QLabel(text, self)
        label1.move(screnData.screenData().leftSkipP(),
                    screnData.screenData().topSkipP() + screnData.screenData().unitH())
        label1.resize(100, 30)

        #button
        button1 = DraggableButton("", self,label1)
        button1.move(screnData.screenData().leftSkipP(), screnData.screenData().topSkipP())
        print(screnData.screenData().leftSkipP())
        print(screnData.screenData().topSkipP())
        button1.resize(screnData.screenData().unitW(),screnData.screenData().unitH())
        button1.setIcon(QtGui.QIcon('myImage.jpg'))
        button1.setIconSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitW()))





    def initUI(self):
        self.textEdit1=QLabel(self)
        self.textEdit1.move(0,0)
        self.textEdit1.resize(100, 30)
   

        self.addbutton("test")






        #self.setWindowTitle("Click or Move")
        #desktop = QApplication.desktop()
        #self.setGeometry(0, 0, desktop.width(),desktop.height())


    def mouseMoveEvent(self, e):
        print('main', e.x(), e.y())


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = DragWidget()
#     ex.show()
#     app.exec_()
