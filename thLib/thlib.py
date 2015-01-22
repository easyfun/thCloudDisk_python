#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore

def getQssFile(qssFile):
	qss=QtCore.QString('')
	result=False

	f=QtCore.QFile(qssFile)
	if f.open(QtCore.QFile.ReadOnly):
		qss=QtCore.QLatin1String(f.readAll())
		result=True
		f.close()

	return result,qss

def get_pyfile_dirname(pyfile):
	return os.path.dirname(os.path.realpath(pyfile))

