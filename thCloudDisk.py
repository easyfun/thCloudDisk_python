#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs

class ThMainWindow(thframe.ThFrame):
	def __init__(self):
		super(ThMainWindow,self).__init__()
#		self.initData()
#		self.initUI()
#		self.initConnect()

def main():
	app=QtGui.QApplication(sys.argv)
	print(sys.argv)
	getQss,qss=thlibs.getQssFile('./skin/qss/black.qss')

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThMainWindow()
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()