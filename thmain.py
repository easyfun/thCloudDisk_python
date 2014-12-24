#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thFrame import thframe
from thLib import thlib
from thclouddiskwindow import ThCloudDiskWindow

def main():
	app=QtGui.QApplication(sys.argv)
	getQss,qss=thlib.getQssFile('./skin/qss/teal.qss')

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThCloudDiskWindow(app)
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()