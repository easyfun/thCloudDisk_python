# !sr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import thtitlebar

class ThFrame(QtGui.QFrame):
	def __init__(self,parent=None,windowFlags=QtCore.Qt.Widget):
		super(ThFrame,self).__init__(parent,windowFlags)
		self.initData()
		self.initUI()
		self.initConnect()

	def initData(self):
		'''dragDirection:0-left,1-right,2-top,3-bottom,4-topleft,5-topright,6-bottomleft,7-bottomright,8-normal
		'''
		self.resizeFrameFlag=True	#缩放窗口大小标志
		self.dragMoveFrameFlag=True	#拖动窗口位置
		self.leftMousePress=False
		self.dragDirection=8
		self.showMaximumFlag=False 	#最大化显示标志

	def initUI(self):
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setMouseTracking(True)

		self.titleBar=thtitlebar.ThTitleBar()
		self.titleBar.setMouseTracking(True)

		self.centralWidget=QtGui.QFrame()#QtGui.QLabel('centralWidget')
		self.centralWidget.setMouseTracking(True)
		print(self.centralWidget)

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
		#禁止缩放窗口大小
		#if False==self.resizeFrameFlag:
		#	return

		#禁止拖动窗口位置
		#if False==self.dragMoveFrameFlag:
		#	return

		if self.leftMousePress:
			if self.showMaximumFlag:
				pass
				#self.setGeometry(self.rectFrame)
			#移动窗口位置
			elif 8==self.dragDirection and self.dragMoveFrameFlag:
				rectFrame=self.geometry()
				self.move(rectFrame.left()+e.globalX()-self.globalStartPosition.x(),
						rectFrame.top()+e.globalY()-self.globalStartPosition.y())
				self.globalStartPosition=e.globalPos()
			elif self.resizeFrameFlag:
				#调整窗口大小
				self.resizeFrame(e.globalX(),e.globalY(),self.dragDirection)
				self.globalStartPosition=e.globalPos()
		else:
			if self.showMaximumFlag:
				self.setCursorStyle(8)
			elif self.resizeFrameFlag:
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
		self.showMaximumFlag=True
		self.setGeometry(0,0,QtGui.QApplication.desktop().availableGeometry().width(),QtGui.QApplication.desktop().availableGeometry().height())

		#鼠标点最大化按钮，不移动鼠标，最大化按钮显示状态不正确

		#给最大化按钮发送leaveEnvent事件，更新显示
		#hoverLeave=QtGui.QHoverEvent(QtCore.QEvent.HoverLeave,QtCore.QPoint(-1,-1),QtCore.QPoint(-1,-1))
		#if QtGui.QApplication.sendEvent(self.getTitleBar().getControl('maxButton'),hoverLeave):
		#	print('send hoverLeave ok')
		
		#mouseEvent=QtGui.QMouseEvent(QtCore.QEvent.MouseMove,QtCore.QPoint(10,10),
		#	QtCore.Qt.NoButton,QtCore.Qt.NoButton,QtCore.Qt.NoModifier)
		#if QtGui.QApplication.sendEvent(self.getTitleBar().getControl('maxButton'),mouseEvent):
		#	print('send mouseEvent ok')

		self.centralWidget.setFocus(QtCore.Qt.MouseFocusReason)

	def showNormalSlot(self):
		self.showMaximumFlag=False
		self.setGeometry(self.rectFrame)

	def getTitleBar(self):
		'''获取标题栏对象'''
		return self.titleBar

	def setResizeFrameFlag(self,flag):
		'''设置窗口缩放'''
		self.resizeFrameFlag=flag

	def setDragMoveFrameFlag(self,flag):
		'''设置窗口拖动'''
		self.dragMoveFrameFlag=flag

	def getCentralWidget(self):
		'''获取视图对象'''
		return self.centralWidget

	def setTitleBarVisible(self,visible):
		if visible:
			self.titleBar.show()
		else:
			self.titleBar.hide()
		
def main():
	app=QtGui.QApplication(sys.argv)
	window=ThFrame()
	window.setGeometry(100,100,800,600)
	window.setWindowTitle('ThFrame')
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()