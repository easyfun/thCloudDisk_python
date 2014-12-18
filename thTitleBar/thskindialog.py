#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
#from thBasic import thtitlebar

class ThSkinDialog(thframe.ThFrame):
	def __init__(self,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThSkinDialog,self).__init__(parent,windowFlags)
		self.initSkinData()
		self.initSkinUI()
		self.initSkinConnect()
		self.installEventFilter(self)

	def initSkinData(self):
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint or QtCore.Qt.Popup)
		#self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.setWindowFlags(QtCore.Qt.Popup)
		pass

	def initSkinUI(self):
		hideControl=('logoButton','skinButton','menuButton','minButton','maxButton')
		for hc in hideControl:
			self.getTitleBar().setControlVisible(hc,False)

		self.setResizeFrameFlag(False)
		#self.setDragMoveFrameFlag(False)

		centralWidget=self.getCentralWidget()
		print(centralWidget)
		gridLayout=QtGui.QGridLayout()
		blackSkin=QtGui.QLabel('BlackSkin')
		blueSkin=QtGui.QLabel('BlueSkin')
		graySkin=QtGui.QLabel('GraySkin')
		yellowSkin=QtGui.QLabel('YellowSkin')
		redSkin=QtGui.QLabel('RedSkin')
		tealSkin=QtGui.QLabel('TealSkin')

		gridLayout.addWidget(blueSkin,0,0)
		gridLayout.addWidget(blackSkin,0,1)
		gridLayout.addWidget(graySkin,0,2)
		gridLayout.addWidget(yellowSkin,1,0)
		gridLayout.addWidget(redSkin,1,1)
		gridLayout.addWidget(tealSkin,1,2)
		gridLayout.setRowStretch(2,1)
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