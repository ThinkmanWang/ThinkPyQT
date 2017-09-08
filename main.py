#!/usr/bin/python
#coding=utf-8

import sys
from windows.CPAMainWindow import *

def main(argv):
    app = QApplication(argv)
    wndMain = CPAMainWindow()
    wndMain.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)