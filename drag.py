
import string
import sys

from win32api import ShellExecute
from PySide2 import QtGui,QtCore
from PySide2.QtWidgets import QPushButton, QWidget, QApplication,QTextEdit,QPlainTextEdit,QLabel,QDialog,QGridLayout,QVBoxLayout
from PySide2.QtCore import Qt, QMimeData, QPoint
#import test
import time
import screnData

class DraggableButton(QPushButton):
    follow=None
    text=None
    def __init__(self, title, parent,f,t):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]
        self.follow=f
        self.text=t

    def mousePressEvent(self, e):
        print("ppp", e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

        print(self.text)
        #test.openword(self.text)


    def mouseDoubleClickEvent(self, e) -> None:
        print("双击")
        ShellExecute(0, 'open', self.text, '', '', 1)



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
    BUTTONS = []
    LABELS=[]
    BUTTONNUM=-1

    def __init__(self,parent=None):
        super(DragWidget,self).__init__(parent)
        self.initUI()

    def add(self,text):
        self.BUTTONNUM = self.BUTTONNUM + 1
        label=QLabel(text.split('/')[-1],self)

        label.setFixedSize(400, 30)
        self.LABELS.append(label)
        widget = DraggableButton("", self, self.LABELS[self.BUTTONNUM],text)
        widget.setFixedSize(200,200)

        self.BUTTONS.append(widget)
        self.BUTTONS[self.BUTTONNUM].move(screnData.screenData().leftSkipP(), screnData.screenData().topSkipP())

        widget.setFixedSize(screnData.screenData().unitW(), screnData.screenData().unitH())
        widget.setIcon(QtGui.QIcon('myImage.png'))
        widget.setIconSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitW()))


        self.layout.addWidget(widget)
        self.layout.addWidget(label)
        self.BUTTONS[self.BUTTONNUM].move(0,0)
        self.LABELS[self.BUTTONNUM].move(0,0)
        return widget



    def addbutton(self,text):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("add")
        print(text)
        self.BUTTONNUM = self.BUTTONNUM + 1
        # label
        label1= QLabel(text, self)
        self.LABELS.append(label1)

        label1.setFixedSize(400, 30)

        # button
        button1 = DraggableButton("", self, self.LABELS[self.BUTTONNUM])
        self.BUTTONS.append(button1)
        #self.BUTTONS[self.BUTTONNUM].move(screnData.screenData().leftSkipP(), screnData.screenData().topSkipP())
        print(screnData.screenData().leftSkipP())
        print(screnData.screenData().topSkipP())
        button1.setFixedSize(screnData.screenData().unitW(), screnData.screenData().unitH())
        button1.setIcon(QtGui.QIcon('myImage.png'))
        button1.setIconSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitW()))

       # button1.move(0,0)
        self.layout.addWidget(button1)
        self.layout.addWidget(label1)

        # label1.move(screnData.screenData().leftSkipP(),
        #             screnData.screenData().topSkipP() + screnData.screenData().unitH())
        # button1.move(0,0)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


    # def dropEvent(self, e):
    #     print("down")
    #     self.addbutton(e.mimeData().text())
    #     self.textEdit1.setText(e.mimeData().text())
    #
    # def dragEnterEvent(self, e):
    #     if e.mimeData().hasUrls():
    #         e.acceptProposedAction()
    def dropEvent(self, e):
        print("down")



    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
            b1=self.add(e.mimeData().text())



    def initUI(self):
        self.setAcceptDrops(True)

        self.textEdit1 = QLabel()
        self.textEdit1.resize(100, 30)
        self.textEdit1.move(0, 0)
        desktop = QApplication.desktop()
        WIDGET = desktop.width()
        HEIGHT = desktop.height()
        # self.resize(WIDGET,HEIGHT)
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)











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
