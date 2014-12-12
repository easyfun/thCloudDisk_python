#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from thBasic import thframe

class ThMainWindow(thframe.ThFrame):
	def __init__(self):
		super(ThMainWindow,self).__init__()

def main():
	app=QtGui.QApplication(sys.argv)
	mainWindow=ThMainWindow()
	mainWindow.setGeometry(100,100,800,600)
	mainWindow.setWindowTitle('ThCloudDisk')
	mainWindow.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()