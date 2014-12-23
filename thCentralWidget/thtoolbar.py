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

		buttonObjName=('HeadPicture','CloudDisk','CloudAlbum','SharedAlum','LogoPicture')
		buttonText=('Head Pciture','Cloud Disk','Cloud Album','Shared Alum','Logo Picture')
		for i in range(5):
			button=QtGui.QPushButton()
			if buttonObjName[i]=='logoPicButton':
				button.setFixedSize(120,80)
			else:
				button.setFixedSize(80,80)
				button.setText(buttonText[i])
			button.setObjectName(buttonObjName[i])
			button.setFlat(True)
			button.setCheckable(True)
			self.buttonDict[buttonObjName[i]]=button

#		self.buttonDict['HeadPicture'].setStyleSheet('''QPushButton{
#					background-image:url(../skin/icons/appbar.group.png);
#					background-repeat:no-repeat;
#					background-position:center top;
#					background-color:transparent;
#					text-align:center bottom;
#					padding-bottom:5px;
#					border-bottom: 2px solid black;}''')

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
		mainLayout.addStretch()
		mainLayout.addWidget(self.buttonDict['LogoPicture'])
		mainLayout.setSpacing(20)
		self.setLayout(mainLayout)


	def initToolBarConnect(self):
		for objName,button in self.buttonDict.items():
			button.clicked.connect(self.buttonCheckedSlot)


	def buttonCheckedSlot(self):
		self.sender().setChecked(True)
		for objName,button in self.buttonDict.items():
			if button is not self.sender():
				button.setChecked(False)

def getQssFile(qssFile):
	qss=QtCore.QString('')
	result=False

	f=QtCore.QFile(qssFile)
	if f.open(QtCore.QFile.ReadOnly):
		qss=QtCore.QLatin1String(f.readAll())
		result=True
		f.close()

	return result,qss

def main():
	app=QtGui.QApplication(sys.argv)

	getQss,qss=getQssFile('../skin/qss/teal.qss')
	if getQss:
		app.setStyleSheet(qss)

	w=ThToolBar(app)
	w.setGeometry(100,100,300,94)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()