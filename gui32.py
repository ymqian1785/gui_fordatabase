# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


#==========引入的库================
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QDate,QDateTime ,QTime
import MySQLdb
import time
import math
from datetime import datetime
from PyQt4 import QtCore, QtGui
import os,cv2
import shutil


tablename = 'wenzhoutable1'
# listshow = ['XUHAO' , 'MUDIZHAN' ,'ZUOWEIHAO','MINZU','XINGLIXINXI','ZHUZHI','ZHENGJIANXINXI','YOUXIAOQIXIAN','ANJIANSHIJIAN','']

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem()
        self.scene.addItem(item)
        # ============连接数据库=================
        self.conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='zdki',
            db='wenzhou',
            #
            charset='utf8',
        )
        self.cur = self.conn.cursor()
        # ==============查询的表名===============
        self.sqlstring = "select * from " + tablename + " where "

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1271, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 961, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget_6 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 911, 231))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_65 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.gridLayout_6.addWidget(self.label_65, 3, 0, 1, 1)
        self.lineEdit_74 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_74.setObjectName(_fromUtf8("lineEdit_74"))
        self.gridLayout_6.addWidget(self.lineEdit_74, 2, 1, 1, 1)
        self.lineEdit_75 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_75.setObjectName(_fromUtf8("lineEdit_75"))
        self.gridLayout_6.addWidget(self.lineEdit_75, 0, 1, 1, 1)
        self.label_67 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.gridLayout_6.addWidget(self.label_67, 1, 0, 1, 1)
        self.label_79 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.gridLayout_6.addWidget(self.label_79, 0, 0, 1, 1)
        self.lineEdit_76 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_76.setObjectName(_fromUtf8("lineEdit_76"))
        self.gridLayout_6.addWidget(self.lineEdit_76, 1, 1, 1, 1)
        self.label_82 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.gridLayout_6.addWidget(self.label_82, 2, 0, 1, 1)
        self.label_83 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.gridLayout_6.addWidget(self.label_83, 4, 2, 1, 1)
        self.label_84 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_84.setObjectName(_fromUtf8("label_84"))
        self.gridLayout_6.addWidget(self.label_84, 5, 0, 1, 1)
        self.lineEdit_77 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_77.setObjectName(_fromUtf8("lineEdit_77"))
        self.gridLayout_6.addWidget(self.lineEdit_77, 5, 1, 1, 1)
        self.lineEdit_78 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_78.setObjectName(_fromUtf8("lineEdit_78"))
        self.gridLayout_6.addWidget(self.lineEdit_78, 0, 3, 1, 1)
        self.lineEdit_79 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_79.setObjectName(_fromUtf8("lineEdit_79"))
        self.gridLayout_6.addWidget(self.lineEdit_79, 3, 1, 1, 1)
        self.label_85 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_85.setObjectName(_fromUtf8("label_85"))
        self.gridLayout_6.addWidget(self.label_85, 3, 2, 1, 1)
        self.label_86 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_86.setObjectName(_fromUtf8("label_86"))
        self.gridLayout_6.addWidget(self.label_86, 4, 0, 1, 1)
        self.label_87 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_87.setObjectName(_fromUtf8("label_87"))
        self.gridLayout_6.addWidget(self.label_87, 0, 2, 1, 1)
        self.label_88 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_88.setObjectName(_fromUtf8("label_88"))
        self.gridLayout_6.addWidget(self.label_88, 6, 2, 1, 1)
        self.lineEdit_80 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_80.setObjectName(_fromUtf8("lineEdit_80"))
        self.gridLayout_6.addWidget(self.lineEdit_80, 4, 1, 1, 1)
        self.lineEdit_81 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_81.setObjectName(_fromUtf8("lineEdit_81"))
        self.gridLayout_6.addWidget(self.lineEdit_81, 1, 3, 1, 1)
        self.label_89 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_89.setObjectName(_fromUtf8("label_89"))
        self.gridLayout_6.addWidget(self.label_89, 5, 2, 1, 1)
        self.label_90 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.gridLayout_6.addWidget(self.label_90, 8, 2, 1, 1)
        self.lineEdit_82 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_82.setObjectName(_fromUtf8("lineEdit_82"))
        self.gridLayout_6.addWidget(self.lineEdit_82, 4, 3, 1, 1)
        self.lineEdit_83 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_83.setObjectName(_fromUtf8("lineEdit_83"))
        self.gridLayout_6.addWidget(self.lineEdit_83, 5, 3, 1, 1)
        self.lineEdit_84 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_84.setObjectName(_fromUtf8("lineEdit_84"))
        self.gridLayout_6.addWidget(self.lineEdit_84, 7, 1, 1, 1)
        self.lineEdit_85 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_85.setObjectName(_fromUtf8("lineEdit_85"))
        self.gridLayout_6.addWidget(self.lineEdit_85, 8, 1, 1, 1)
        self.lineEdit_86 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_86.setObjectName(_fromUtf8("lineEdit_86"))
        self.gridLayout_6.addWidget(self.lineEdit_86, 3, 3, 1, 1)
        self.label_91 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.gridLayout_6.addWidget(self.label_91, 6, 0, 1, 1)
        self.lineEdit_87 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_87.setObjectName(_fromUtf8("lineEdit_87"))
        self.gridLayout_6.addWidget(self.lineEdit_87, 7, 3, 1, 1)
        self.label_92 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_92.setObjectName(_fromUtf8("label_92"))
        self.gridLayout_6.addWidget(self.label_92, 8, 0, 1, 1)
        self.label_93 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_93.setObjectName(_fromUtf8("label_93"))
        self.gridLayout_6.addWidget(self.label_93, 7, 0, 1, 1)
        self.lineEdit_88 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_88.setObjectName(_fromUtf8("lineEdit_88"))
        self.gridLayout_6.addWidget(self.lineEdit_88, 2, 3, 1, 1)
        self.label_94 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_94.setObjectName(_fromUtf8("label_94"))
        self.gridLayout_6.addWidget(self.label_94, 7, 2, 1, 1)
        self.lineEdit_89 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_89.setObjectName(_fromUtf8("lineEdit_89"))
        self.gridLayout_6.addWidget(self.lineEdit_89, 6, 1, 1, 1)
        self.label_95 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_95.setObjectName(_fromUtf8("label_95"))
        self.gridLayout_6.addWidget(self.label_95, 4, 4, 1, 1)
        self.label_96 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_96.setObjectName(_fromUtf8("label_96"))
        self.gridLayout_6.addWidget(self.label_96, 1, 4, 1, 1)
        self.lineEdit_90 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_90.setObjectName(_fromUtf8("lineEdit_90"))
        self.gridLayout_6.addWidget(self.lineEdit_90, 6, 3, 1, 1)
        self.label_97 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_97.setObjectName(_fromUtf8("label_97"))
        self.gridLayout_6.addWidget(self.label_97, 0, 4, 1, 1)
        self.lineEdit_91 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_91.setObjectName(_fromUtf8("lineEdit_91"))
        self.gridLayout_6.addWidget(self.lineEdit_91, 8, 3, 1, 1)
        self.label_98 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_98.setObjectName(_fromUtf8("label_98"))
        self.gridLayout_6.addWidget(self.label_98, 3, 4, 1, 1)
        self.lineEdit_92 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_92.setObjectName(_fromUtf8("lineEdit_92"))
        self.gridLayout_6.addWidget(self.lineEdit_92, 0, 5, 1, 1)
        self.lineEdit_93 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_93.setObjectName(_fromUtf8("lineEdit_93"))
        self.gridLayout_6.addWidget(self.lineEdit_93, 1, 5, 1, 1)
        self.lineEdit_94 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_94.setObjectName(_fromUtf8("lineEdit_94"))
        self.gridLayout_6.addWidget(self.lineEdit_94, 2, 5, 1, 1)
        self.lineEdit_95 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_95.setObjectName(_fromUtf8("lineEdit_95"))
        self.gridLayout_6.addWidget(self.lineEdit_95, 3, 5, 1, 1)
        self.lineEdit_96 = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_96.setObjectName(_fromUtf8("lineEdit_96"))
        self.gridLayout_6.addWidget(self.lineEdit_96, 4, 5, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.label, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 2, 4, 1, 1)
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(70, 250, 551, 161))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 30, 59, 16))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.lineEdit_52 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_52.setGeometry(QtCore.QRect(90, 30, 131, 20))
        self.lineEdit_52.setObjectName(_fromUtf8("lineEdit_52"))
        self.label_60 = QtGui.QLabel(self.tab_2)
        self.label_60.setGeometry(QtCore.QRect(20, 60, 48, 20))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.lineEdit_53 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_53.setGeometry(QtCore.QRect(90, 60, 131, 20))
        self.lineEdit_53.setObjectName(_fromUtf8("lineEdit_53"))
        self.label_62 = QtGui.QLabel(self.tab_2)
        self.label_62.setGeometry(QtCore.QRect(20, 100, 48, 20))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.lineEdit_51 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_51.setGeometry(QtCore.QRect(90, 100, 131, 20))
        self.lineEdit_51.setObjectName(_fromUtf8("lineEdit_51"))
        self.label_59 = QtGui.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(20, 140, 48, 20))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.lineEdit_56 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_56.setGeometry(QtCore.QRect(90, 140, 131, 20))
        self.lineEdit_56.setObjectName(_fromUtf8("lineEdit_56"))
        self.label_68 = QtGui.QLabel(self.tab_2)
        self.label_68.setGeometry(QtCore.QRect(20, 180, 48, 20))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.lineEdit_57 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_57.setGeometry(QtCore.QRect(90, 180, 131, 20))
        self.lineEdit_57.setObjectName(_fromUtf8("lineEdit_57"))
        self.label_64 = QtGui.QLabel(self.tab_2)
        self.label_64.setGeometry(QtCore.QRect(20, 220, 48, 20))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.lineEdit_54 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_54.setGeometry(QtCore.QRect(90, 220, 131, 20))
        self.lineEdit_54.setObjectName(_fromUtf8("lineEdit_54"))
        self.label_73 = QtGui.QLabel(self.tab_2)
        self.label_73.setGeometry(QtCore.QRect(20, 250, 48, 20))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.lineEdit_66 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_66.setGeometry(QtCore.QRect(90, 250, 131, 20))
        self.lineEdit_66.setObjectName(_fromUtf8("lineEdit_66"))
        self.label_75 = QtGui.QLabel(self.tab_2)
        self.label_75.setGeometry(QtCore.QRect(20, 280, 48, 20))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.lineEdit_61 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_61.setGeometry(QtCore.QRect(90, 280, 131, 20))
        self.lineEdit_61.setObjectName(_fromUtf8("lineEdit_61"))
        self.label_74 = QtGui.QLabel(self.tab_2)
        self.label_74.setGeometry(QtCore.QRect(20, 330, 36, 20))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.lineEdit_62 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_62.setGeometry(QtCore.QRect(90, 320, 131, 20))
        self.lineEdit_62.setObjectName(_fromUtf8("lineEdit_62"))
        self.label_69 = QtGui.QLabel(self.tab_2)
        self.label_69.setGeometry(QtCore.QRect(250, 30, 71, 20))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.lineEdit_55 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_55.setGeometry(QtCore.QRect(320, 30, 121, 20))
        self.lineEdit_55.setObjectName(_fromUtf8("lineEdit_55"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 60, 71, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.lineEdit_58 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_58.setGeometry(QtCore.QRect(320, 60, 121, 20))
        self.lineEdit_58.setObjectName(_fromUtf8("lineEdit_58"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 100, 71, 16))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.lineEdit_65 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_65.setGeometry(QtCore.QRect(320, 100, 121, 20))
        self.lineEdit_65.setObjectName(_fromUtf8("lineEdit_65"))
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(250, 140, 71, 16))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.lineEdit_63 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_63.setGeometry(QtCore.QRect(320, 140, 121, 20))
        self.lineEdit_63.setObjectName(_fromUtf8("lineEdit_63"))
        self.label_63 = QtGui.QLabel(self.tab_2)
        self.label_63.setGeometry(QtCore.QRect(250, 180, 41, 20))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.lineEdit_59 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_59.setGeometry(QtCore.QRect(320, 180, 121, 20))
        self.lineEdit_59.setObjectName(_fromUtf8("lineEdit_59"))
        self.lineEdit_60 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_60.setGeometry(QtCore.QRect(320, 220, 121, 20))
        self.lineEdit_60.setObjectName(_fromUtf8("lineEdit_60"))
        self.label_71 = QtGui.QLabel(self.tab_2)
        self.label_71.setGeometry(QtCore.QRect(250, 220, 31, 20))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.checkBox_5 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_5.setGeometry(QtCore.QRect(250, 250, 71, 16))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.lineEdit_67 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_67.setGeometry(QtCore.QRect(320, 250, 121, 20))
        self.lineEdit_67.setObjectName(_fromUtf8("lineEdit_67"))
        self.label_76 = QtGui.QLabel(self.tab_2)
        self.label_76.setGeometry(QtCore.QRect(250, 280, 48, 20))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.lineEdit_64 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_64.setGeometry(QtCore.QRect(320, 280, 121, 20))
        self.lineEdit_64.setObjectName(_fromUtf8("lineEdit_64"))
        self.label_72 = QtGui.QLabel(self.tab_2)
        self.label_72.setGeometry(QtCore.QRect(250, 320, 24, 20))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.lineEdit_68 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_68.setGeometry(QtCore.QRect(320, 310, 121, 20))
        self.lineEdit_68.setObjectName(_fromUtf8("lineEdit_68"))
        self.label_80 = QtGui.QLabel(self.tab_2)
        self.label_80.setGeometry(QtCore.QRect(450, 30, 59, 20))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.lineEdit_69 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_69.setGeometry(QtCore.QRect(520, 30, 131, 20))
        self.lineEdit_69.setObjectName(_fromUtf8("lineEdit_69"))
        self.label_78 = QtGui.QLabel(self.tab_2)
        self.label_78.setGeometry(QtCore.QRect(450, 60, 59, 20))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.lineEdit_70 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_70.setGeometry(QtCore.QRect(520, 60, 131, 20))
        self.lineEdit_70.setObjectName(_fromUtf8("lineEdit_70"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(450, 100, 59, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.lineEdit_71 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_71.setGeometry(QtCore.QRect(520, 100, 131, 20))
        self.lineEdit_71.setObjectName(_fromUtf8("lineEdit_71"))
        self.label_81 = QtGui.QLabel(self.tab_2)
        self.label_81.setGeometry(QtCore.QRect(450, 130, 59, 20))
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.lineEdit_72 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_72.setGeometry(QtCore.QRect(520, 130, 131, 20))
        self.lineEdit_72.setObjectName(_fromUtf8("lineEdit_72"))
        self.checkBox_7 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_7.setGeometry(QtCore.QRect(450, 170, 59, 16))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.lineEdit_73 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_73.setGeometry(QtCore.QRect(520, 170, 131, 20))
        self.lineEdit_73.setObjectName(_fromUtf8("lineEdit_73"))
        self.graphicsView = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(450, 210, 481, 201))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(670, 30, 121, 161))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(810, 30, 121, 161))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1020, 60, 231, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 2, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem('33.112.19.227')
        self.comboBox.addItem('33.112.19.228')
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit_2.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout.addWidget(self.dateTimeEdit_2, 2, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1010, 40, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1010, 210, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1010, 230, 251, 161))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEdit_24 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.gridLayout_2.addWidget(self.lineEdit_24, 0, 1, 1, 1)
        self.lineEdit_25 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.gridLayout_2.addWidget(self.lineEdit_25, 2, 1, 1, 1)
        self.lineEdit_26 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.gridLayout_2.addWidget(self.lineEdit_26, 3, 1, 1, 1)
        self.lineEdit_27 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.gridLayout_2.addWidget(self.lineEdit_27, 4, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1010, 420, 54, 12))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(1010, 450, 251, 101))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1010, 570, 54, 12))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1010, 600, 131, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_2)
        self.pushButton_7 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout.addWidget(self.pushButton_8)
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(30, 750, 41, 31))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 750, 31, 31))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.setStyleSheet(_fromUtf8("\n"
                                                  "background-color: rgb(255, 0, 0);\n"
                                                  "background-color: rgb(50, 255, 47);"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 490, 961, 251))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(24)
        self.tableWidget.setRowCount(100000)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1271, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_65.setText(_translate("MainWindow", "行李信息", None))
        self.label_67.setText(_translate("MainWindow", "座位号", None))
        self.label_79.setText(_translate("MainWindow", "目的站", None))
        self.label_82.setText(_translate("MainWindow", "民族国籍", None))
        self.label_83.setText(_translate("MainWindow", "生日", None))
        self.label_84.setText(_translate("MainWindow", "证件信息", None))
        self.label_85.setText(_translate("MainWindow", "证件号码", None))
        self.label_86.setText(_translate("MainWindow", "住址", None))
        self.label_87.setText(_translate("MainWindow", "起飞时间", None))
        self.label_88.setText(_translate("MainWindow", "拼音姓名", None))
        self.label_89.setText(_translate("MainWindow", "序号", None))
        self.label_90.setText(_translate("MainWindow", "性别", None))
        self.label_91.setText(_translate("MainWindow", "有效期限", None))
        self.label_92.setText(_translate("MainWindow", "登机口", None))
        self.label_93.setText(_translate("MainWindow", "安检信息", None))
        self.label_94.setText(_translate("MainWindow", "航班日期", None))
        self.label_95.setText(_translate("MainWindow", "始发站", None))
        self.label_96.setText(_translate("MainWindow", "安检时间", None))
        self.label_97.setText(_translate("MainWindow", "签发机关", None))
        self.label_98.setText(_translate("MainWindow", "值机姓名", None))
        self.label.setText(_translate("MainWindow", "证件号", None))
        self.label_2.setText(_translate("MainWindow", "航班号", None))
        self.label_3.setText(_translate("MainWindow", "姓名", None))
        self.label_4.setText(_translate("MainWindow", "实时图片", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "实时", None))
        self.checkBox_6.setText(_translate("MainWindow", "目的站", None))
        self.label_60.setText(_translate("MainWindow", "座位号", None))
        self.label_62.setText(_translate("MainWindow", "民族国籍", None))
        self.label_59.setText(_translate("MainWindow", "行李信息", None))
        self.label_68.setText(_translate("MainWindow", "住址", None))
        self.label_64.setText(_translate("MainWindow", "证件信息", None))
        self.label_73.setText(_translate("MainWindow", "有效期限", None))
        self.label_75.setText(_translate("MainWindow", "安检信息", None))
        self.label_74.setText(_translate("MainWindow", "登机口", None))
        self.label_69.setText(_translate("MainWindow", "起飞时间", None))
        self.checkBox_3.setText(_translate("MainWindow", "证件号", None))
        self.checkBox_4.setText(_translate("MainWindow", "航班号", None))
        self.checkBox_8.setText(_translate("MainWindow", "证件号码", None))
        self.label_63.setText(_translate("MainWindow", "生日", None))
        self.label_71.setText(_translate("MainWindow", "序号", None))
        self.checkBox_5.setText(_translate("MainWindow", "拼音姓名", None))
        self.label_76.setText(_translate("MainWindow", "航班日期", None))
        self.label_72.setText(_translate("MainWindow", "性别", None))
        self.label_80.setText(_translate("MainWindow", "签发机关", None))
        self.label_78.setText(_translate("MainWindow", "安检时间", None))
        self.checkBox_2.setText(_translate("MainWindow", "姓名", None))
        self.label_81.setText(_translate("MainWindow", "值机姓名", None))
        self.checkBox_7.setText(_translate("MainWindow", "始发站", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查询", None))
        self.label_10.setText(_translate("MainWindow", "时间段", None))
        self.checkBox.setText(_translate("MainWindow", "柜台", None))
        self.label_11.setText(_translate("MainWindow", "从", None))
        self.label_12.setText(_translate("MainWindow", "到", None))
        self.label_13.setText(_translate("MainWindow", "查询条件", None))
        self.label_14.setText(_translate("MainWindow", "统计人数", None))
        self.label_15.setText(_translate("MainWindow", "男性", None))
        self.label_18.setText(_translate("MainWindow", "总人数", None))
        self.label_17.setText(_translate("MainWindow", "行李", None))
        self.label_16.setText(_translate("MainWindow", "女性", None))
        self.label_19.setText(_translate("MainWindow", "服务端", None))
        self.pushButton_2.setText(_translate("MainWindow", "清空", None))
        self.pushButton_4.setText(_translate("MainWindow", "导出", None))
        self.pushButton_3.setText(_translate("MainWindow", "放大", None))
        self.pushButton.setText(_translate("MainWindow", "查询", None))
        self.pushButton_5.setText(_translate("MainWindow", "启动", None))
        self.pushButton_6.setText(_translate("MainWindow", "退出", None))
        self.label_20.setText(_translate("MainWindow", "客户端", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "17", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "18", None))
        self.pushButton_7.setText(_translate("MainWindow", "启动", None))
        self.pushButton_8.setText(_translate("MainWindow", "断开", None))
        self.label_22.setText(_translate("MainWindow", "状态", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "目的站", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "座位号", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "民族国籍", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "行李信息", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "住址", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "证件信息", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "有效期限", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "安检信息", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "登机口", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "起飞时间", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "证件号", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "证件号码", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "航班号", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "生日", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "序号", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "拼音姓名", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "航班日期", None))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "性别", None))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "签发机关", None))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "安检时间", None))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "姓名", None))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "值机姓名", None))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "始发站", None))

