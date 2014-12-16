#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
#from thBasic import thtitlebar

class ThSkinDialog(thframe.ThFrame):
	def __init__(self):
		super(ThSkinDialog,self).__init__()
		self.initSkinData()
		self.initSkinUI()
		self.initSkinConnect()

	def initSkinData(self):
		pass

	def initSkinUI(self):
		hideControl=('logoButton','skinButton','menuButton','minButton','maxButton')
		for hc in hideControl:
			self.getTitleBar().setControlVisible(hc,False)

	def initSkinConnect(self):
		pass

def main():
	app=QtGui.QApplication(sys.argv)
	w=ThSkinDialog()
	w.setGeometry(100,100,200,200)
	w.show()
	sys.exit(app.exec_())

if '__main__'==__name__:
	main()