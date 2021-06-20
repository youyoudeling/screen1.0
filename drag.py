
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
class DraggableButton(QPushButton):
    global transfer
    follow=None
    text=None
    locationX=screnData.screenData().leftSkip+10
    locationY=screnData.screenData().topSkip+10
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
        print("self.locationX", self.locationX)
        print("self.locationY", self.locationY)
        print(screnData.screenData().UnitNum(self.locationX, self.locationY))
        file = docx.Document(self.text.split('///')[-1])
        print("地址"+self.text.split('///')[-1])
        text=file.paragraphs[0].text
        print(text)
        s = "xcx:gh_f4803b06a633path:pages/index/index?document=" + self.text.split('/')[-1]+"&text="+text
        transfer.output("", 2, screnData.screenData().UnitNum(self.locationX , self.locationY))

        time.sleep(0.01)
        print("self.X", self.mapToParent(cor).x())
        print("self.Y", self.mapToParent(cor).y())
        print(screnData.screenData().UnitNum(self.mapToParent(cor).x(), self.mapToParent(cor).y()))
        transfer.output(s,0,screnData.screenData().UnitNum(self.mapToParent(cor).x(),self.mapToParent(cor).y()))



        self.locationX=self.mapToParent(cor).x()
        self.locationY=self.mapToParent(cor).y()

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

        widget.setFixedSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitH()))
        #widget.setFixedSize(230, 230)
        widget.setIcon(QtGui.QIcon('myImage.png'))

        widget.setIconSize(QtCore.QSize(screnData.screenData().unitW(), screnData.screenData().unitW()))


        self.layout.addWidget(widget)
        self.layout.addWidget(label)
        return widget



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