#====================================查询数据导出==============++++++++++++++++++++
    def buttonoutfile(self):
        now = datetime.now()
        a = now.strftime('%Y-%m-%d-%H-%M-%S')
        temp_sqlstring = "SELECT * FROM " + tablename + " where "
        is_first = True
        if self.checkBox_2.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "XINGMING='%s'" % self.lineEdit_71.text()
            else:
                temp_sqlstring += "and XINGMING='%s'" % self.lineEdit_71.text()

        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ZHENGJIANHAO=%s" % self.lineEdit_58.text()
            else:
                temp_sqlstring += "and ZHENGJIANHAO=%s" % self.lineEdit_58.text()



        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "PINYINXINGMING='%s'" % self.lineEdit_67.text()
            else:
                temp_sqlstring += "and PINYINXINGMING='%s'" % self.lineEdit_67.text()



        if self.checkBox_8.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ZHENGJIANHAOMA='%s'" % self.lineEdit_63.text()
            else:
                temp_sqlstring += "and ZHENGJIANHAOMA='%s'" % self.lineEdit_63.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "HANGBANHAO='%s'" % self.lineEdit_65.text()
            else:
                temp_sqlstring += "and HANGBANHAO='%s'" % self.lineEdit_65.text()

        if self.checkBox_7.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "SHIFAZHAN='%s'" % self.lineEdit_73.text()
            else:
                temp_sqlstring += "and SHIFAZHAN='%s'" % self.lineEdit_73.text()

        if self.checkBox_6.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "MUDIZHAN='%s'" % self.lineEdit_52.text()
            else:
                temp_sqlstring += "and MUDIZHAN='%s'" % self.lineEdit_52.text()

        #if self.checkBox_2.isChecked():

        # if self.checkBox.isChecked():
        #     if is_first:
        #         is_first = False
        #         #if self.comboBox.currentText()=='17':
        #             #temp_sqlstring += "IP='33.112.19.227'"
        #         #else:
        #             #temp_sqlstring += "IP='33.112.19.228'"
        #         temp_sqlstring += "IP='%s'" % self.comboBox.currentText()
        #     else:
        #         temp_sqlstring += "and IP='%s'" % self.comboBox.currentText()

        # if is_first:
        #     is_first = False
        #     temp_sqlstring += "DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
        #         'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
        #         'yyyy-MM-dd hh:mm:ss')
        # else:
        #     temp_sqlstring += "and DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
        #         'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
        #         'yyyy-MM-dd hh:mm:ss')

        if not (is_first):
            str1 = " into outfile '/var/lib/mysql-files/fileName.txt' lines terminated by '\r\n'"
            str = temp_sqlstring + str1
            newstr = str.replace("fileName", a)
            self.cur.execute(newstr)



