#!usr/bin/python
# -*- coding:utf8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thBasic import thframe
from thBasic import thlibs
from thTitleBar import thskindialog

class ThCloudDiskWindow(thframe.ThFrame):
	def __init__(self,application,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThCloudDiskWindow,self).__init__(parent,windowFlags)
		self.application=application
		self.initCloudDiskData()
		self.initCloudDiskUI()
		self.initCloudDiskConnect()

	def initCloudDiskData(self):
		self.sd=None

	def initCloudDiskUI(self):
		pass

	def initCloudDiskConnect(self):
		self.titleBar.skinButtonClicked.connect(self.skinDialog)


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