#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
import thclouddiskwindow

#class ThCloudDiskWindow(thframe.ThFrame):
#	def __init__(self):
#		super(ThCloudDiskWindow,self).__init__()
#		self.initData()
#		self.initUI()
#		self.initConnect()

def main():
	app=QtGui.QApplication(sys.argv)
	getQss,qss=thlibs.getQssFile('./skin/qss/yellow.qss')

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=thclouddiskwindow.ThCloudDiskWindow()
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()