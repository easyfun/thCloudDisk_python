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

		current_row_changed=QtCore.pyqtSignal()
	
	def init_data(self):
		pass

	def init_ui(self):
		self.setStyleSheet('''
			QFrame{
				background:white;
				border-right:1px solid #8f8f91;
			}
			QPushButton#DiskListWidget_PushButton{
				border:none;
				text-align:left;
				padding-left: 16px;
				color: black;
			}
			QPushButton#DiskListWidget_PushButton:hover{
				border:none;
				background-color:teal;
				color:white;
			}
			QPushButton#DiskListWidget_PushButton:checked{
				border:none;
				background-color:teal;
				color:white;
			}
			QPushButton#DiskListWidget_PushButton:flat{
				border:none;
			}
			QPushButton#DiskListWidget_PushButton:hover{
				background:teal;
			}


			QPushButton#DiskListWidget_PushButton_2nd{
				border:none;
				text-align:left;
				padding-left: 24px;
				color: black;
			}
			QPushButton#DiskListWidget_PushButton_2nd:hover{
				border:none;
				background-color:teal;
				color:white;
			}
			QPushButton#DiskListWidget_PushButton_2nd:checked{
				border:none;
				background-color:teal;
				color:white;
			}
			QPushButton#DiskListWidget_PushButton_2nd:flat{
				border:none;
			}


			QGroupBox#DiskListWidget_GroupBox_All_Files{
				border:none;
			}
			QGroupBox#DiskListWidget_GroupBox_My_Shared{
				border:none;
				border-top:1px solid #8f8f91;
			}
			QGroupBox#DiskListWidget_GroupBox_Can{
				border:none;
				border-top:1px solid #8f8f91;
			}
			QGroupBox#DiskListWidget_GroupBox_History{
				border:none;
				border-top:1px solid #8f8f91;
			}
			''')

		'''
		dict_groupbox={'group_box_all_files':[0-index,
											1-button_num,
											2-object_name,
											3-object]
		'''
		self.dict_groupbox={
							'groupbox_all_files':[0,5,'DiskListWidget_GroupBox_All_Files'],
							'groupbox_my_shared':[1,1,'DiskListWidget_GroupBox_My_Shared'],
							'groupbox_can':[2,2,'DiskListWidget_GroupBox_Can'],
							'groupbox_history':[3,1,'DiskListWidget_GroupBox_History']
							}
		for value in self.dict_groupbox.values():
			groupbox=QtGui.QGroupBox()
			groupbox.setObjectName(value[2])
			value.append(groupbox)

		'''
		dict_button={'button_all_files':[0-group_box_index,
										1-text,
										2-icon_path,
										3-object_name,
										4-group_box_object,
										5-btn_object]}
		'''

		group_box_object_index=3
		self.dict_button={
			'button_all_files':[0,u'全部文档',':/all_files_16.png',
								'DiskListWidget_PushButton',
								self.dict_groupbox['groupbox_all_files'][group_box_object_index]],
			'button_file':[1,u'文档',':/all_files_16.png',
								'DiskListWidget_PushButton_2nd',
								self.dict_groupbox['groupbox_all_files'][group_box_object_index]],
			'button_music':[2,u'音乐',':/all_files_16.png',
								'DiskListWidget_PushButton_2nd',
								self.dict_groupbox['groupbox_all_files'][group_box_object_index]],
			'button_vedio':[3,u'视频',':/all_files_16.png',
								'DiskListWidget_PushButton_2nd',
								self.dict_groupbox['groupbox_all_files'][group_box_object_index]],
			'button_photo':[4,u'照片',':/all_files_16.png',
								'DiskListWidget_PushButton_2nd',
								self.dict_groupbox['groupbox_all_files'][group_box_object_index]],
			'button_my_shared':[0,u'我的分享',':/all_files_16.png',
								'DiskListWidget_PushButton',
								self.dict_groupbox['groupbox_my_shared'][group_box_object_index]],
			'button_safe_box':[0,u'保险箱',':/all_files_16.png',
								'DiskListWidget_PushButton',
								self.dict_groupbox['groupbox_can'][group_box_object_index]],
			'button_recycle_bin':[1,u'回收站',':/all_files_16.png',
								'DiskListWidget_PushButton',
								self.dict_groupbox['groupbox_can'][group_box_object_index]],
			'button_history':[0,u'操作历史',':/all_files_16.png',
								'DiskListWidget_PushButton',
								self.dict_groupbox['groupbox_history'][group_box_object_index]],
			}

		index=0
		for value in self.dict_button.values():
			button=QtGui.QPushButton(value[1])
			button.setIcon(QtGui.QIcon(value[2]))
			button.setIconSize(QtCore.QSize(16,16))
			button.setFixedHeight(32)
			button.setFlat(True)
			button.setCheckable(True)
			button.setFocusPolicy(QtCore.Qt.NoFocus)
			button.setObjectName(value[3])
			value.append(button)
			value.append(index)
			index+=1

		#print self.dict_groupbox
		#print self.dict_button

		for value in self.dict_groupbox.values():
			layout_group=QtGui.QVBoxLayout()
			index=0
			for count in range(0,value[1]):
				for v in self.dict_button.values():
					if index==v[0] and value[group_box_object_index]==v[4]:
						layout_group.addWidget(v[5])
						index+=1
						break

			layout_group.setContentsMargins(0,2,0,2)
			layout_group.setSpacing(1)
			value[3].setLayout(layout_group)

		layout_main=QtGui.QVBoxLayout()
		for i in range(0,len(self.dict_groupbox)+1):
			for value in self.dict_groupbox.values():
				if i==value[0]:
					layout_main.addWidget(value[group_box_object_index])
					break

		layout_main.addStretch()
		layout_main.setContentsMargins(0,0,0,0)
		layout_main.setSpacing(1)
		self.setLayout(layout_main)

		self.setFixedWidth(160)


	def init_connect(self):
		for value in self.dict_button.values():
			value[5].clicked.connect(self.button_checked_slot)


	def button_checked_slot(self):
		self.sender().setChecked(True)
		for value in self.dict_button.values():
			if value[5] is not self.sender():
				value[5].setChecked(False)
			else:
				current_row_changed.emit()

	'''
	def setButtonChecked(self,buttonName):
		for value in self.dict_button.values():
			if value[5] is not self.sender():
				button.setChecked(False)
	'''