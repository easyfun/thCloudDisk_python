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
		self.buttonDict={}
		pass

	def initToolBarUI(self):
		self.setFixedHeight(92)

#		buttonObjName=('HeadPicture','CloudDisk','CloudAlbum','SharedAlum','LogoPicture')
#		buttonText=('Head Pciture','Cloud Disk','Cloud Album','Shared Alum','Logo Picture')
		buttonObjName=('HeadPicture','CloudDisk','CloudAlbum','SharedAlum','AllFuction')
		buttonText=('Head Pciture','Cloud Disk','Cloud Album','Shared Alum','AllFuction')
		for i in range(len(buttonObjName)):
			button=QtGui.QPushButton()
			button.setFixedSize(70,80)
			if 0 != i:
				button.setText(buttonText[i])
			button.setObjectName(buttonObjName[i])
			button.setFlat(True)
			button.setCheckable(True)
			button.setFocusPolicy(QtCore.Qt.NoFocus)
			self.buttonDict[buttonObjName[i]]=button

		self.buttonDict['HeadPicture'].setFocusPolicy(QtCore.Qt.NoFocus)
		self.buttonDict['HeadPicture'].setCursor(QtCore.Qt.PointingHandCursor)

		self.accountComboBox=QtGui.QComboBox()
		self.accountComboBox.setFixedWidth(160)
		self.nameLineEdit=QtGui.QLineEdit()
		self.nameLineEdit.setFixedWidth(116)
		self.levelLabel=QtGui.QLabel('level 1')
		self.levelLabel.setFixedWidth(40)
		self.storageProgress=QtGui.QProgressBar()
		self.storageProgress.setFixedWidth(160)


		sndLayout=QtGui.QVBoxLayout()
		sndLayout.addWidget(self.accountComboBox)

		trdLayout=QtGui.QHBoxLayout()
		trdLayout.addWidget(self.nameLineEdit)
		trdLayout.addWidget(self.levelLabel)
		sndLayout.addLayout(trdLayout)

		sndLayout.addWidget(self.storageProgress)
		sndLayout.setSpacing(4)


		mainLayout=QtGui.QHBoxLayout()
		mainLayout.addWidget(self.buttonDict['HeadPicture'])
		mainLayout.addLayout(sndLayout)
		mainLayout.addWidget(self.buttonDict['CloudDisk'])
		mainLayout.addWidget(self.buttonDict['CloudAlbum'])
		mainLayout.addWidget(self.buttonDict['SharedAlum'])
		mainLayout.addWidget(self.buttonDict['AllFuction'])
		mainLayout.addStretch()
#		mainLayout.addWidget(self.buttonDict['LogoPicture'])
		mainLayout.setSpacing(20)
		self.setLayout(mainLayout)


	def initToolBarConnect(self):
		for objName,button in self.buttonDict.items():
			if objName!='HeadPicture':
				button.clicked.connect(self.buttonCheckedSlot)


	def buttonCheckedSlot(self):
		if self.sender()!=self.buttonDict['HeadPicture']:
			self.sender().setChecked(True)
			for objName,button in self.buttonDict.items():
				if button is not self.sender():
					button.setChecked(False)

	def setButtonChecked(self,buttonName):
		if buttonName in self.buttonDict:
			self.buttonDict[buttonName].setChecked(True)

def getQssFile(qssFile):
	qss=QtCore.QString('')
	result=False

	f=QtCore.QFile(qssFile)
	if f.open(QtCore.QFile.ReadOnly):
		qss=QtCore.QLatin1String(f.readAll())
		result=True
		f.close()

	return result,qss