#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class thViewSharedAlbum(QtGui.QFrame):
	def __init__(self,application,parent=None,windowFlag=QtCore.Qt.Widget):
		super(thViewSharedAlbum,self).__init__(parent,windowFlag)
		self.application=application
		self.initViewData()
		self.initViewUI()
		self.initViewConnect()
		
	def initViewData(self):
		pass

	def initViewUI(self):
		label=QtGui.QLabel('View Shared Disk')
		mainLayout=QtGui.QHBoxLayout()
		mainLayout.addWidget(label)
		self.setLayout(mainLayout)

	def initViewConnect(self):
		pass

def main():
	app=QtGui.QApplication(sys.argv)
	w=thViewSharedAlbum(app)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()