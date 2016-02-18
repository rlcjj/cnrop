# encoding: UTF-8

import sys
import ctypes
from vtEngine import MainEngine
from uiMainWindow import *


# ----------------------------------------------------------------------
def main():
    """主程序入口"""
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('vnpy.ico'))
    app.setFont(BASIC_FONT)

    mainEngine = MainEngine()
    mainWindow = MainWindow(mainEngine, mainEngine.eventEngine)
    mainWindow.showMaximized()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
