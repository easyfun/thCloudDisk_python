#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thFrame import thframe
from thLib import thlib
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
	def __init__(self,color,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThColorLabel,self).__init__(parent,windowFlags)
		self.application=application
		#self.installEventFilter(self)
		self.installEventFilter(parent)
		self.color=color
		self.setFixedSize(120,120)
		self.setStyleSheet('''QLabel{background-color:%s;}''' % color)

		self.selectedButton=PictureButton(self)
		self.selectedButton.setFixedSize(20,20)
		self.selectedButton.setStyleSheet('''QToolButton{background-color:%s;border-style:none;}''' % color)
		self.selectedButton.move(92,92)

		#self.selectedButton.hide()
		self.selectedButton.iconFlag=0

class ThSkinDialog(thframe.ThFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThSkinDialog,self).__init__(parent,windowFlags)
		self.application=application
		self.initSkinData()
		self.initSkinUI()
		self.initSkinConnect()
		self.installEventFilter(self)

	def initSkinData(self):
		self.setObjectName('ThSkinDialog')
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint or QtCore.Qt.Tool)
		#self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.setWindowFlags(QtCore.Qt.Popup)
		self.themeDict={}
		self.themeObjList=[]
		self.themeNameList=[]
		self.hoverIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.off.selected.png')
		self.selectedIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.auto.selected.png')

	def initSkinUI(self):
	#	hideControl=('logoButton','skinButton','menuButton','minButton','maxButton')
	#	for hc in hideControl:
	#		self.getTitleBar().setControlVisible(hc,False)

		self.setResizeFrameFlag(False)
		self.setDragMoveFrameFlag(False)

		self.setTitleBarVisible(False)
		centralWidget=self.getCentralWidget()

		gridLayout=QtGui.QGridLayout()

		self.themeNameList=['black','blue','purple','green','red','teal']
		positions=[(i,j) for i in range(2) for j in range(3)]

		for position,themeName in zip(positions,self.themeNameList):
			themeLabel=ThColorLabel(themeName,self.application,self)
			self.themeDict[themeName]=themeLabel
			self.themeObjList.append(themeLabel)
			gridLayout.addWidget(themeLabel,*position)

		gridLayout.setContentsMargins(4,4,4,4)
		gridLayout.setSpacing(4)
		centralWidget.setLayout(gridLayout)

		'''系统默认主题teal'''
		self.currentTheme='teal'
		self.themeDict['teal'].selectedButton.iconFlag=2
		self.themeDict['teal'].selectedButton.setIcon(self.selectedIcon)
		self.themeDict['teal'].selectedButton.setIconSize(QtCore.QSize(20,20))
		self.themeDict['teal'].selectedButton.show()

	def initSkinConnect(self):
		pass

	def eventFilter(self,obj,event):
		if event.type()==QtCore.QEvent.MouseButtonPress:
			self.close()
			return True
	
		#return super(ThSkinDialog,self).eventFilter(obj,event)
	
		if obj in self.themeObjList:
			if event.type()==QtCore.QEvent.HoverEnter or\
				event.type()==QtCore.QEvent.HoverMove or\
				event.type()==QtCore.QEvent.Enter:
					if 1 != obj.selectedButton.iconFlag:
						obj.selectedButton.setIcon(self.hoverIcon)
						obj.selectedButton.setIconSize(QtCore.QSize(20,20))
						obj.selectedButton.iconFlag=1

					if not obj.selectedButton.isVisible():
						obj.selectedButton.show()

					#改变皮肤
					getQss,qss=thlib.getQssFile('./skin/qss/%s.qss' % obj.color)
					if getQss:
						self.application.setStyleSheet(qss)

					return True

			if event.type()==QtCore.QEvent.HoverLeave or\
				event.type()==QtCore.QEvent.Leave:
				if 2==obj.selectedButton.iconFlag or obj==self.themeDict[self.currentTheme]:
				#if obj==self.themeDict[self.currentTheme]:
					obj.selectedButton.iconFlag=2
					obj.selectedButton.setIcon(self.selectedIcon)
					obj.selectedButton.setIconSize(QtCore.QSize(20,20))
					obj.selectedButton.show()
				else:
					obj.selectedButton.iconFlag=0
					obj.selectedButton.hide()

					#改变皮肤
					getQss,qss=thlib.getQssFile('./skin/qss/%s.qss' % self.currentTheme)
					if getQss:
						self.application.setStyleSheet(qss)

				return True


			if event.type()==QtCore.QEvent.MouseButtonPress or\
				event.type()==QtCore.QEvent.MouseButtonRelease or\
				event.type()==QtCore.QEvent.MouseButtonDblClick:

				if 2 != obj.selectedButton.iconFlag:
					self.themeDict[self.currentTheme].selectedButton.iconFlag=0
					self.themeDict[self.currentTheme].selectedButton.hide()

					obj.selectedButton.setIcon(self.selectedIcon)
					obj.selectedButton.setIconSize(QtCore.QSize(20,20))
					obj.selectedButton.show()
					obj.selectedButton.iconFlag=2
					self.currentTheme=self.themeNameList[self.themeObjList.index(obj)]
					getQss,qss=thlib.getQssFile('./skin/qss/%s.qss' % self.currentTheme)
					if getQss:
						self.application.setStyleSheet(qss)
					#obj.selectedTheme=1

				return True

		return super(ThSkinDialog,self).eventFilter(obj,event)

def main():
	app=QtGui.QApplication(sys.argv)
	w=ThSkinDialog()
	w.setGeometry(100,100,200,200)
	w.show()
	sys.exit(app.exec_())

if '__main__'==__name__:
	main()