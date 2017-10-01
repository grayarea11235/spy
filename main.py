#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1024, 768)

        self.statusBar().showMessage('Status')

        self.setWindowTitle('Spy')
        
        self.text = QTextEdit(self)
        self.text.setGeometry(0, 0, 1024, 768)

        self.text.show()

        # Set up the menu
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.show()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    main_wind = MainWindow()
 
    sys.exit(a.exec_())
