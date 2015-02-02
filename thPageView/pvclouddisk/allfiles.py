#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class AllFiles(QtGui.QFrame):
	def __init__(self,application,parent=None,windowsFlag=QtCore.Qt.Widget):
		super(AllFiles,self).__init__(parent,windowsFlag)
		self.application=application
		self.setObjectName('ViewCloudDiskAllFiles')
		self.initAllFilesData()
		self.initAllFilesUI()
		self.initAllFilesConnect()

	def initAllFilesData(self):
		pass

	def initAllFilesUI(self):

		self.setStyleSheet('''
			QFrame{
				color:black;
			}
			QToolButton{
				color:black;
			}
			''')

		'''
		{'button_id':[0-button_name,1-object_name,2-button_type,3-icon_path,4-object]}
		3-button_type:0-icon,1-icon_text,2-menu
		'''
		self.dict_button={'home_button':[u'','ViewCloudDiskToolButton',0,':/allfiles.home_24.png'],
			'back_button':[u'','ViewCloudDiskToolButton',0,':/allfiles.back_24.png'],
			'forword_button':[u'','ViewCloudDiskToolButton',0,':/allfiles.forword_24.png'],
			'refresh_button':[u'','ViewCloudDiskToolButton',0,':/allfiles.refresh_24.png'],
			'upload_button':[u'上传文件','ViewCloudDiskToolButton',1,':/allfiles.upload_24.png'],
			'new_button':[u'新建','ViewCloudDiskToolButton',1,':/allfiles.new_24.png'],
			'download_button':[u'下载','ViewCloudDiskToolButton',1,':/allfiles.download_24.png'],
			'delete_button':[u'删除','ViewCloudDiskToolButton',1,':/allfiles.delete_24.png'],
			'share_button':[u'分享','ViewCloudDiskToolButton',1,':/allfiles.share_24.png'],
			'sort_button':[u'排序','ViewCloudDiskToolButton',1,':/allfiles.sort_24.png'],
			'view_button':[u'视图','ViewCloudDiskToolButton',1,':/allfiles.view_24.png']
			}

		height=26
		for value in self.dict_button.values():
			button=QtGui.QToolButton()
			button.setObjectName(value[1])
			button.setIcon(QtGui.QIcon(value[3]))
			if 1==value[2]:
				button.setText(value[0])
				button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
				button.setFixedHeight(height)
			else:
				button.setFixedSize(height,height)

			value.append(button)

		self.pathComboBox=QtGui.QComboBox()
		self.pathComboBox.setFixedHeight(height)

		self.searchEdit=QtGui.QLineEdit()
		self.searchEdit.setFixedWidth(200)
		self.searchEdit.setFixedHeight(height)

		topLayout=QtGui.QHBoxLayout()
		topLayout.addWidget(self.dict_button['home_button'][4])
		topLayout.addWidget(self.dict_button['back_button'][4])
		topLayout.addWidget(self.dict_button['forword_button'][4])

		topChildLayout=QtGui.QHBoxLayout()
		topChildLayout.addWidget(self.pathComboBox)
		topChildLayout.addWidget(self.dict_button['refresh_button'][4])
		topChildLayout.setContentsMargins(0,0,0,0)
		topChildLayout.setSpacing(1)
		topLayout.addLayout(topChildLayout)
		topLayout.setStretch(3,1)

		topLayout.addWidget(self.searchEdit)
		topLayout.setContentsMargins(5,2,2,0)

		self.listWidget=QtGui.QListWidget()
		self.listWidget.setObjectName('ViewCloudDiskListWidget')
		self.listWidget.setIconSize(QtCore.QSize(48,48))
		self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
		self.listWidget.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
		self.listWidget.setViewMode(QtGui.QListView.IconMode)
		self.listWidget.setResizeMode(QtGui.QListView.Adjust)


		'''
		itemName=u'上传文件'
		item=QtGui.QListWidgetItem(itemName,self.listWidget)
		item.setIcon(QtGui.QIcon(':/listwidget.upload_48.png'))
		item.setFlags(QtCore.Qt.ItemIsEnabled)
		item.setSizeHint(QtCore.QSize(72,64))
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		'''
		#[type-0文件夹-1文件-2上传,name,full_path,parent_folder]
		self.dict_listwidget_items=[[1,u'我的文件','',''],[0,u'我的文件夹','',''],[2,u'上传文件','','']]
		for index in range(0,len(self.dict_listwidget_items)):
			item=QtGui.QListWidgetItem(self.dict_listwidget_items[index][1],self.listWidget)
			file_type=self.dict_listwidget_items[index][0]
			if 0==file_type:
				item.setIcon(QtGui.QIcon(':/listwidget.folder_48.png'))
				item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)
			elif 1==file_type:
				item.setIcon(QtGui.QIcon(':/listwidget.document_48.png'))
				item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)
			else:
				item.setIcon(QtGui.QIcon(':/listwidget.upload_48.png'))
				item.setFlags(QtCore.Qt.ItemIsEnabled)

			item.setSizeHint(QtCore.QSize(72,64))
			item.setTextAlignment(QtCore.Qt.AlignCenter)

		toolGroup=QtGui.QGroupBox()
		toolGroup.setObjectName('ViewCloudDiskToolGroup')
		toolLayout=QtGui.QHBoxLayout()
		toolLayout.setObjectName('ToolLayout')
		toolLayout.addWidget(self.dict_button['upload_button'][4])
		toolLayout.addWidget(self.dict_button['new_button'][4])
		toolLayout.addWidget(self.dict_button['download_button'][4])
		toolLayout.addWidget(self.dict_button['delete_button'][4])
		toolLayout.addWidget(self.dict_button['share_button'][4])
		toolLayout.addStretch()
		toolLayout.addWidget(self.dict_button['sort_button'][4])
		toolLayout.addWidget(self.dict_button['view_button'][4])
		toolLayout.setContentsMargins(5,2,2,2)
		toolGroup.setLayout(toolLayout)

		mainLayout=QtGui.QVBoxLayout()
		mainLayout.addLayout(topLayout)
		#mainLayout.addLayout(toolLayout)
		mainLayout.addWidget(toolGroup)
		mainLayout.addWidget(self.listWidget)
		#mainLayout.addStretch()
		mainLayout.setContentsMargins(0,0,0,0)
		mainLayout.setSpacing(4)
		self.setLayout(mainLayout)


	def initAllFilesConnect(self):
		pass

	def setToolButtonIcon(self,toolButton,strIcon):
		toolButton.setIcon(QtGui.QIcon(strIcon))
		toolButton.setIconSize(QtCore.QSize(26,26))

	def iconForSymbol(self,name):
		fileName=QtCore.QString("./symbolimage/"+name)
		fileName.toLower()
		fileName.replace(" ","-")
		return QtGui.QIcon(fileName)

