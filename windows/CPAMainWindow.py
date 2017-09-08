#!/usr/bin/python
#coding=utf-8

import sys
from PyQt5.QtWidgets import qApp, QAction, QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class CPAMainWindow(QMainWindow):
    def __init__(self):
        super(CPAMainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()

        exitAction = QAction(QIcon('heart256.ico'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('menubar')





