#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thFrame import thframe
from thLib import thlib
from thTitleBar import thskindialog
from thToolBar import thtoolbar
from thPageView.thviewclouddisk import thViewCloudDisk
from thPageView.thviewcloudalbum import thViewCloudAlbum
from thPageView.thviewsharedalbum import thViewSharedAlbum
from thPageView.thviewallfunction import thViewAllFunction

class ThCloudDiskWindow(thframe.ThFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThCloudDiskWindow,self).__init__(parent,windowFlags)
		self.setObjectName('ThCloudDiskWindow')
		self.application=application
		self.initCloudDiskData()
		self.initCloudDiskUI()
		self.initCloudDiskConnect()

	def initCloudDiskData(self):
		self.sd=None
		self.pageViewDict={}
		self.pageIndexDict={}

	def initCloudDiskUI(self):
		#设置标题栏菜单
		'''
		0-类型:0-无子菜单,1-有子菜单
		1-图标
		2-text
		3-快捷键
		4-是否增加分组符
		5-action_object
		'''
		actions=[[0,'',u'暂停传送','Ctrl+P',0],
				[0,'',u'查看传输列表','Ctrl+V',0],
				[0,'',u'本次传输完自动关机','Ctrl+T',1],
				[0,'',u'更换帐号','Ctrl+A',1],
				[0,'',u'隐藏悬浮框','Ctrl+X',0],
				[0,'',u'设置','Ctrl+S',1],
				[0,'',u'打开云盘网页版','Ctrl+W',0],
				[1,'',u'帮助','Ctrl+H',0],
				[0,'',u'在线升级','Ctrl+U',1],
				[0,'',u'锁定云盘','Ctrl+L',1],
				[0,'',u'退出','Ctrl+E',0]]
		self.menu=QtGui.QMenu(self)
		for index in range(len(actions)):
			action=QtGui.QAction(QtGui.QIcon(actions[index][1]),actions[index][2],self)
			#action.setShortcut(actions[index][3])
			actions[index].append(action)
			self.menu.addAction(action)
			if 1==actions[index][4]:
				self.menu.addSeparator()
		#print self.titleBar
		#print self.titleBar.getControl('menuButton')
		#self.titleBar.getControl('menuButton').setMenu(self.menu)
		
		#self.titleBar.menuButton.setArrowType(QtCore.Qt.NoArrow)
		#self.titleBar.menuButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
		self.titleBar.menuButton.setMenu(self.menu)
		self.titleBar.menuButton.clicked.connect(self.titleBar.menuButton.showMenu)

		self.toolbar=thtoolbar.ThToolBar(self.application,self)
		self.toolbar.setMouseTracking(True)

		self.pageView=QtGui.QStackedWidget()
		self.pageView.setMouseTracking(True)

		#pageviews=('CloudDisk','CloudAlbum','SharedAlum','AllFuction')
		#for view,index in zip(pageviews,range(len(pageviews))):
		#	pv=QtGui.QLabel(view)
		#	strView=QtCore.QString(view)
		#	self.pageViewDict[strView]=pv
		#	self.pageIndexDict[strView]=index
		#	self.pageView.addWidget(pv)

		pv=thViewCloudDisk(self.application)
		strView=QtCore.QString('CloudDisk')
		self.pageViewDict[strView]=pv
		self.pageIndexDict[strView]=0
		self.pageView.addWidget(pv)

		pv=thViewCloudAlbum(self.application)
		strView=QtCore.QString('CloudAlbum')
		self.pageViewDict[strView]=pv
		self.pageIndexDict[strView]=1
		self.pageView.addWidget(pv)

		pv=thViewSharedAlbum(self.application)
		strView=QtCore.QString('SharedAlum')
		self.pageViewDict[strView]=pv
		self.pageIndexDict[strView]=2
		self.pageView.addWidget(pv)

		pv=thViewAllFunction(self.application)
		strView=QtCore.QString('AllFuction')
		self.pageViewDict[strView]=pv
		self.pageIndexDict[strView]=3
		self.pageView.addWidget(pv)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addWidget(self.toolbar)
		mainLayout.addWidget(self.pageView)
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(0)
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
	import os
	app=QtGui.QApplication(sys.argv)
	print(sys.argv)

	qss_file_path=os.path.join(thlib.get_pyfile_dirname(__file__),'skin','qss','teal.qss')
	getQss,qss=thlib.getQssFile(qss_file_path) # './skin/qss/black.qss'

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThCloudDiskWindow(app)
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()