#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs

class ThSkinDialog(thframe.ThFrame):
	def __init__(self):
		super(ThSkinDialog,self).__init__()
#		self.initData()
#		self.initUI()
#		self.initConnect()

#	def initData(self):
#		pass

#	def initUI(self):
#		pass

#	def initConnect(self):
#		pass

def main():
	app=QtGui.QApplication(sys.argv)
	w=ThSkinDialog()
	w.setGeometry(100,100,200,200)
	w.show()
	sys.exit(app.exec_())

if '__main__'==__name__:
	main()