#==================================================退出界面==============================================
    def buttonExit(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()



#===============================================清空查询界面==============================================
    def buttonclean(self):
        self.lineEdit_51.clear()
        self.lineEdit_52.clear()
        self.lineEdit_53.clear()
        self.lineEdit_54.clear()
        self.lineEdit_55.clear()
        self.lineEdit_56.clear()
        self.lineEdit_57.clear()
        self.lineEdit_58.clear()
        self.lineEdit_59.clear()
        self.lineEdit_60.clear()
        self.lineEdit_61.clear()
        self.lineEdit_62.clear()
        self.lineEdit_63.clear()
        self.lineEdit_64.clear()
        self.lineEdit_65.clear()
        self.lineEdit_66.clear()
        self.lineEdit_67.clear()
        self.lineEdit_68.clear()
        self.lineEdit_69.clear()
        self.lineEdit_70.clear()
        self.lineEdit_71.clear()
        self.lineEdit_72.clear()
        self.lineEdit_73.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()
        self.tableWidget.clearContents()

#===============================================ESC退出界面=======================================
    def keyPressEvent(self, e):  # 不懂这个函数用在哪里？
        # 重写控件centralwidget的键盘按下事件
        if e.key() == QtCore.Qt.Key_Escape:
            # 如果按下了ESC键则执行buttonExit函数
            self.buttonExit()



#==============================================查询按钮功能++++++++++++++++++++++++++++++++++++++++
    def buttonTest(self):
        #self.pushButton.setEnabled(False)
        self.tableWidget.clearContents()
        temp_sqlstring = self.sqlstring
        is_first = True
        if self.checkBox_2.isChecked():
            mystr = self.lineEdit_71.text()
            BattleTag_str = unicode(QtCore.QString(mystr)).encode('utf-8')
            if is_first:
                is_first = False
                if BattleTag_str.find('%') == -1:
                    temp_sqlstring += "XINGMING='%s'" % self.lineEdit_71.text()
                else:
                    temp_sqlstring += "XINGMING like '%s'" % self.lineEdit_71.text()
            else:
                if BattleTag_str.find('%') == -1:
                    temp_sqlstring += "and XINGMING='%s'" % self.lineEdit_71.text()
                else:
                    temp_sqlstring += "and XINGMING like '%s'" % self.lineEdit_71.text()

        # if self.checkBox_2.isChecked():
        #     if is_first:
        #         is_first = False
        #         temp_sqlstring += "XINGMING='%s'" % self.lineEdit_71.text()
        #     else:
        #         temp_sqlstring += "and XINGMING='%s'" % self.lineEdit_71.text()


        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ZHENGJIANHAO=%s" % self.lineEdit_58.text()
            else:
                temp_sqlstring += "and ZHENGJIANHAO=%s" % self.lineEdit_58.text()



        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "PINYINXINGMING='%s'" % self.lineEdit_67.text()
            else:
                temp_sqlstring += "and PINYINXINGMING='%s'" % self.lineEdit_67.text()



        if self.checkBox_8.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ZHENGJIANHAOMA='%s'" % self.lineEdit_63.text()
            else:
                temp_sqlstring += "and ZHENGJIANHAOMA='%s'" % self.lineEdit_63.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "HANGBANHAO='%s'" % self.lineEdit_65.text()
            else:
                temp_sqlstring += "and HANGBANHAO='%s'" % self.lineEdit_65.text()

        if self.checkBox_7.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "SHIFAZHAN='%s'" % self.lineEdit_73.text()
            else:
                temp_sqlstring += "and SHIFAZHAN='%s'" % self.lineEdit_73.text()

        if self.checkBox_6.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "MUDIZHAN='%s'" % self.lineEdit_52.text()
            else:
                temp_sqlstring += "and MUDIZHAN='%s'" % self.lineEdit_52.text()

        #if self.checkBox_2.isChecked():

        # if self.checkBox.isChecked():
        #     if is_first:
        #         is_first = False
        #         #if self.comboBox.currentText()=='17':
        #             #temp_sqlstring += "IP='33.112.19.227'"
        #         #else:
        #             #temp_sqlstring += "IP='33.112.19.228'"
        #         temp_sqlstring += "IP='%s'" % self.comboBox.currentText()
        #     else:
        #         temp_sqlstring += "and IP='%s'" % self.comboBox.currentText()

        if is_first:
            is_first = False
            temp_sqlstring += "ANJIANSHIJIAN>='%s'" % self.dateTimeEdit.dateTime().toString(
                'yyyy-MM-dd hh:mm:ss') + "and ANJIANSHIJIAN<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                'yyyy-MM-dd hh:mm:ss')
            print(temp_sqlstring)
        else:
            temp_sqlstring += "and ANJIANSHIJIAN>='%s'" % self.dateTimeEdit.dateTime().toString(
                'yyyy-MM-dd hh:mm:ss') + "and ANJIANSHIJIAN<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                'yyyy-MM-dd hh:mm:ss')


        #===================================列表查询结果列出=================================================
        if not (is_first):
            self.cur.execute(temp_sqlstring)
            alldata = self.cur.fetchall()
            if alldata:
                k = 0
                for i in alldata:
                    w = 0
                    for j in i:
                        if type(j) == long:
                            newItem = QtGui.QTableWidgetItem(str(j))
                        if type(j) == datetime:
                            newItem = QtGui.QTableWidgetItem(str(j))
                        else:
                            newItem = QtGui.QTableWidgetItem(j)
                        self.tableWidget.setItem(k, w, newItem)#这句话！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1
                        w += 1
                    k += 1
                # self.lineEdit_27.setText(str(k))

        #==================================统计结果======================================
        if not (is_first):
            a1 = 0
            a2 = 0
            a3 = 0
            self.cur.execute(temp_sqlstring)
            data1 = self.cur.fetchall()
            for row in data1:
                if row[4] == u'男':
                   a1 += 1
                if row[4] == u'女':
                   a2 += 1
                if row[1] == u'':
                   a3 += 1
                # if rec[28].find(u'异常布控,非正常') == -1:
                # a3 += 0
                # else:
                # a3 += 1
            self.lineEdit_24.setText(str(a1))
            self.lineEdit_25.setText(str(a2))
            self.lineEdit_26.setText(str(a3))

        #==================================最新一个符合查询条件的显示++++++++++++++++++++++++++++
        if not (is_first):
            img = QPixmap('./test_images/qiang/full_20180724213745343.png')
            self.label_200.setPixmap(img)

            #global a
            sql=temp_sqlstring+"order by ID desc limit 1"
            self.cur.execute(sql)
            data = self.cur.fetchall()

            index = self.cur.description
            result = []

            # 如果有数据返回，就循环输出, alldata是有个n维的列表
            if data:
                for rec in data:
                    row = {}
                    for i in range(len(index)):
                        row[index[i][0]] = rec[i]
                        result.append(row)
                # for i in result:
                #     for j in i:
                #         print j,i[j]

                # =============================刷新结果显示在lineedit========================
                for i in result:
                    for j in i:
                        print j,i[j]
                        # print
                        # j, i[j]
                        # print(i),'---------------'
                        # print(j)
                        if j == 'MINZU':
                            self.lineEdit_51.setText(i[j])
                        if j == 'MUDIZHAN':
                            self.lineEdit_52.setText(i[j])
                        if j == 'ZUOWEIHAO':
                            self.lineEdit_53.setText(i[j])
                        if j == 'ZHENGJIANXINXI':
                            self.lineEdit_54.setText(i[j])
                        if j == 'QIFEISHIJIAN':
                            self.lineEdit_55.setText(i[j])
                        if j == 'XINGLIXINXI':
                            self.lineEdit_56.setText(i[j])
                        if j == 'ZHUZHI':
                            self.lineEdit_57.setText(i[j])
                        if j == 'ZHENGJIANHAO':
                            self.lineEdit_58.setText(i[j])
                        if j == 'SHENGRI':
                            self.lineEdit_59.setText(i[j])
                        if j == 'XUHAO':
                            self.lineEdit_60.setText(i[j])
                        if j == 'ANJIANXINXI':
                            self.lineEdit_61.setText(i[j])
                        if j == 'DENGJIKOU':
                            self.lineEdit_62.setText(i[j])
                        if j == 'ZHENGJIANHAOMA':
                            self.lineEdit_63.setText(i[j])
                        if j == 'HANGBANRIQI':
                            self.lineEdit_64.setText(i[j])
                        if j == 'HANGBANHAO':
                            self.lineEdit_65.setText(i[j])
                        if j == 'YOUXIAOQIXIAN':
                            self.lineEdit_66.setText(i[j])
                        if j == 'PINYINXINGMING':
                            self.lineEdit_67.setText(i[j])
                        if j == 'XINGBIE':
                            self.lineEdit_68.setText(i[j])
                        if j == 'QIANFAJIGUAN':
                            self.lineEdit_69.setText(i[j])
                        if j == 'ANJIANSHIJIAN':
                            self.lineEdit_70.setText(i[j])
                        if j == 'XINGMING':
                            self.lineEdit_71.setText(i[j])
                        if j == 'ZHIJIXINGMING':
                            self.lineEdit_72.setText(i[j])
                        if j == 'SHIFAZHAN':
                            self.lineEdit_73.setText(i[j])

            # for rec in data:
            #     self.lineEdit_51.setText(rec[17])
            #     self.lineEdit_52.setText((rec[7]))
            #     self.lineEdit_53.setText((rec[15]))
            #     self.lineEdit_54.setText((rec[9]))
            #     self.lineEdit_55.setText((rec[23]))
            #     self.lineEdit_56.setText((rec[1]))
            #     self.lineEdit_57.setText((rec[16]))
            #     self.lineEdit_58.setText((rec[12]))
            #     self.lineEdit_59.setText((rec[18]))
            #     self.lineEdit_60.setText((rec[22]))
            #     self.lineEdit_61.setText((rec[20]))
            #     self.lineEdit_62.setText((rec[5]))
            #     self.lineEdit_63.setText((rec[14]))
            #     self.lineEdit_64.setText((rec[6]))
            #     self.lineEdit_65.setText((rec[19]))
            #     self.lineEdit_66.setText((rec[13]))
            #     self.lineEdit_67.setText((rec[2]))
            #     self.lineEdit_68.setText((rec[4]))
            #     self.lineEdit_69.setText((rec[21]))
            #     self.lineEdit_70.setText((rec[3]))
            #     self.lineEdit_71.setText((rec[8]))
            #     self.lineEdit_72.setText((rec[10]))
            #     self.lineEdit_73.setText((rec[11]))


                #a = rec[32]
                # #================================图片显示=================================
                # pixmap.load(rec[32])
                # scaredPixmap = pixmap.scaled(760, 500, aspectRatioMode=Qt.KeepAspectRatio)
                # item = QGraphicsPixmapItem(scaredPixmap)
                # self.scene = QGraphicsScene(self)
                # self.scene.addItem(item)
                # self.graphicsView_2.setScene(self.scene)
                #
                # pixmap.load(rec[33])
                # scaredPixmap = pixmap.scaled(200, 120, aspectRatioMode=Qt.KeepAspectRatio)
                # item = QGraphicsPixmapItem(scaredPixmap)
                # self.scene = QGraphicsScene(self)
                # self.scene.addItem(item)
                # self.graphicsView_3.setScene(self.scene)
                #
                # pixmap.load(rec[34])
                # scaredPixmap = pixmap.scaled(200, 120, aspectRatioMode=Qt.KeepAspectRatio)
                # item = QGraphicsPixmapItem(scaredPixmap)
                # self.scene = QGraphicsScene(self)
                # self.scene.addItem(item)
                # self.graphicsView_4.setScene(self.scene)
                # #self.pushButton.setEnabled(True)


#=================================实时刷新部分====================================
    def buttonstart(self, data):  # 多线程下用每秒发送的data执行的函数
         #==========================断开数据库======================================
        #  self.cur.close()
        #  self.conn.close()
        # # #============================连接数据库======================================
        #  self.conn = MySQLdb.connect(
        #      host='localhost',
        #      user='root',
        #      passwd='123456',
        #      db='wenzhou',
        #      #
        #     charset='utf8',
        #  )
        #  self.cur = self.conn.cursor()

         self.cur.execute(str(data))
         alldata = self.cur.fetchall()
         index = self.cur.description
         result = []

        # 如果有数据返回，就循环输出, alldata是有个n维的列表
         if alldata:
            for rec in alldata:
                row = {}
                for i in range(len(index)):
                    row[index[i][0]] = rec[i]
                    result.append(row)
         # for i in result:
         #     for j in i:
         #         print j,i[j]


        #=============================刷新结果显示在lineedit========================
            for i in result:
                for j in i:
                    # print j,i[j]
                    # print(i),'---------------'
                    # print(j)
                    if j == 'MINZU':
                        self.lineEdit_74.setText(i[j])
                    if j == 'MUDIZHAN':
                        self.lineEdit_75.setText(i[j])
                    if j == 'ZUOWEIHAO':
                        self.lineEdit_76.setText(i[j])
                    if j == 'QIFEISHIJIAN':
                        self.lineEdit_78.setText(i[j])
                    if j == 'ZHENGJIANXINXI':
                        self.lineEdit_77.setText(i[j])
                    if j == 'XINGLIXINXI':
                        self.lineEdit_79.setText(i[j])
                    if j == 'ZHUZHI':
                        self.lineEdit_80.setText(i[j])
                    if j == 'ZHENGJIANHAO':
                        self.lineEdit_81.setText(i[j])
                    if j == 'SHENGRI':
                        self.lineEdit_82.setText(i[j])
                    if j == 'XUHAO':
                        self.lineEdit_83.setText(i[j])
                    if j == 'ANJIANXINXI':
                        self.lineEdit_84.setText(i[j])
                    if j == 'DENGJIKOU':
                        self.lineEdit_85.setText(i[j])
                    if j == 'ZHENGJIANHAOMA':
                        self.lineEdit_86.setText(i[j])
                    if j == 'HANGBANRIQI':
                        self.lineEdit_87.setText(i[j])
                    if j == 'HANGBANHAO':
                        self.lineEdit_88.setText(i[j])
                    if j == 'YOUXIAOQIXIAN':
                        self.lineEdit_89.setText(i[j])
                    if j == 'PINYINXINGMING':
                        self.lineEdit_90.setText(i[j])
                    if j == 'XINGBIE':
                        self.lineEdit_91.setText(i[j])
                    if j == 'QIANFAJIGUAN':
                        self.lineEdit_92.setText(i[j])
                    if j == 'ANJIANSHIJIAN':
                        self.lineEdit_93.setText(i[j])
                    if j == 'XINGMING':
                        self.lineEdit_94.setText(i[j])
                    if j == 'ZHIJIXINGMING':
                        self.lineEdit_95.setText(i[j])
                    if j == 'SHIFAZHAN':
                        self.lineEdit_96.setText(i[j])


            # #=============================实时界面图片加载===============================
            #
            #     pixmap.load(rec[32])
            #     scaredPixmap = pixmap.scaled(2000, 430, aspectRatioMode=Qt.KeepAspectRatio)
            #     self.scene.items()[0].setPixmap(scaredPixmap)
            #     self.graphicsView.setScene(self.scene)


    #=========================================后端程序是否运行显示颜色变化========================
    def buttoncolor(self, pf):
        pf1 = str(pf)
        os.system(" ps -ef|grep run_keras_server.py|grep -v grep >%s" % pf1)
        if (os.path.getsize(pf1)):
            self.pushButton_7.setStyleSheet("background-color: green")
        else:
            self.pushButton_7.setStyleSheet("background-color: red")



#=========================================前面发送端工控机的连接==========================
    def buttonconnect(self):
        if self.comboBox_2.currentText() == '17':
            #  把按钮禁用掉
            # self.pushButton_11.setDisabled(True)
            #  连接子进程的信号和槽函数
            # self.bwThread.finishSignal.connect(self.BigWorkEnd)
            #  开始执行 run() 函数里的内容
            # self.bwThread.start()
            self.readThread.start()
            window = Dialog2(self)
            window.show()
        if self.comboBox_2.currentText() == '18':
            self.readThread2.start()
            window = Dialog2(self)
            window.show()



#======================================按钮有延时停用状态（与前面的BigWorkEnd对应）================================
    # def BigWorkEnd(self, ls):
    #     print 'get!'
    #     # 使用传回的返回值
    #     for word in ls:
    #         print word,
    #     # 恢复按钮
    #     self.pushButton_11.setDisabled(False)


#========================================发送端断开连接==========================================================
    def buttonunconnect(self):
        if self.comboBox_2.currentText() == '17':
              cmd = "/home/fj/linux-pyqt4/unconnect227.sh"
              data = os.popen(cmd)
              print data.read()
              window = Dialog3(self)
              window.show()
        if self.comboBox_2.currentText() == '18':
              cmd1 = "/home/fj/linux-pyqt4/unconnect228.sh"
              data = os.popen(cmd1)
              print data.read()
              window = Dialog3(self)
              window.show()



#=========================================启动后台识别程序====================================================
    def buttonrestart(self):
        self.readThread3.start()



#=======================================放大查询得到的图片===================================================
    def buttonunshowpic(self):
        window=Dialog(self)
        window.show()



#======================================== 用Backend(Qthread)定时发送data======================================
class Backend(QThread):
    update_date = pyqtSignal(str)
    def run(self):
        while True:
            # pass
            data = "select * from " + tablename + " order by ID desc limit 1"
            self.update_date.emit(data)
            time.sleep(3)

# ==========================================用Thread(Qthread)定时发送pf=====================================
class Thread(QThread):
    finished_signal = pyqtSignal(str)
    def run(self):
        while True:
            pf = "/home/lyp/run_keras_server.lock"
            self.finished_signal.emit(pf)
            time.sleep(3)


#=========================================在class定义了连接的shell脚本的操作==================================
# class BigWorkThread(QThread):
#     finishSignal = pyqtSignal(list)
#     def __init__(self, t):
#         super(BigWorkThread, self).__init__()
#         self.t=t
#     def run(self):
#         cmd = "/home/fj/linux-pyqt4/connect227.sh"
#         print("111")
#         data = os.popen(cmd)
#         print data.read()
#         time.sleep(self.t)
#         self.finishSignal.emit(['hello'])
class ReadThread(QThread):
    readOk=pyqtSignal(bool)
    def __init__(self):
        super(ReadThread, self).__init__()
    # 重写 run() 函数，在里面干大事。
    def run(self):
        # 大事
        cmd = "/home/fj/linux-pyqt4/connect227.sh"
        data = os.popen(cmd)
        print data.read()


#=======================================在class定义了连接的shell脚本的操作======================================
class ReadThread2(QThread):
    readOk=pyqtSignal(bool)
    def __init__(self):
        super(ReadThread2, self).__init__()
    # 重写 run() 函数，在里面干大事。
    def run(self):
        # 大事
        cmd = "/home/fj/linux-pyqt4/connect228.sh"
        data = os.popen(cmd)
        print data.read()


#======================================在类里定义执行后台文字识别程序（执行shell脚本）的操作=============================
class ReadThread3(QThread):
    readOk=pyqtSignal(bool)
    def __init__(self):
        super(ReadThread3, self).__init__()
    # 重写 run() 函数，在里面干大事。
    def run(self):
        # 大事
        cmd = "./run.sh"
        data = os.popen(cmd)
        print data.read()
        #execfile('/home/lyp/ocr-v2.2.0/run_keras_server.py')


# ===================================PyQt生产的是一个叫做Ui_MainWindow的类，只需要放在一个框架下画出来即可===================
class MyWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.readThread3 = ReadThread3()
        #self.bwThread = BigWorkThread(int(1))
        self.readThread2 = ReadThread2()
        self.readThread = ReadThread()
        #==================================按钮和函数连接部分=======================================================
        self.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.buttonExit)
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.buttonTest)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.buttonclean)
        self.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.buttonoutfile)
        self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.buttonrestart)
        self.connect(self.pushButton_7,QtCore.SIGNAL('clicked()'), self.buttonconnect)
        self.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), self.buttonunconnect)
        #self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.buttonunshowpic)


        self.b = Backend()
        self.b.update_date.connect(self.buttonstart)
        self.b.start()
        self.a = Thread()
        self.a.finished_signal.connect(self.buttoncolor)
        self.a.start()


