#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class SafeBox(QtGui.QFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(SafeBox,self).__init__(parent)
		self.application=application
		self.setObjectName('ViewCloudDiskSafeBox')
		self.initSafeBoxData()
		self.initSafeBoxUI()
		self.initSafeBoxConnect()

	def initSafeBoxData(self):
		pass

	def initSafeBoxUI(self):
		self.groupBox=QtGui.QGroupBox()
		self.groupBox.setFixedHeight(200)

		self.labelPixmap=QtGui.QLabel()
		self.labelPixmap.setFixedSize(160,160)
		self.labelPixmap.setPixmap(QtGui.QPixmap('./thPageView/pvclouddisk/safebox.png'))

		self.labelTsxx=QtGui.QLabel('The safebox has locked')
		self.labelTsxx.setStyleSheet('''QLabel{
			font-size:20px;
			}''')

		self.lineEditPassword=QtGui.QLineEdit()
		self.lineEditPassword.setFixedHeight(40)

		self.buttonSure=QtGui.QPushButton()
		self.buttonSure.setText('Entry')
		self.buttonSure.setFixedSize(80,40)

		self.labelForgetPassword=QtGui.QLabel('<u>Forget safebox password</u>')
		self.labelForgetPassword.setStyleSheet('''QLabel{
			font-size:16px;
			}''')

		self.labelModifyPassword=QtGui.QLabel('<u>Modify safebox password</u>')
		self.labelModifyPassword.setStyleSheet('''QLabel{
			font-ssze:16px;
			}''')

		gridLayout=QtGui.QGridLayout()
		gridLayout.setRowStretch(0,4)
		gridLayout.setRowStretch(4,1)
		gridLayout.addWidget(self.labelTsxx,1,0,1,2)
		gridLayout.addWidget(self.lineEditPassword,2,0)
		gridLayout.addWidget(self.buttonSure,2,1)
		gridLayout.addWidget(self.labelForgetPassword,3,0)
		gridLayout.addWidget(self.labelModifyPassword,3,1)
		gridLayout.setSpacing(10)

		groupLayout=QtGui.QHBoxLayout()
		groupLayout.addStretch()
		groupLayout.addWidget(self.labelPixmap)
		groupLayout.addLayout(gridLayout)
		groupLayout.addStretch()
		self.groupBox.setLayout(groupLayout)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addStretch()
		mainLayout.addWidget(self.groupBox)
		mainLayout.addStretch()
		self.setLayout(mainLayout)

	def initSafeBoxConnect(self):
		pass