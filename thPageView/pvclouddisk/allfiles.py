#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class AllFiles(QtGui.QFrame):
	def __init__(self,application,parent=None,windowsFlag=QtCore.Qt.Widget):
		super(AllFiles,self).__init__(parent,windowsFlag)
		self.application=application
		self.setObjectName('ViewCloudDiskAllFiles')
		self.initAllFilesData()
		self.initAllFilesUI()
		self.initAllFilesConnect()

	def initAllFilesData(self):
		pass

	def initAllFilesUI(self):
		height=26
		self.homeButton=QtGui.QToolButton()
		self.homeButton.setObjectName('ViewCloudDiskToolButton')
		self.homeButton.setFixedHeight(height)
		self.setToolButtonIcon(self.homeButton,'./thPageView/pvclouddisk/appbar.home.png')

		self.backButton=QtGui.QToolButton()
		self.backButton.setObjectName('ViewCloudDiskToolButton')
		self.backButton.setFixedHeight(height)
		self.setToolButtonIcon(self.backButton,'./thPageView/pvclouddisk/appbar.arrow.left.png')

		self.forwordButton=QtGui.QToolButton()
		self.forwordButton.setObjectName('ViewCloudDiskToolButton')
		self.forwordButton.setFixedHeight(height)
		self.setToolButtonIcon(self.forwordButton,'./thPageView/pvclouddisk/appbar.arrow.right.png')

		self.pathComboBox=QtGui.QComboBox()
		self.pathComboBox.setFixedHeight(height)
		self.refreshButton=QtGui.QToolButton()
		self.refreshButton.setObjectName('ViewCloudDiskRefreshButton')
		self.refreshButton.setFixedHeight(height)
		self.setToolButtonIcon(self.refreshButton,'./thPageView/pvclouddisk/appbar.refresh.png')

		self.searchEdit=QtGui.QLineEdit()
		self.searchEdit.setFixedWidth(200)
		self.searchEdit.setFixedHeight(height)

		topLayout=QtGui.QHBoxLayout()
		topLayout.addWidget(self.homeButton)
		topLayout.addWidget(self.backButton)
		topLayout.addWidget(self.forwordButton)

		topChildLayout=QtGui.QHBoxLayout()
		topChildLayout.addWidget(self.pathComboBox)
		topChildLayout.addWidget(self.refreshButton)
	#	topLayout.addWidget(self.pathComboBox)
	#	topLayout.setStretch(3,1)
	#	topLayout.addWidget(self.refreshButton)
		topChildLayout.setContentsMargins(0,0,0,0)
		topChildLayout.setSpacing(1)
		topLayout.addLayout(topChildLayout)
		topLayout.setStretch(3,1)

		topLayout.addWidget(self.searchEdit)
		topLayout.setContentsMargins(5,2,2,0)

		height2=24
		self.uploadButton=QtGui.QToolButton()
		self.uploadButton.setFixedHeight(height2)
		#self.uploadButton.setObjectName('ViewCloudDiskUploadButton')
		self.uploadButton.setObjectName('ViewCloudDiskToolButton')
		self.uploadButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.uploadButton.setText('UpFile')
		self.uploadButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.upload.png'))

		self.newButton=QtGui.QToolButton()
		self.newButton.setFixedHeight(height2)
		self.newButton.setObjectName('ViewCloudDiskToolButton')
		self.newButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.newButton.setText('New')
		self.newButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.add.png'))

		self.downloadButton=QtGui.QToolButton()
		self.downloadButton.setFixedHeight(height2)
		self.downloadButton.setObjectName('ViewCloudDiskToolButton')
		self.downloadButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.downloadButton.setText('DownFile')
		self.downloadButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.download.png'))

		self.deleteButton=QtGui.QToolButton()
		self.deleteButton.setFixedHeight(height2)
		self.deleteButton.setObjectName('ViewCloudDiskToolButton')
		self.deleteButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.deleteButton.setText('Delete')
		self.deleteButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.delete.png'))
		
		self.shareButton=QtGui.QToolButton()
		self.shareButton.setFixedHeight(height2)
		self.shareButton.setObjectName('ViewCloudDiskToolButton')
		self.shareButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.shareButton.setText('Share')
		self.shareButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.share.png'))
		
		self.sortButton=QtGui.QToolButton()
		self.sortButton.setFixedHeight(height2)
		self.sortButton.setObjectName('ViewCloudDiskToolButton')
		self.sortButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.sortButton.setText('Sort')
		self.sortButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.sort.png'))
		
		self.viewButton=QtGui.QToolButton()
		self.viewButton.setFixedHeight(height2)
		self.viewButton.setObjectName('ViewCloudDiskToolButton')
		self.viewButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.viewButton.setText('View')
		self.viewButton.setIcon(QtGui.QIcon('./thPageView/pvclouddisk/appbar.list.png'))

		toolGroup=QtGui.QGroupBox()
		toolGroup.setObjectName('ViewCloudDiskToolGroup')
		toolLayout=QtGui.QHBoxLayout()
		toolLayout.setObjectName('ToolLayout')
		toolLayout.addWidget(self.uploadButton)
		toolLayout.addWidget(self.newButton)
		toolLayout.addWidget(self.downloadButton)
		toolLayout.addWidget(self.deleteButton)
		toolLayout.addWidget(self.shareButton)
		toolLayout.addStretch()
		toolLayout.addWidget(self.sortButton)
		toolLayout.addWidget(self.viewButton)
		toolLayout.setContentsMargins(5,2,2,2)
		toolGroup.setLayout(toolLayout)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addLayout(topLayout)
		#mainLayout.addLayout(toolLayout)
		mainLayout.addWidget(toolGroup)
		mainLayout.addStretch()
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(4)
		self.setLayout(mainLayout)


	def initAllFilesConnect(self):
		pass

	def setToolButtonIcon(self,toolButton,strIcon):
		toolButton.setIcon(QtGui.QIcon(strIcon))
		toolButton.setIconSize(QtCore.QSize(26,26))