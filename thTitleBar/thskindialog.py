#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
#from thBasic import thtitlebar

class ThColorLabel(QtGui.QLabel):
	def __init__(self,color,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThColorLabel,self).__init__(parent,windowFlags)
		self.color=color
		self.setFixedSize(120,120)
		self.setStyleSheet('''QLabel{background-color:%s;}''' % color)

		self.hoverIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.off.selected.png')
		self.selectedIcon=QtGui.QIcon('./skin/icons/appbar.camera.flash.auto.selected.png')

		self.selectedButton=QtGui.QToolButton(self)
		self.selectedButton.installEventFilter(self)
		
		self.selectedButton.setFixedSize(20,20)
		self.selectedButton.setStyleSheet('''QToolButton{background-color:%s;border-style:none;}''' % color)
		self.selectedButton.move(100,100)

		#self.selectedButton.hide()
		
		self.selectedButton.setIcon(self.selectedIcon)
		self.selectedButton.setIconSize(QtCore.QSize(20,20))

		

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