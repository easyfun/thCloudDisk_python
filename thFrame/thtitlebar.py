#!usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ThTitleBar(QtGui.QFrame):
	closeButtonClicked=QtCore.pyqtSignal()
	minButtonClicked=QtCore.pyqtSignal()
	maximumShow=QtCore.pyqtSignal()
	normalShow=QtCore.pyqtSignal()
	menuButtonClicked=QtCore.pyqtSignal()
	skinButtonClicked=QtCore.pyqtSignal()

	def __init__(self,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThTitleBar,self).__init__(parent,windowFlags)
		self.initData()
		self.initUI()
		self.initConnect()
		self.setFocusPolicy(QtCore.Qt.NoFocus)

	def initData(self):
		self.setObjectName('ThTitleBar')
		#Flase-正常,True-最大化
		self.maxButtonStatus=True
		self.maxIcon=QtGui.QIcon('./skin/icons/appbar.fullscreen.box.png')
		self.normalIcon=QtGui.QIcon('./skin/icons/appbar.app.png')

	def initUI(self):
		self.setFixedHeight(28)
		self.titleLabel=QtGui.QLabel("ThCloudDisk")
		self.logoButton=QtGui.QToolButton()
		self.skinButton=QtGui.QToolButton()
		self.menuButton=QtGui.QToolButton()
		self.minButton=QtGui.QToolButton()
		self.maxButton=QtGui.QToolButton()
		self.closeButton=QtGui.QToolButton()
		
		self.titleLabel.setFocusPolicy(QtCore.Qt.NoFocus)
		self.logoButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.skinButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.menuButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.minButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.maxButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)

		self.closeButton.setObjectName('closeApplication')
		self.setToolButtonIcon(self.skinButton, "./skin/icons/appbar.clothes.shirt.png")
		self.setToolButtonIcon(self.menuButton, "./skin/icons/appbar.control.down.png")
		self.setToolButtonIcon(self.minButton, "./skin/icons/appbar.minus.png")
		self.setToolButtonIcon(self.closeButton, "./skin/icons/appbar.close.png")
		self.maxButton.setIcon(self.normalIcon)
		#self.maxButton.setIconSize(QtCore.QSize(self.height()-3,self.height()-3))
		self.maxButton.setIconSize(QtCore.QSize(20,20))

		self.menuButton.setArrowType(QtCore.Qt.NoArrow)
		#self.menuButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)


		self.controlDict={
				'titleLabel':self.titleLabel,
				'logoButton':self.logoButton,
				'skinButton':self.skinButton,
				'menuButton':self.menuButton,
				'minButton':self.minButton,
				'maxButton':self.maxButton,
				'maxButton':self.maxButton,
				'closeButton':self.closeButton
				}

		mainLayout=QtGui.QHBoxLayout()
		mainLayout.addWidget(self.logoButton)
		mainLayout.addWidget(self.titleLabel)
		mainLayout.addStretch()
		mainLayout.addWidget(self.skinButton)
		mainLayout.addWidget(self.menuButton)
		mainLayout.addWidget(self.minButton)
		mainLayout.addWidget(self.maxButton)
		mainLayout.addWidget(self.closeButton)
		mainLayout.setContentsMargins(3,3,3,0)
		mainLayout.setSpacing(0)
		self.setLayout(mainLayout)

	def initConnect(self):
		self.closeButton.clicked.connect(self.closeButtonClicked)
		self.maxButton.clicked.connect(self.maxButtonClickedHandler)
		self.minButton.clicked.connect(self.minButtonClicked)
		self.menuButton.clicked.connect(self.menuButtonClicked)
		self.skinButton.clicked.connect(self.skinButtonClicked)

	def setToolButtonIcon(self,toolButton,strIcon):
		toolButton.setIcon(QtGui.QIcon(strIcon))
		#toolButton.setIconSize(QtCore.QSize(self.height()-3,self.height()-3))
		toolButton.setIconSize(QtCore.QSize(20,20))

	def maxButtonClickedHandler(self):
		if self.maxButtonStatus:
			self.maxButtonStatus=False
			self.maxButton.setIcon(self.maxIcon)
			#self.maxButton.setIconSize(QtCore.QSize(self.height()-3,self.height()-3))
			self.maxButton.setIconSize(QtCore.QSize(20,20))
			self.maximumShow.emit()
		else:
			self.maxButtonStatus=True
			self.maxButton.setIcon(self.normalIcon)
			#self.maxButton.setIconSize(QtCore.QSize(self.height()-3,self.height()-3))
			self.maxButton.setIconSize(QtCore.QSize(20,20))
			self.normalShow.emit()

	def mouseDoubleClickEvent(self,e):
		self.maxButtonClickedHandler()

	def setControlVisible(self,controlName,visible):
		if controlName in self.controlDict:
			if visible:
				self.controlDict[controlName].show()
			else:
				self.controlDict[controlName].hide()

	def getControlGeometry(self,controlName):
		if controlName in self.controlDict:
			if self.controlDict[controlName].isVisible():
				return self.controlDict[controlName].geometry()

	def  getControl(self,controlName):
		if controlName in self.controlDict:
			if self.controlDict[controlName].isVisible():
				return self.controlDict[controlName]

def main():
	app=QtGui.QApplication(sys.argv)
	window=ThTitleBar()
	window.setGeometry(100,100,800,600)
	#window.setWindowTitle('ThTitleBar')
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