# =========================================弹出查询图片的小窗口定义==================================================
class Dialog(QtGui.QDialog):
     def __init__(self, parent=None):
         QtGui.QDialog.__init__(self, parent)
         self._diawidth = 1450  # 设置实例成员_diawidth,它的值为300
         self._diaheight = 900
         self.setWindowTitle("picture")  # 设置窗口标题
         self.setMinimumHeight(self._diaheight)  # 设置窗口最小的大小
         self.setMinimumWidth(self._diawidth)

         self.label = QtGui.QLabel(self)
         self.label.setPixmap(QPixmap(a))
         self.label.setObjectName(_fromUtf8("label"))
         self.label.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示

# =========================================操作提示小窗口定义==================================================
class Dialog2(QtGui.QDialog):
        def __init__(self, parent=None):
                QtGui.QDialog.__init__(self, parent)
                self._diawidth = 100  # 设置实例成员_diawidth,它的值为300
                self._diaheight = 50
                self.setWindowTitle("Tip")  # 设置窗口标题
                self.pwd = QtGui.QLabel(self)
                self.pwd.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示
                self.pwd.setText(u'创建连接')

# =========================================操作提示小窗口定义==================================================
class Dialog3(QtGui.QDialog):
        def __init__(self, parent=None):
                QtGui.QDialog.__init__(self, parent)
                self._diawidth = 100  # 设置实例成员_diawidth,它的值为300
                self._diaheight = 50
                self.setWindowTitle("Tip")  # 设置窗口标题
                self.pwd = QtGui.QLabel(self)
                self.pwd.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示
                self.pwd.setText(u'断开连接')


#=========================================登入界面的输入账号和密码窗口定义===============================================
class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle('wenzhou')
        self.user = QtGui.QLineEdit(self)
        self.user.move(10, 20)
        self.user.setText('')
        self.pwd = QtGui.QLineEdit(self)
        self.pwd.move(10, 60)
        self.pwd.setText('')
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.loginBtn = QtGui.QPushButton('Login', self)
        self.loginBtn.move(100, 90)
        self.loginBtn.clicked.connect(self.login)  # 绑定方法判断用户名和密码

    def login(self):
        if self.user.text() == 'admin' and self.pwd.text() == 'admin':
            # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
            self.accept()
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'User name or password error')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)  # 建立一个app，把框架放在这个app中执行
    app.aboutToQuit.connect(app.deleteLater)
    pixmap = QtGui.QPixmap()
    dialog = LoginDialog()
    if dialog.exec_():
        myshow = MyWindow()
        myshow.show()
        sys.exit(app.exec_())  # 也可以写成app.exec_() sys.exit(0)，前者是循环整个界面，后者是退出app
