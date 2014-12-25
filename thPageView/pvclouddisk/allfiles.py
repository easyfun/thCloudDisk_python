#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class AllFiles(QtGui.QFrame):
	def __init__(self,application,parent=None,windowsFlag=QtCore.Qt.Widget):
		super(AllFiles,self).__init__(parent,windowsFlag)
		self.application=application
		self.initAllFilesData()
		self.initAllFilesUI()
		self.initAllFilesConnect()

	def initAllFilesData(self):
		pass

	def initAllFilesUI(self):
		self.homeButton=QtGui.QToolButton()
		self.backButton=QtGui.QToolButton()
		self.forwordButton=QtGui.QToolButton()
		self.pathComboBox=QtGui.QComboBox()
		self.refreshButton=QtGui.QToolButton()
		self.searchEdit=QtGui.QLineEdit()
		topLayout=QtGui.QHBoxLayout()
		topLayout.addWidget(self.homeButton)
		topLayout.addWidget(self.backButton)
		topLayout.addWidget(self.forwordButton)
		topLayout.addWidget(self.pathComboBox)
		topLayout.setStretch(3,1)
		topLayout.addWidget(self.refreshButton)
		topLayout.addWidget(self.searchEdit)
		topLayout.setContentsMargins(5,2,2,0)

		self.uploadButton=QtGui.QToolButton()
		self.uploadButton.setText('Upload File')
		self.newButton=QtGui.QToolButton()
		self.newButton.setText('New')
		self.downloadButton=QtGui.QToolButton()
		self.downloadButton.setText('Download')
		self.deleteButton=QtGui.QToolButton()
		self.deleteButton.setText('Delete')
		self.shareButton=QtGui.QToolButton()
		self.shareButton.setText('Share')
		self.sortButton=QtGui.QToolButton()
		self.sortButton.setText('Sort')
		self.viewButton=QtGui.QToolButton()
		self.viewButton.setText('View')
		toolLayout=QtGui.QHBoxLayout()
		toolLayout.addWidget(self.uploadButton)
		toolLayout.addWidget(self.newButton)
		toolLayout.addWidget(self.downloadButton)
		toolLayout.addWidget(self.deleteButton)
		toolLayout.addWidget(self.shareButton)
		toolLayout.addStretch()
		toolLayout.addWidget(self.sortButton)
		toolLayout.addWidget(self.viewButton)
		toolLayout.setContentsMargins(5,2,2,0)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addLayout(topLayout)
		mainLayout.addLayout(toolLayout)
		mainLayout.addStretch()
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(4)
		self.setLayout(mainLayout)


	def initAllFilesConnect(self):
		pass