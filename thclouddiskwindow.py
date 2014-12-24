#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thFrame import thframe
from thLib import thlib
from thTitleBar import thskindialog
from thToolBar import thtoolbar

class ThCloudDiskWindow(thframe.ThFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThCloudDiskWindow,self).__init__(parent,windowFlags)
		self.application=application
		self.initCloudDiskData()
		self.initCloudDiskUI()
		self.initCloudDiskConnect()

	def initCloudDiskData(self):
		self.sd=None
		self.pageViewDict={}
		self.pageIndexDict={}

	def initCloudDiskUI(self):
		self.toolbar=thtoolbar.ThToolBar(self.application,self)
		self.toolbar.setMouseTracking(True)

		self.pageView=QtGui.QStackedWidget()
		self.pageView.setMouseTracking(True)

		pageviews=('CloudDisk','CloudAlbum','SharedAlum','AllFuction')
		for view,index in zip(pageviews,range(len(pageviews))):
			pv=QtGui.QLabel(view)
			strView=QtCore.QString(view)
			self.pageViewDict[strView]=pv
			self.pageIndexDict[strView]=index
			self.pageView.addWidget(pv)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addWidget(self.toolbar)
		mainLayout.addWidget(self.pageView)
		mainLayout.setContentsMargins(0,0,0,0)
		self.getCentralWidget().setLayout(mainLayout)

		self.toolbar.setButtonChecked('CloudDisk')
		self.pageView.setCurrentIndex(0)

	def initCloudDiskConnect(self):
		self.titleBar.skinButtonClicked.connect(self.skinDialog)
		for objName,button in self.toolbar.buttonDict.items():
			if objName!='HeadPicture':
				button.clicked.connect(self.buttonCheckedSlot)

	def buttonCheckedSlot(self):
		objectName=self.sender().objectName()
		if objectName in self.pageIndexDict:
			self.pageView.setCurrentIndex(self.pageIndexDict[objectName])
#			pageviews=('HeadPicture','CloudDisk','CloudAlbum','SharedAlum','AllFuction')
#			for i in range(len(pageviews)):
#				if pageviews[i]==self.sender().objectName():
#					self.pageView.setCurrentIndex(i)
#					break


	def skinDialog(self):
	 	
	 	if self.sd:
	 		pass
	 	else:
			self.sd=thskindialog.ThSkinDialog(self.application,self)
		
		#在skinMenu按钮下方以菜单形式显示
		self.sd.resize(200,200)
		rect=self.getTitleBar().getControlGeometry('skinButton')
		rectFrame=self.sd.geometry()
		frameBottomRight=QtCore.QPoint(rect.right(),rect.bottom())
		frameBottomRight=self.mapToGlobal(frameBottomRight)
		self.sd.setGeometry(frameBottomRight.x()-rectFrame.width(),frameBottomRight.y(),rectFrame.width(),rectFrame.height())
#		self.sd.move(rectSD.topLeft())
	 	#self.sd.show()
		
		#模态对话框主窗口居中显示

		#self.sd=thskindialog.ThSkinDialog()
		#self.sd.setParent(self)
		#self.sd.resize(200,200)
#		rectFG=self.frameGeometry()
#		cpFG=rectFG.center()
#		rectSD=self.sd.geometry()
#		rectSD.moveCenter(cpFG)
#		self.sd.move(rectSD.topLeft())
		
		#self.sd.exec_()
		#self.setWindowModality(QtCore.Qt.ApplicationModal)
		
		self.sd.show()
		self.sd.raise_()
		self.sd.activateWindow()


def main():
	app=QtGui.QApplication(sys.argv)
	print(sys.argv)
	getQss,qss=thlibs.getQssFile('./skin/qss/black.qss')

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThCloudDiskWindow()
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()