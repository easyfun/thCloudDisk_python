#!usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from thFrame import thframe
from thLib import thlib
from thclouddiskwindow import ThCloudDiskWindow

if __name__=='__main__':
	
	app=QtGui.QApplication(sys.argv)

	qss_file_path=os.path.join(thlib.get_pyfile_dirname(__file__),'skin','qss','teal.qss')
	getQss,qss=thlib.getQssFile(qss_file_path) # './skin/qss/teal.qss'

	if getQss:
		app.setStyleSheet(qss)
		pass

	w=ThCloudDiskWindow(app)
	w.setGeometry(100,100,800,600)
	w.show()
	sys.exit(app.exec_())
	