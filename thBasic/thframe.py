# !sr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import thtitlebar

class ThFrame(QtGui.QFrame):
	def __init__(self):
		super(ThFrame,self).__init__()
		self.initData()
		self.initUI()
		self.initConnect()

	def initData(self):
		'''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
		self.leftMousePress=False
		self.dragDirection=8
		self.showMaximumStatus=False

	def initUI(self):
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setMouseTracking(True)

		self.titleBar=thtitlebar.ThTitleBar()
		self.titleBar.setMouseTracking(True)
		self.centralWidget=QtGui.QLabel('centralWidget')
		self.centralWidget.setMouseTracking(True)
		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addWidget(self.titleBar)
		mainLayout.addWidget(self.centralWidget)
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(0)
		self.setLayout(mainLayout)
		self.rectFrame=self.geometry()

	def initConnect(self):
		self.titleBar.closeButtonClicked.connect(self.close)
		self.titleBar.minButtonClicked.connect(self.showMinimized)
		self.titleBar.maximumShow.connect(self.showMaxSlot)
		self.titleBar.normalShow.connect(self.showNormalSlot)

	def keyPressEvent(self,e):
		if e.key()==QtCore.Qt.Key_Escape:
			self.close()

	def mousePressEvent(self,e):
		if QtCore.Qt.LeftButton==e.button():
			self.leftMousePress=True
			self.globalStartPosition=e.globalPos()

	def mouseMoveEvent(self,e):
		if self.leftMousePress:
			if self.showMaximumStatus:
				pass
				#self.setGeometry(self.rectFrame)
			#移动窗口位置
			elif 8==self.dragDirection:
				rectFrame=self.geometry()
				self.move(rectFrame.left()+e.globalX()-self.globalStartPosition.x(),
						rectFrame.top()+e.globalY()-self.globalStartPosition.y())
				self.globalStartPosition=e.globalPos()
			else:
				#调整窗口大小
				self.resizeFrame(e.globalX(),e.globalY(),self.dragDirection)
				self.globalStartPosition=e.globalPos()
		else:
			if self.showMaximumStatus:
				self.setCursorStyle(8)
			else:
				self.dragDirection=self.getDragDirection(e.globalX(),e.globalY())
				self.setCursorStyle(self.dragDirection)

	def mouseReleaseEvent(self,e):
		if e.button()==QtCore.Qt.LeftButton:
			self.leftMousePress=False
			self.dragDirection=self.getDragDirection(e.globalX(),e.globalY())
			self.setCursorStyle(self.dragDirection)


	def resizeFrame(self,globalX,globalY,direction):
		#计算偏移量
		dX=globalX-self.globalStartPosition.x()
		dY=globalY-self.globalStartPosition.y()
		rectFrame=self.geometry()
		#计算新窗口位置
		'''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
		if 0==direction:
			rectFrame.setLeft(rectFrame.left()+dX)
		elif 1==direction:
			rectFrame.setRight(rectFrame.right()+dX)
		elif 2==direction:
			rectFrame.setTop(rectFrame.top()+dY)
		elif 3==direction:
			rectFrame.setBottom(rectFrame.bottom()+dY)
		elif 4==direction:
			rectFrame.setLeft(rectFrame.left()+dX)
			rectFrame.setTop(rectFrame.top()+dY)
		elif 5==direction:
			rectFrame.setRight(rectFrame.right()+dX)
			rectFrame.setTop(rectFrame.top()+dY)
		elif 6==direction:
			rectFrame.setLeft(rectFrame.left()+dX)
			rectFrame.setBottom(rectFrame.bottom()+dY)
		elif 7==direction:
			rectFrame.setRight(rectFrame.right()+dX)
			rectFrame.setBottom(rectFrame.bottom()+dY)

		if rectFrame.width()<self.minimumWidth() or rectFrame.height()<self.minimumHeight():
			return

		self.setGeometry(rectFrame)

	def getDragDirection(self,globalX,globalY):
		'''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
		rectFrame=self.geometry()
		left=rectFrame.left()
		right = rectFrame.right()
		top = rectFrame.top()
		bottom = rectFrame.bottom()

		if left <= globalX and globalX <= left+1 and top <= globalY and globalY <= top+1:
			return 4

		if left <= globalX and globalX <= left+1 and top+1 < globalY and globalY < bottom-1:
			return 0

		if left <= globalX and globalX <= left+1 and bottom-1 <= globalY and globalY <= bottom:
			return 6

		if left+1< globalX and globalX < right-1 and top <= globalY and globalY <= top+1:
			return 2

		if left+1 < globalX and globalX < right-1 and bottom-1 <= globalY and globalY <= bottom:
			return 3

		if right-1 <= globalX and globalX <= right and top <= globalY and globalY <= top+1:
			return 5

		if right-1 <= globalX and globalX <= right and top+1 < globalY and globalY < bottom-1:
			return 1

		if right-1 <= globalX and globalX <= right and bottom-1 <= globalY and globalY <= bottom:
			return 7
		return 8

	def setCursorStyle(self,direction):
		'''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
		if 0==direction or 1==direction:
			self.setCursor(QtCore.Qt.SizeHorCursor)
		elif 2==direction or 3==direction:
			self.setCursor(QtCore.Qt.SizeVerCursor)
		elif 4==direction or 7==direction:
			self.setCursor(QtCore.Qt.SizeFDiagCursor)
		elif 5==direction or 6==direction:
			self.setCursor(QtCore.Qt.SizeBDiagCursor)
		else:
			self.setCursor(QtCore.Qt.ArrowCursor)


	def showMaxSlot(self):
		self.rectFrame=self.geometry()
		self.showMaximumStatus=True
		self.setGeometry(0,0,QtGui.QApplication.desktop().availableGeometry().width(),QtGui.QApplication.desktop().availableGeometry().height())

	def  showNormalSlot(self):
		self.showMaximumStatus=False
		self.setGeometry(self.rectFrame)


def main():
	app=QtGui.QApplication(sys.argv)
	window=ThFrame()
	window.setGeometry(100,100,800,600)
	window.setWindowTitle('ThFrame')
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()