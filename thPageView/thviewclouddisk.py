#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from pvclouddisk import allfiles

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
		self.listWidget=QtGui.QListWidget()
		self.listWidget.setObjectName('CloudDiskListWidget')
		self.listWidget.setFixedWidth(200)
		self.statckedWidget=QtGui.QStackedWidget()
		mainLayout=QtGui.QHBoxLayout()
		mainLayout.addWidget(self.listWidget)
		mainLayout.addWidget(self.statckedWidget)
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(0)
		self.setLayout(mainLayout)

		strItems=('All Files','Files','Music','Vedio','Photograph','From Browser','My Shared','Safe Box','Recycle Bin','History')
		icons=('appbar.page.new.png','appbar.page.pdf.png','appbar.page.powerpoint.png',
			'appbar.page.search.png','appbar.page.text.png','appbar.page.word.png',
			'appbar.page.xml.png','appbar.paper.png','appbar.paw.png','appbar.paypal.png')
		for i in range(len(strItems)):
			item=QtGui.QListWidgetItem(strItems[i])
			icon=QtGui.QIcon('./thPageView/'+icons[i])
			item.setIcon(icon)
			item.setSizeHint(QtCore.QSize(36,36))
			self.listWidget.addItem(item)
		self.listWidget.setIconSize(QtCore.QSize(30,30))
		self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)

		self.pvAllFiles=allfiles.AllFiles(self.application)
		self.statckedWidget.addWidget(self.pvAllFiles)

	def initViewConnect(self):
		self.listWidget.currentRowChanged.connect(self.statckedWidget.setCurrentIndex)

def main():
	app=QtGui.QApplication(sys.argv)
	w=thViewCloudDisk(app)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()