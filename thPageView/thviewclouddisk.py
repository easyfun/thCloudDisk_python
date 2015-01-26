#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from pvclouddisk import allfiles
from pvclouddisk import safebox
from pvclouddisk.cloudlistwidget import DiskListWidget
from thResource import qrc_resources


class thViewCloudDisk(QtGui.QFrame):
	def __init__(self,application,parent=None,windowFlag=QtCore.Qt.Widget):
		super(thViewCloudDisk,self).__init__(parent,windowFlag)
		self.application=application
		self.initViewData()
		self.initViewUI()
		self.initViewConnect()
		
	def initViewData(self):
		pass

	def initViewUI(self):
		'''
		self.listWidget=QtGui.QListWidget()
		self.listWidget.setObjectName('CloudDiskListWidget')
		self.listWidget.setFixedWidth(200)
		'''
		self.diskList=DiskListWidget()
		self.statckedWidget=QtGui.QStackedWidget()
		mainLayout=QtGui.QHBoxLayout()
		#mainLayout.addWidget(self.listWidget)
		mainLayout.addWidget(self.diskList)
		mainLayout.addWidget(self.statckedWidget)
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(0)
		self.setLayout(mainLayout)

		#self.pvAllFiles=allfiles.AllFiles(self.application)
		#self.statckedWidget.addWidget(self.pvAllFiles)
		#self.pvSafeBox=safebox.SafeBox(self.application)
		#self.statckedWidget.addWidget(self.pvSafeBox)

	def initViewConnect(self):
		#self.listWidget.currentRowChanged.connect(self.statckedWidget.setCurrentIndex)
		#self.listWidget.currentRowChanged.connect(self.setViewShow)
		pass

	def setViewShow(self,index):
		realIndex=index
		if 7==index:
			realIndex=1
		else:
			realIndex=0

		self.statckedWidget.setCurrentIndex(realIndex)

def main():
	app=QtGui.QApplication(sys.argv)
	w=thViewCloudDisk(app)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()