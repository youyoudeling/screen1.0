
import sys

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow,QPlainTextEdit,QPushButton, QWidget, QApplication,QTabWidget
from PySide2.QtCore import Qt, QMimeData
import PySide2.QtGui
import drag

import string

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def onChange(self, index):
        print("切换" + str(index))
        if (index == 0):  # 如果点击的是第一个按钮
            print("Tab one change  tab 0")
        if (index == 1):  # 第二个
            print("Tab change tab 1")

        if (index == 2):  # 第三个
            #   self.textEdit_3.setText("I do  nothing ")
            pass


    def initUi(self):
        desktop = QApplication.desktop()
        WIDGET=desktop.width()
        HEIGHT=desktop.height()
        print("屏幕宽:" + str(WIDGET))
        print("屏幕高:" + str(HEIGHT))


        #self.setFixedSize(WIDGET,HEIGHT)
        self.resize(200,200)

        self.tabwidget = QTabWidget(self)
        self.tabwidget.setFixedSize(WIDGET,HEIGHT)




        #TAB1
        ex = drag.DragWidget()
        #接受拖拽进去？
        # ex.acceptDrops()
        print("ka")
        self.tabwidget.addTab(ex, '拖拽label')

        #TAB2
        self.tabwidget.addTab(QPushButton('tab2'), 'tab2')

        self.tabwidget.currentChanged.connect(self.onChange)




if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    desktop = QApplication.desktop()
    window.show()
    app.exec_()




