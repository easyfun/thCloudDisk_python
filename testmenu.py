#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class SkinMenu(QtGui.QMenu):
	def __init__(self):
		super(SkinMenu,self).__init__()
		self.initData()
		self.initUI()
		self.initConnect()

	def initData(self):
		pass

	def initUI(self):
		skinButton=QtGui.QToolButton(self)
		skinButton.setGeometry(20,20,20,20)
		self.resize(200,200)

	def initConnect(self):
		pass



class TestMenu(QtGui.QWidget):
	"""docstring for TestMenu"""
	def __init__(self):
		super(TestMenu, self).__init__()
		self.initData()
		self.initUI()
		self.initConnect()

	def initData(self):
		pass

	def initUI(self):
		self.skinButton=QtGui.QToolButton(self)
		self.skinButton.setGeometry(200,200,20,20)
		self.menu=SkinMenu()
		self.skinButton.setMenu(self.menu)

	def initConnect(self):
		pass
#		self.skinButton.clicked.connect(self.skinMenuSlot)

#	def skinMenuSlot(self):
#		sm=SkinMenu()
#		sm.show()

		

def main():
	app=QtGui.QApplication(sys.argv)
	w=TestMenu()
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if '__main__'==__name__:
	main()