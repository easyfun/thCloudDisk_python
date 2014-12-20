#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
#from thBasic import thtitlebar

class PictureButton(QtGui.QToolButton):
	def __init__(self,parent=None):
		super(PictureButton,self).__init__(parent)
		self.eventType=QtCore.QEvent.None
		self.setFocusPolicy(QtCore.Qt.NoFocus)
		self.setStyleSheet('QToolButton{border-style:none;}')
		self.setIcon(QtGui.QIcon('./picture.png'))
		self.setIconSize(QtCore.QSize(40,40))
		self.installEventFilter(self)
		self.iconFlag=0 #0-无ICON,1-hover,2-selected

	def eventFilter(self,obj,event):
		if event.type()==QtCore.QEvent.HoverEnter or\
			event.type()==QtCore.QEvent.HoverLeave or\
			event.type()==QtCore.QEvent.HoverMove or\
			event.type()==QtCore.QEvent.Leave or\
			event.type()==QtCore.QEvent.Enter or\
			event.type()==QtCore.QEvent.KeyPress or\
			event.type()==QtCore.QEvent.KeyRelease or\
			event.type()==QtCore.QEvent.MouseButtonPress or\
			event.type()==QtCore.QEvent.MouseButtonRelease or\
			event.type()==QtCore.QEvent.MouseButtonDblClick:
			return True

		return super(PictureButton,self).eventFilter(obj,event)

class ThColorLabel(QtGui.QLabel):
	def __init__(self,color,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThColorLabel,self).__init__(parent,windowFlags)
		self.installEventFilter(self)
		self.color=color
		self.setFixedSize(120,120)
		self.setStyleSheet('''QLabel{background-color:%s;}''' % color)

		self.hoverIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.off.selected.png')
		self.selectedIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.auto.selected.png')

		self.selectedButton=PictureButton(self)
		self.selectedButton.setFixedSize(20,20)
		self.selectedButton.setStyleSheet('''QToolButton{background-color:%s;border-style:none;}''' % color)
		self.selectedButton.move(92,92)

		self.selectedButton.hide()
		self.selectedButton.iconFlag=0
		

	def eventFilter(self,obj,event):
		if event.type()==QtCore.QEvent.HoverEnter or\
			event.type()==QtCore.QEvent.HoverMove or\
			event.type()==QtCore.QEvent.Enter:
			if 1 != self.selectedButton.iconFlag:
				self.selectedButton.setIcon(self.hoverIcon)
				self.selectedButton.setIconSize(QtCore.QSize(20,20))
				self.selectedButton.iconFlag=1

			if not self.selectedButton.isVisible():
				self.selectedButton.show()
			return True

		if event.type()==QtCore.QEvent.HoverLeave or\
			event.type()==QtCore.QEvent.Leave:
			if 2==self.selectedButton.iconFlag:
				self.selectedButton.show()
			else:
				self.selectedButton.hide()
			return True


		if event.type()==QtCore.QEvent.MouseButtonPress or\
			event.type()==QtCore.QEvent.MouseButtonRelease or\
			event.type()==QtCore.QEvent.MouseButtonDblClick:

			if 2 != self.selectedButton.iconFlag:
				self.selectedButton.setIcon(self.selectedIcon)
				self.selectedButton.setIconSize(QtCore.QSize(20,20))
				self.selectedButton.show()
				self.selectedButton.iconFlag=2

			return True
	
		
		return super(ThColorLabel,self).eventFilter(obj,event)		


class ThSkinDialog(thframe.ThFrame):
	def __init__(self,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThSkinDialog,self).__init__(parent,windowFlags)
		self.initSkinData()
		self.initSkinUI()
		self.initSkinConnect()
		self.installEventFilter(self)

	def initSkinData(self):
		self.setObjectName('ThSkinDialog')
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint or QtCore.Qt.Tool)
		#self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.setWindowFlags(QtCore.Qt.Popup)
		self.colorDict={}
		pass

	def initSkinUI(self):
	#	hideControl=('logoButton','skinButton','menuButton','minButton','maxButton')
	#	for hc in hideControl:
	#		self.getTitleBar().setControlVisible(hc,False)

	#	self.setResizeFrameFlag(False)
		#self.setDragMoveFrameFlag(False)

		self.setTitleBarVisible(False)
		centralWidget=self.getCentralWidget()

		gridLayout=QtGui.QGridLayout()

#		blackSkin=QtGui.QLabel('BlackSkin')
#		blueSkin=QtGui.QLabel('BlueSkin')
#		graySkin=QtGui.QLabel('PurpleSkin')
#		yellowSkin=QtGui.QLabel('YellowSkin')
#		redSkin=QtGui.QLabel('RedSkin')
#		tealSkin=QtGui.QLabel('TealSkin')

#		gridLayout.addWidget(blueSkin,0,0)
#		gridLayout.addWidget(blackSkin,0,1)
#		gridLayout.addWidget(graySkin,0,2)
#		gridLayout.addWidget(yellowSkin,1,0)
#		gridLayout.addWidget(redSkin,1,1)
#		gridLayout.addWidget(tealSkin,1,2)
#		gridLayout.setRowStretch(2,1)

		colors=['black','blue','purple','pink','red','teal']
		positions=[(i,j) for i in range(2) for j in range(3)]

		for position,color in zip(positions,colors):
			colorLabel=ThColorLabel(color)
			self.colorDict[color]=colorLabel
			gridLayout.addWidget(colorLabel,*position)

		print(self.colorDict)
		gridLayout.setContentsMargins(4,4,4,4)
		gridLayout.setSpacing(4)
		centralWidget.setLayout(gridLayout)

		#self.setGeometry(100,100,200,200)

	def initSkinConnect(self):
		pass

	def eventFilter(self,obj,event):
		if event.type()==QtCore.QEvent.MouseButtonPress:
			self.close()
			return True
		else:	
			return super(ThSkinDialog,self).eventFilter(obj,event)

def main():
	app=QtGui.QApplication(sys.argv)
	w=ThSkinDialog()
	w.setGeometry(100,100,200,200)
	w.show()
	sys.exit(app.exec_())

if '__main__'==__name__:
	main()