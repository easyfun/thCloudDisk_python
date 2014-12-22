#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ThToolBar(QtGui.QFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThToolBar,self).__init__(parent,windowFlags)
		self.application=application
		self.initToolBarData()
		self.initToolBarUI()
		self.initToolBarConnect()

	def initToolBarData(self):
		self.setObjectName('ThToolBar')
		pass

	def initToolBarUI(self):
		self.setFixedHeight(92)
		self.headPicButton=QtGui.QToolButton()
		self.headPicButton.setFixedSize(80,80)

		self.accountComboBox=QtGui.QComboBox()
		self.nameLineEdit=QtGui.QLineEdit()
		self.levelLabel=QtGui.QLabel('level 1')
		self.levelLabel.setFixedWidth(40)
		self.storageProgress=QtGui.QProgressBar()

		self.cloudDiskButton=QtGui.QToolButton()
		self.cloudDiskButton.setFixedSize(80,80)

		self.cloudAlbumButton=QtGui.QToolButton()
		self.cloudAlbumButton.setFixedSize(80,80)

		self.sharedAlbumButton=QtGui.QToolButton()
		self.sharedAlbumButton.setFixedSize(80,80)

		self.logoPicButton=QtGui.QToolButton()
		self.logoPicButton.setFixedHeight(80)

		sndLayout=QtGui.QVBoxLayout()
		sndLayout.addWidget(self.accountComboBox)

		trdLayout=QtGui.QHBoxLayout()
		trdLayout.addWidget(self.nameLineEdit)
		trdLayout.addWidget(self.levelLabel)
		sndLayout.addLayout(trdLayout)

		sndLayout.addWidget(self.storageProgress)

		mainLayout=QtGui.QHBoxLayout()
		mainLayout.addWidget(self.headPicButton)
		mainLayout.addLayout(sndLayout)
		mainLayout.addWidget(self.cloudDiskButton)
		mainLayout.addWidget(self.cloudAlbumButton)
		mainLayout.addWidget(self.sharedAlbumButton)
		mainLayout.addWidget(self.logoPicButton)
		self.setLayout(mainLayout)


	def initToolBarConnect(self):
		pass



def main():
	app=QtGui.QApplication(sys.argv)
	w=ThToolBar(app)
	w.setGeometry(100,100,300,94)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()