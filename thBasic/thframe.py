# !sr/bin/python
# -*- coding:utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

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

	def initUI(self):
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

	def initConnect(self):
		pass



import sys

def main():
	app=QtGui.QApplication(sys.argv)
	window=ThFrame()
	window.setGeometry(100,100,800,600)
	window.setWindowTitle('ThFrame')
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()