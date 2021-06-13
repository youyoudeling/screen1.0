import string
import sys

from PySide2 import QtGui,QtCore
from PySide2.QtWidgets import QPushButton, QWidget, QApplication,QTextEdit,QPlainTextEdit,QLabel,QDialog,QGridLayout
from PySide2.QtCore import Qt, QMimeData, QPoint

import time
import screnData

class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]

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
        self.parent().label1.move(self.mapToParent(cor).x(), self.mapToParent(cor).y() + screnData.screenData().unitH())
        print('drag button event,', time.time(), e.pos(), e.x(), e.y(),self.mapToParent(cor))
    def mouseReleaseEvent(self,e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]
        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。
        self.parent().textEdit1.setText((str)(self.mapToParent(cor).x()) + " , " + (str)(self.mapToParent(cor).y()))
        self.parent().label1.move(self.mapToParent(cor).x(),self.mapToParent(cor).y()+screnData.screenData().unitH())
        print('mouseReleaseEvent,', time.time(), e.pos(), e.x(), e.y(), self.mapToParent(cor))
        #print("mouseReleaseEvent ")

 # class DynAddObject(QDialog):
 #     def __init__(self, parent=None):
 #         super(DynAddObject, self).__init__(parent)
 #         addButton = QPushButton(u"添加控件")
 #         self.layout = QGridLayout()
 #         self.layout.addWidget(addButton, 1, 0)
 #         self.setLayout(self.layout)
 #         self.connect(addButton, SIGNAL("clicked()"), self.add)
 #
 #     def add(self):
 #         btncont= self.layout.count()
 #         widget = QPushButton(str(btncont), self)
 #         self.layout.addWidget(widget)


class DragWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit1=QLabel(self)
        self.textEdit1.move(0,0)
        self.textEdit1.resize(100, 30)
   

        self.button1 = DraggableButton("", self)

        self.button1.move(screnData.screenData().leftSkipP(), screnData.screenData().topSkipP())
        print(screnData.screenData().leftSkipP())
        print(screnData.screenData().topSkipP())

        self.button1.resize(screnData.screenData().unitW(),screnData.screenData().unitH())
        self.button1.setIcon(QtGui.QIcon('myImage.jpg'))
        self.button1.setIconSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitW()))

        self.label1=QLabel(self)
        self.label1.move(screnData.screenData().leftSkipP(), screnData.screenData().topSkipP()+screnData.screenData().unitH())
        self.label1.resize(100,30)
        self.label1.setText("test")


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
