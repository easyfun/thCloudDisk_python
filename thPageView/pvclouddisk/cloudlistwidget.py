#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore

class DiskListWidget(QtGui.QFrame):
	def __init__(self):
		super(DiskListWidget,self).__init__()
		self.init_data()
		self.init_ui()
		self.init_connect()

	def init_data(self):
		pass

	def init_ui(self):
		self.setStyleSheet('''
			QWidget{
				background:white;
			}
			QPushButton#DiskListWidget_PushButton{
				border:none;
				text-align:left;
				padding-left: 30px;
				color: black;
			}
			QPushButton#DiskListWidget_PushButton:hover{
				border:none;
				background-color:teal;
			}
			QPushButton#DiskListWidget_PushButton:checked{
				border:none;
				background-color:teal;
			}
			QPushButton#DiskListWidget_PushButton:flat{
				border:none;
			}


			QGroupBox#DiskListWidget_All_Files{
				border:none;
			}
			QGroupBox#DiskListWidget_My_Shared{
				border:none;
				border-top:1px solid black;
			}
			QGroupBox#DiskListWidget_Can{
				border:none;
				border-top:1px solid black;
			}
			QGroupBox#DiskListWidget_History{
				border:none;
				border-top:1px solid black;
			}

			QPushButton#DiskListWidget_PushButton:hover{
				background:teal;
			}
			''')

		group_all_files=QtGui.QGroupBox()
		group_all_files.setObjectName('DiskListWidget_All_Files')
		group_my_shared=QtGui.QGroupBox()
		group_my_shared.setObjectName('DiskListWidget_My_Shared')
		group_can=QtGui.QGroupBox()
		group_can.setObjectName('DiskListWidget_Can')
		group_history=QtGui.QGroupBox()
		group_history.setObjectName('DiskListWidget_History')

		self.button_all_files=QtGui.QPushButton(u'全部文档')
		self.button_all_files.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_all_files.setIconSize(QtCore.QSize(16,16))
		self.button_all_files.setFixedHeight(32)
		self.button_all_files.setFlat(True)
		self.button_all_files.setCheckable(True)
		self.button_all_files.setFocusPolicy(QtCore.Qt.NoFocus)
		self.button_all_files.setObjectName('DiskListWidget_PushButton')

		self.button_file=QtGui.QPushButton()
		self.button_file.setObjectName('DiskListWidget_PushButton')
		self.button_file.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_file.setIconSize(QtCore.QSize(16,16))
		self.button_file.setFixedHeight(32)
		self.button_file.setFlat(True)
		self.button_file.setCheckable(True)
		self.button_file.setFocusPolicy(QtCore.Qt.NoFocus)

		self.button_music=QtGui.QPushButton()
		self.button_music.setObjectName('DiskListWidget_PushButton')
		self.button_music.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_music.setIconSize(QtCore.QSize(16,16))
		self.button_music.setFixedHeight(32)
		self.button_music.setFlat(True)
		self.button_music.setCheckable(True)
		self.button_music.setFocusPolicy(QtCore.Qt.NoFocus)

		self.button_vedio=QtGui.QPushButton()
		self.button_vedio.setObjectName('DiskListWidget_PushButton')
		self.button_vedio.setObjectName('DiskListWidget_PushButton')
		self.button_vedio.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_vedio.setIconSize(QtCore.QSize(16,16))
		self.button_vedio.setFixedHeight(32)
		self.button_vedio.setFlat(True)
		self.button_vedio.setCheckable(True)
		self.button_vedio.setFocusPolicy(QtCore.Qt.NoFocus)

		self.button_photo=QtGui.QPushButton()
		self.button_photo.setObjectName('DiskListWidget_PushButton')
		self.button_photo.setObjectName('DiskListWidget_PushButton')
		self.button_photo.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_photo.setIconSize(QtCore.QSize(16,16))
		self.button_photo.setFixedHeight(32)
		self.button_photo.setFlat(True)
		self.button_photo.setCheckable(True)
		self.button_photo.setFocusPolicy(QtCore.Qt.NoFocus)
		
		layout_all_files=QtGui.QVBoxLayout()
		layout_all_files.addWidget(self.button_all_files)
		layout_all_files.addWidget(self.button_file)
		layout_all_files.addWidget(self.button_music)
		layout_all_files.addWidget(self.button_vedio)
		layout_all_files.addWidget(self.button_photo)
		layout_all_files.setContentsMargins(0,2,0,0)
		layout_all_files.setSpacing(1)
		group_all_files.setLayout(layout_all_files)

		self.button_my_shared=QtGui.QPushButton()
		self.button_my_shared.setObjectName('DiskListWidget_PushButton')
		self.button_my_shared.setObjectName('DiskListWidget_PushButton')
		self.button_my_shared.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_my_shared.setIconSize(QtCore.QSize(16,16))
		self.button_my_shared.setFixedHeight(32)
		self.button_my_shared.setFlat(True)
		self.button_my_shared.setCheckable(True)
		self.button_my_shared.setFocusPolicy(QtCore.Qt.NoFocus)

		layout_my_shared=QtGui.QVBoxLayout()
		layout_my_shared.addWidget(self.button_my_shared)
		layout_my_shared.setContentsMargins(0,4,0,4)
		layout_my_shared.setSpacing(1)
		group_my_shared.setLayout(layout_my_shared)

		self.button_safe_box=QtGui.QPushButton()
		self.button_safe_box.setObjectName('DiskListWidget_PushButton')
		self.button_safe_box.setObjectName('DiskListWidget_PushButton')
		self.button_safe_box.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_safe_box.setIconSize(QtCore.QSize(16,16))
		self.button_safe_box.setFixedHeight(32)
		self.button_safe_box.setFlat(True)
		self.button_safe_box.setCheckable(True)
		self.button_safe_box.setFocusPolicy(QtCore.Qt.NoFocus)

		self.button_recycle_bin=QtGui.QPushButton()
		self.button_recycle_bin.setObjectName('DiskListWidget_PushButton')
		self.button_recycle_bin.setObjectName('DiskListWidget_PushButton')
		self.button_recycle_bin.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_recycle_bin.setIconSize(QtCore.QSize(16,16))
		self.button_recycle_bin.setFixedHeight(32)
		self.button_recycle_bin.setFlat(True)
		self.button_recycle_bin.setCheckable(True)
		self.button_recycle_bin.setFocusPolicy(QtCore.Qt.NoFocus)

		layout_can=QtGui.QVBoxLayout()
		layout_can.addWidget(self.button_safe_box)
		layout_can.addWidget(self.button_recycle_bin)
		layout_can.setContentsMargins(0,4,0,4)
		layout_can.setSpacing(1)
		group_can.setLayout(layout_can)

		self.button_history=QtGui.QPushButton()
		self.button_history.setObjectName('DiskListWidget_PushButton')
		self.button_history.setObjectName('DiskListWidget_PushButton')
		self.button_history.setIcon(QtGui.QIcon(':/all_files_16.png'))
		self.button_history.setIconSize(QtCore.QSize(16,16))
		self.button_history.setFixedHeight(32)
		self.button_history.setFlat(True)
		self.button_history.setCheckable(True)
		self.button_history.setFocusPolicy(QtCore.Qt.NoFocus)

		layout_history=QtGui.QVBoxLayout()
		layout_history.addWidget(self.button_history)
		layout_history.setContentsMargins(0,4,0,0)
		layout_history.setSpacing(1)
		group_history.setLayout(layout_history)

		layout_main=QtGui.QVBoxLayout()
		layout_main.addWidget(group_all_files)
		layout_main.addWidget(group_my_shared)
		layout_main.addWidget(group_can)
		layout_main.addWidget(group_history)
		layout_main.addStretch()
		layout_main.setContentsMargins(0,0,0,0)
		layout_main.setSpacing(1)
		self.setLayout(layout_main)
		self.setFixedWidth(160)


	def init_connect(self):
		pass
