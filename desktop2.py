# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
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
import os
import shutil

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
        #============连接数据库=================
        self.conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='wenzhou',
            #
            charset='utf8',
        )
        self.cur = self.conn.cursor()
        #==============查询的表名===============
        self.sqlstring = "select * from CHECK_IN_INFOR8 where "

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1538, 834)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 1181, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 231, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 70, 231, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 231, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 140, 231, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 170, 231, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 410, 231, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 440, 231, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 480, 231, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 200, 231, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 410, 71, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 81, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 480, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 51, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 300, 54, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(380, 40, 71, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(380, 80, 61, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(380, 120, 54, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(380, 150, 71, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_10 = QtGui.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 300, 231, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_13 = QtGui.QLineEdit(self.tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(470, 40, 181, 20))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.tab)
        self.lineEdit_14.setGeometry(QtCore.QRect(470, 70, 181, 20))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab)
        self.lineEdit_15.setGeometry(QtCore.QRect(470, 110, 181, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(470, 150, 181, 20))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(380, 190, 71, 20))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_19 = QtGui.QLineEdit(self.tab)
        self.lineEdit_19.setGeometry(QtCore.QRect(470, 190, 181, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_26 = QtGui.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(380, 230, 71, 21))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(700, 30, 91, 31))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(700, 70, 71, 21))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(700, 110, 71, 21))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(700, 150, 71, 21))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(700, 190, 71, 31))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(700, 230, 91, 21))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.lineEdit_20 = QtGui.QLineEdit(self.tab)
        self.lineEdit_20.setGeometry(QtCore.QRect(470, 230, 181, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.lineEdit_21 = QtGui.QLineEdit(self.tab)
        self.lineEdit_21.setGeometry(QtCore.QRect(820, 30, 181, 20))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.lineEdit_22 = QtGui.QLineEdit(self.tab)
        self.lineEdit_22.setGeometry(QtCore.QRect(820, 70, 181, 21))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.lineEdit_23 = QtGui.QLineEdit(self.tab)
        self.lineEdit_23.setGeometry(QtCore.QRect(820, 110, 181, 20))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.lineEdit_24 = QtGui.QLineEdit(self.tab)
        self.lineEdit_24.setGeometry(QtCore.QRect(820, 150, 181, 20))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.lineEdit_25 = QtGui.QLineEdit(self.tab)
        self.lineEdit_25.setGeometry(QtCore.QRect(820, 190, 181, 20))
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.lineEdit_26 = QtGui.QLineEdit(self.tab)
        self.lineEdit_26.setGeometry(QtCore.QRect(820, 230, 181, 20))
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(380, 270, 721, 221))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(30, 370, 51, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 370, 231, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 340, 41, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_11 = QtGui.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 340, 231, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_49 = QtGui.QLabel(self.tab)
        self.label_49.setGeometry(QtCore.QRect(30, 240, 72, 15))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_51 = QtGui.QLabel(self.tab)
        self.label_51.setGeometry(QtCore.QRect(30, 270, 72, 15))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.lineEdit_51 = QtGui.QLineEdit(self.tab)
        self.lineEdit_51.setGeometry(QtCore.QRect(120, 240, 231, 21))
        self.lineEdit_51.setObjectName(_fromUtf8("lineEdit_51"))
        self.lineEdit_52 = QtGui.QLineEdit(self.tab)
        self.lineEdit_52.setGeometry(QtCore.QRect(120, 270, 231, 21))
        self.lineEdit_52.setObjectName(_fromUtf8("lineEdit_52"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 70, 71, 21))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 100, 71, 16))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 130, 71, 21))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 160, 71, 21))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.lineEdit_27 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_27.setGeometry(QtCore.QRect(110, 40, 221, 20))
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.lineEdit_28 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_28.setGeometry(QtCore.QRect(110, 70, 221, 20))
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.lineEdit_29 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_29.setGeometry(QtCore.QRect(110, 100, 221, 20))
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.lineEdit_30 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_30.setGeometry(QtCore.QRect(110, 130, 221, 20))
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.lineEdit_31 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_31.setGeometry(QtCore.QRect(110, 160, 221, 20))
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.checkBox_7 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 190, 71, 21))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 230, 71, 16))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.lineEdit_32 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_32.setGeometry(QtCore.QRect(110, 190, 221, 20))
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.lineEdit_33 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_33.setGeometry(QtCore.QRect(110, 230, 221, 20))
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.label_33 = QtGui.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(30, 340, 51, 20))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(30, 380, 61, 21))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(30, 410, 81, 21))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(30, 450, 81, 21))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(30, 480, 81, 21))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.checkBox_9 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_9.setGeometry(QtCore.QRect(370, 80, 91, 16))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_10.setGeometry(QtCore.QRect(370, 110, 91, 16))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.label_38 = QtGui.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(370, 50, 71, 21))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.tab_2)
        self.label_39.setGeometry(QtCore.QRect(370, 150, 71, 16))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.tab_2)
        self.label_40.setGeometry(QtCore.QRect(370, 180, 81, 16))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.tab_2)
        self.label_41.setGeometry(QtCore.QRect(370, 210, 81, 16))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.lineEdit_34 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_34.setGeometry(QtCore.QRect(110, 340, 221, 20))
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.lineEdit_35 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_35.setGeometry(QtCore.QRect(110, 380, 221, 20))
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.lineEdit_36 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_36.setGeometry(QtCore.QRect(110, 410, 221, 20))
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.lineEdit_37 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_37.setGeometry(QtCore.QRect(110, 450, 221, 20))
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.lineEdit_38 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_38.setGeometry(QtCore.QRect(110, 480, 221, 20))
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.lineEdit_39 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_39.setGeometry(QtCore.QRect(450, 50, 121, 20))
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.lineEdit_40 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_40.setGeometry(QtCore.QRect(450, 80, 121, 20))
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.lineEdit_41 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_41.setGeometry(QtCore.QRect(450, 110, 121, 20))
        self.lineEdit_41.setObjectName(_fromUtf8("lineEdit_41"))
        self.lineEdit_42 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_42.setGeometry(QtCore.QRect(450, 140, 121, 20))
        self.lineEdit_42.setObjectName(_fromUtf8("lineEdit_42"))
        self.lineEdit_43 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_43.setGeometry(QtCore.QRect(450, 180, 121, 20))
        self.lineEdit_43.setObjectName(_fromUtf8("lineEdit_43"))
        self.lineEdit_44 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_44.setGeometry(QtCore.QRect(450, 210, 121, 20))
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.label_42 = QtGui.QLabel(self.tab_2)
        self.label_42.setGeometry(QtCore.QRect(600, 50, 71, 16))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.tab_2)
        self.label_43.setGeometry(QtCore.QRect(600, 80, 61, 16))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_44 = QtGui.QLabel(self.tab_2)
        self.label_44.setGeometry(QtCore.QRect(600, 110, 61, 21))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_45 = QtGui.QLabel(self.tab_2)
        self.label_45.setGeometry(QtCore.QRect(600, 140, 61, 21))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.tab_2)
        self.label_46.setGeometry(QtCore.QRect(600, 180, 61, 20))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.label_47 = QtGui.QLabel(self.tab_2)
        self.label_47.setGeometry(QtCore.QRect(600, 210, 81, 21))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(370, 250, 781, 241))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.lineEdit_45 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_45.setGeometry(QtCore.QRect(680, 50, 121, 21))
        self.lineEdit_45.setObjectName(_fromUtf8("lineEdit_45"))
        self.lineEdit_46 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_46.setGeometry(QtCore.QRect(680, 80, 121, 20))
        self.lineEdit_46.setObjectName(_fromUtf8("lineEdit_46"))
        self.lineEdit_47 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_47.setGeometry(QtCore.QRect(680, 110, 121, 20))
        self.lineEdit_47.setObjectName(_fromUtf8("lineEdit_47"))
        self.lineEdit_48 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_48.setGeometry(QtCore.QRect(680, 140, 121, 20))
        self.lineEdit_48.setObjectName(_fromUtf8("lineEdit_48"))
        self.lineEdit_49 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_49.setGeometry(QtCore.QRect(680, 170, 121, 20))
        self.lineEdit_49.setObjectName(_fromUtf8("lineEdit_49"))
        self.lineEdit_50 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_50.setGeometry(QtCore.QRect(680, 210, 121, 20))
        self.lineEdit_50.setObjectName(_fromUtf8("lineEdit_50"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(820, 50, 151, 181))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(1000, 50, 151, 181))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 260, 221, 21))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(110, 300, 221, 21))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.checkBox_12 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_12.setGeometry(QtCore.QRect(30, 260, 71, 19))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_13 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_13.setGeometry(QtCore.QRect(30, 300, 71, 19))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1220, 50, 297, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 2, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 2, 1, 1)
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit_2.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout.addWidget(self.dateTimeEdit_2, 2, 2, 1, 1)
        self.checkBox_11 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout.addWidget(self.checkBox_11, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem('33.112.19.227')
        self.comboBox.addItem('33.112.19.228')
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1220, 10, 71, 31))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1220, 210, 91, 31))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1220, 240, 301, 171))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_23 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_2.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_2.addWidget(self.label_24, 5, 0, 1, 1)
        self.textBrowser_2 = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.gridLayout_2.addWidget(self.textBrowser_2, 2, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.textBrowser_3 = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_2.addWidget(self.textBrowser_3, 4, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.textBrowser_4 = QtGui.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.gridLayout_2.addWidget(self.textBrowser_4, 5, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 560, 1181, 181))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(36)
        self.tableWidget.setRowCount(10000)
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(33, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(34, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(35, item)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1220, 460, 141, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_9 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1380, 460, 141, 141))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.label_50 = QtGui.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(1220, 430, 121, 16))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1220, 640, 141, 128))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem('17')
        self.comboBox_2.addItem('18')
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.label_54 = QtGui.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(1220, 620, 101, 16))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 750, 171, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_48 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.horizontalLayout.addWidget(self.label_48)
        self.pushButton_7 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(50, 255, 47);"))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "姓名", None))
        self.label_2.setText(_translate("MainWindow", "性别", None))
        self.label_3.setText(_translate("MainWindow", "民族", None))
        self.label_4.setText(_translate("MainWindow", "证件号", None))
        self.label_5.setText(_translate("MainWindow", "生日", None))
        self.label_6.setText(_translate("MainWindow", "签发机关", None))
        self.label_7.setText(_translate("MainWindow", "有效日期", None))
        self.label_8.setText(_translate("MainWindow", "家庭住址", None))
        self.label_9.setText(_translate("MainWindow", "name", None))
        self.label_10.setText(_translate("MainWindow", "航班号", None))
        self.label_13.setText(_translate("MainWindow", "航班日期", None))
        self.label_14.setText(_translate("MainWindow", "出发地", None))
        self.label_15.setText(_translate("MainWindow", "目的地", None))
        self.label_16.setText(_translate("MainWindow", "起飞时间", None))
        self.label_25.setText(_translate("MainWindow", "值机信息", None))
        self.label_26.setText(_translate("MainWindow", "行李情况", None))
        self.label_27.setText(_translate("MainWindow", "是否当天航班", None))
        self.label_28.setText(_translate("MainWindow", "证件情况", None))
        self.label_29.setText(_translate("MainWindow", "布控情况", None))
        self.label_30.setText(_translate("MainWindow", "是否特殊", None))
        self.label_31.setText(_translate("MainWindow", "安检情况", None))
        self.label_32.setText(_translate("MainWindow", "隔离区情况", None))
        self.label_12.setText(_translate("MainWindow", "登机口", None))
        self.label_11.setText(_translate("MainWindow", "座位", None))
        self.label_49.setText(_translate("MainWindow", "姓名2", None))
        self.label_51.setText(_translate("MainWindow", "证件2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "实时", None))
        self.checkBox.setText(_translate("MainWindow", "姓名", None))
        self.checkBox_3.setText(_translate("MainWindow", "性别", None))
        self.checkBox_4.setText(_translate("MainWindow", "民族", None))
        self.checkBox_5.setText(_translate("MainWindow", "证件号", None))
        self.checkBox_6.setText(_translate("MainWindow", "生日", None))
        self.checkBox_7.setText(_translate("MainWindow", "name", None))
        self.checkBox_8.setText(_translate("MainWindow", "航班号", None))
        self.label_33.setText(_translate("MainWindow", "座位", None))
        self.label_34.setText(_translate("MainWindow", "登机口", None))
        self.label_35.setText(_translate("MainWindow", "签发机关", None))
        self.label_36.setText(_translate("MainWindow", "有效日期", None))
        self.label_37.setText(_translate("MainWindow", "家庭住址", None))
        self.checkBox_9.setText(_translate("MainWindow", "出发地", None))
        self.checkBox_10.setText(_translate("MainWindow", "目的地", None))
        self.label_38.setText(_translate("MainWindow", "航班日期", None))
        self.label_39.setText(_translate("MainWindow", "起飞时间", None))
        self.label_40.setText(_translate("MainWindow", "值机信息", None))
        self.label_41.setText(_translate("MainWindow", "行李情况", None))
        self.label_42.setText(_translate("MainWindow", "签发地点", None))
        self.label_43.setText(_translate("MainWindow", "证件情况", None))
        self.label_44.setText(_translate("MainWindow", "布控情况", None))
        self.label_45.setText(_translate("MainWindow", "是否特殊", None))
        self.label_46.setText(_translate("MainWindow", "安检情况", None))
        self.label_47.setText(_translate("MainWindow", "隔离区情况", None))
        self.checkBox_12.setText(_translate("MainWindow", "姓名2", None))
        self.checkBox_13.setText(_translate("MainWindow", "证件2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查询", None))
        self.label_18.setText(_translate("MainWindow", "到", None))
        self.checkBox_2.setText(_translate("MainWindow", "时间段", None))
        self.label_17.setText(_translate("MainWindow", "从", None))
        self.checkBox_11.setText(_translate("MainWindow", "柜台", None))
        self.label_19.setText(_translate("MainWindow", "查询条件", None))
        self.label_20.setText(_translate("MainWindow", "查询统计信息", None))
        self.label_23.setText(_translate("MainWindow", "布控人数", None))
        self.label_22.setText(_translate("MainWindow", "女性人数", None))
        self.label_24.setText(_translate("MainWindow", "查询总人数", None))
        self.label_21.setText(_translate("MainWindow", "男性人数", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "安检时间", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "姓名", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "性别", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "国籍", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "民族", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "证件号", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "生日", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "签发机关", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "签发地点", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "有效日期", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "家庭住址", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "name", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "pinyin", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "证件号2", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "航班号", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "航班日期", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "座位号", None))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "登机口", None))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "序号", None))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "出发地", None))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "目的地", None))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "起飞时间", None))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "值机信息", None))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "行李情况", None))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "航班", None))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "证件信息", None))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "布控情况", None))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "是否特殊", None))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("MainWindow", "安检情况", None))
        item = self.tableWidget.horizontalHeaderItem(31)
        item.setText(_translate("MainWindow", "隔离区情况", None))
        item = self.tableWidget.horizontalHeaderItem(32)
        item.setText(_translate("MainWindow", "截屏地址", None))
        item = self.tableWidget.horizontalHeaderItem(33)
        item.setText(_translate("MainWindow", "证件图片", None))
        item = self.tableWidget.horizontalHeaderItem(34)
        item.setText(_translate("MainWindow", "实时图片", None))
        item = self.tableWidget.horizontalHeaderItem(35)
        item.setText(_translate("MainWindow", "IP地址", None))
        self.pushButton.setText(_translate("MainWindow", "查询", None))
        self.pushButton_9.setText(_translate("MainWindow", "放大图片", None))
        self.pushButton_3.setText(_translate("MainWindow", "重启程序", None))
        self.pushButton_4.setText(_translate("MainWindow", "清空", None))
        self.pushButton_2.setText(_translate("MainWindow", "导出查询记录", None))
        self.pushButton_5.setText(_translate("MainWindow", "退出", None))
        self.label_50.setText(_translate("MainWindow", "服务器功能区", None))
        self.pushButton_11.setText(_translate("MainWindow", "连接", None))
        self.pushButton_12.setText(_translate("MainWindow", "断开", None))
        self.label_54.setText(_translate("MainWindow", "发送端功能区", None))
        self.label_48.setText(_translate("MainWindow", "服务器端进程状态", None))

#====================================查询数据导出==============++++++++++++++++++++
    def buttonoutfile(self):
        now = datetime.now()
        a = now.strftime('%Y-%m-%d-%H-%M-%S')
        temp_sqlstring = "SELECT * FROM CHECK_IN_INFOR8 where "
        is_first = True
        if self.checkBox.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "NAME1='%s'" % self.lineEdit_27.text()
            else:
                temp_sqlstring += "and NAME1='%s'" % self.lineEdit_27.text()

        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "SEX='%s'" % self.lineEdit_28.text()
            else:
                temp_sqlstring += "and SEX='%s'" % self.lineEdit_28.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "RACE='%s'" % self.lineEdit_29.text()
            else:
                temp_sqlstring += "and RACE='%s'" % self.lineEdit_29.text()

        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ID_NO=%s" % self.lineEdit_30.text()
            else:
                temp_sqlstring += "and ID_NO=%s" % self.lineEdit_30.text()

        if self.checkBox_6.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "BIRTHDAY='%s'" % self.lineEdit_31.text()
            else:
                temp_sqlstring += "and BIRTHDAY='%s'" % self.lineEdit_31.text()

        if self.checkBox_7.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "NAME2='%s'" % self.lineEdit_32.text()
            else:
                temp_sqlstring += "and NAME2='%s'" % self.lineEdit_32.text()

        if self.checkBox_12.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "NAME3='%s'" % self.lineEdit_17.text()
            else:
                temp_sqlstring += "and NAME3='%s'" % self.lineEdit_17.text()

        if self.checkBox_13.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ID_NO2='%s'" % self.lineEdit_18.text()
            else:
                temp_sqlstring += "and ID_NO2='%s'" % self.lineEdit_18.text()

        if self.checkBox_8.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "FLIGHT_NO='%s'" % self.lineEdit_33.text()
            else:
                temp_sqlstring += "and FLIGHT_NO='%s'" % self.lineEdit_33.text()

        if self.checkBox_9.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DEPT='%s'" % self.lineEdit_40.text()
            else:
                temp_sqlstring += "and DEPT='%s'" % self.lineEdit_40.text()

        if self.checkBox_10.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DEST='%s'" % self.lineEdit_41.text()
            else:
                temp_sqlstring += "and DEST='%s'" % self.lineEdit_41.text()

        if self.checkBox_2.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss')
            else:
                temp_sqlstring += "and DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss')

        if self.checkBox_11.isChecked():
            if is_first:
                is_first = False
                #if self.comboBox.currentText()=='17':
                    #temp_sqlstring += "IP='33.112.19.227'"
                #else:
                    #temp_sqlstring += "IP='33.112.19.228'"
                temp_sqlstring += "IP='%s'" % self.comboBox.currentText()
            else:
                temp_sqlstring += "and IP='%s'" % self.comboBox.currentText()

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
        self.lineEdit_17.clear()
        self.lineEdit_18.clear()
        self.lineEdit_27.clear()
        self.lineEdit_28.clear()
        self.lineEdit_29.clear()
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.lineEdit_34.clear()
        self.lineEdit_35.clear()
        self.lineEdit_36.clear()
        self.lineEdit_37.clear()
        self.lineEdit_38.clear()
        self.lineEdit_39.clear()
        self.lineEdit_40.clear()
        self.lineEdit_41.clear()
        self.lineEdit_42.clear()
        self.lineEdit_43.clear()
        self.lineEdit_44.clear()
        self.lineEdit_45.clear()
        self.lineEdit_46.clear()
        self.lineEdit_47.clear()
        self.lineEdit_48.clear()
        self.lineEdit_49.clear()
        self.lineEdit_50.clear()
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.tableWidget.clearContents()
        self.scene = QGraphicsScene(self)
        self.scene.clear()
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_4.setScene(self.scene)


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
        if self.checkBox.isChecked():
            mystr = self.lineEdit_27.text()
            BattleTag_str = unicode(QtCore.QString(mystr)).encode('utf-8')
            if is_first:
                is_first = False
                if BattleTag_str.find('%') == -1:
                    temp_sqlstring += "NAME1='%s'" % self.lineEdit_27.text()
                else:
                    temp_sqlstring += "NAME1 like '%s'" % self.lineEdit_27.text()
            else:
                if BattleTag_str.find('%') == -1:
                    temp_sqlstring += "and NAME1='%s'" % self.lineEdit_27.text()
                else:
                    temp_sqlstring += "and NAME1 like '%s'" % self.lineEdit_27.text()

        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "SEX='%s'" % self.lineEdit_28.text()
            else:
                temp_sqlstring += "and SEX='%s'" % self.lineEdit_28.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "RACE='%s'" % self.lineEdit_29.text()
            else:
                temp_sqlstring += "and RACE='%s'" % self.lineEdit_29.text()

        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ID_NO=%s" % self.lineEdit_30.text()
            else:
                temp_sqlstring += "and ID_NO=%s" % self.lineEdit_30.text()

        if self.checkBox_6.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "BIRTHDAY='%s'" % self.lineEdit_31.text()
            else:
                temp_sqlstring += "and BIRTHDAY='%s'" % self.lineEdit_31.text()

        if self.checkBox_7.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "NAME2='%s'" % self.lineEdit_32.text()
            else:
                temp_sqlstring += "and NAME3='%s'" % self.lineEdit_32.text()

        if self.checkBox_12.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "NAME3='%s'" % self.lineEdit_17.text()
            else:
                temp_sqlstring += "and NAME2='%s'" % self.lineEdit_17.text()

        if self.checkBox_13.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "ID_NO2='%s'" % self.lineEdit_18.text()
            else:
                temp_sqlstring += "and ID_NO2='%s'" % self.lineEdit_18.text()

        if self.checkBox_8.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "FLIGHT_NO='%s'" % self.lineEdit_33.text()
            else:
                temp_sqlstring += "and FLIGHT_NO='%s'" % self.lineEdit_33.text()

        if self.checkBox_9.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DEPT='%s'" % self.lineEdit_40.text()
            else:
                temp_sqlstring += "and DEPT='%s'" % self.lineEdit_40.text()

        if self.checkBox_10.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DEST='%s'" % self.lineEdit_41.text()
            else:
                temp_sqlstring += "and DEST='%s'" % self.lineEdit_41.text()

        if self.checkBox_2.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss')
            else:
                temp_sqlstring += "and DATE_NOW>='%s'" % self.dateTimeEdit.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss') + "and DATE_NOW<='%s'" % self.dateTimeEdit_2.dateTime().toString(
                    'yyyy-MM-dd hh:mm:ss')

        if self.checkBox_11.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "IP='%s'" % self.comboBox.currentText()
            else:
                temp_sqlstring += "and IP='%s'" % self.comboBox.currentText()

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
                        self.tableWidget.setItem(k, w, newItem)
                        w += 1
                    k += 1
                self.textBrowser_4.setText(str(k))

        #==================================统计结果======================================
        if not (is_first):
            a1 = 0
            a2 = 0
            a3 = 0
            self.cur.execute(temp_sqlstring)
            data1 = self.cur.fetchall()
            for row in data1:
                if row[3] == u'男':
                   a1 += 1
                if row[3] == u'女':
                   a2 += 1
                if row[28] == u'异常布控':
                   a3 += 1
                # if rec[28].find(u'异常布控,非正常') == -1:
                # a3 += 0
                # else:
                # a3 += 1
            self.textBrowser.setText(str(a1))
            self.textBrowser_2.setText(str(a2))
            self.textBrowser_3.setText(str(a3))

        #==================================最新一个符合查询条件的显示++++++++++++++++++++++++++++
        if not (is_first):
            global a
            sql=temp_sqlstring+"order by ID desc limit 1"
            self.cur.execute(sql)
            data = self.cur.fetchall()
            for rec in data:
                self.lineEdit_27.setText(rec[2])
                self.lineEdit_28.setText((rec[3]))
                self.lineEdit_29.setText((rec[5]))
                self.lineEdit_30.setText((rec[6]))
                self.lineEdit_31.setText((rec[7]))
                self.lineEdit_36.setText((rec[8]))
                self.lineEdit_37.setText((rec[10]))
                self.lineEdit_38.setText((rec[11]))
                self.lineEdit_32.setText((rec[12]))
                self.lineEdit_17.setText((rec[13]))
                self.lineEdit_18.setText((rec[14]))
                self.lineEdit_33.setText((rec[15]))
                self.lineEdit_34.setText((rec[17]))
                self.lineEdit_35.setText((rec[18]))
                self.lineEdit_39.setText((rec[16]))
                self.lineEdit_40.setText((rec[20]))
                self.lineEdit_41.setText((rec[21]))
                self.lineEdit_42.setText((rec[22]))
                self.lineEdit_43.setText((rec[23]))
                self.lineEdit_44.setText((rec[24]))
                self.lineEdit_45.setText((rec[25]))
                self.lineEdit_46.setText((rec[27]))
                self.lineEdit_47.setText((rec[28]))
                self.lineEdit_48.setText((rec[29]))
                self.lineEdit_49.setText((rec[30]))
                self.lineEdit_50.setText((rec[31]))
                a = rec[32]
                #================================图片显示=================================
                pixmap.load(rec[32])
                scaredPixmap = pixmap.scaled(760, 500, aspectRatioMode=Qt.KeepAspectRatio)
                item = QGraphicsPixmapItem(scaredPixmap)
                self.scene = QGraphicsScene(self)
                self.scene.addItem(item)
                self.graphicsView_2.setScene(self.scene)

                pixmap.load(rec[33])
                scaredPixmap = pixmap.scaled(200, 120, aspectRatioMode=Qt.KeepAspectRatio)
                item = QGraphicsPixmapItem(scaredPixmap)
                self.scene = QGraphicsScene(self)
                self.scene.addItem(item)
                self.graphicsView_3.setScene(self.scene)

                pixmap.load(rec[34])
                scaredPixmap = pixmap.scaled(200, 120, aspectRatioMode=Qt.KeepAspectRatio)
                item = QGraphicsPixmapItem(scaredPixmap)
                self.scene = QGraphicsScene(self)
                self.scene.addItem(item)
                self.graphicsView_4.setScene(self.scene)
                #self.pushButton.setEnabled(True)






#=================================实时刷新部分====================================
    def buttonstart(self, data):  # 多线程下用每秒发送的data执行的函数
         #==========================断开数据库======================================
         self.cur.close()
         self.conn.close()
        # #============================连接数据库======================================
         self.conn = MySQLdb.connect(
             host='localhost',
             user='root',
             passwd='123456',
             db='wenzhou',
             #
            charset='utf8',
         )
         self.cur = self.conn.cursor()

         self.cur.execute(str(data))
         alldata = self.cur.fetchall()
        # 如果有数据返回，就循环输出, alldata是有个n维的列表
         if alldata:
            for rec in alldata:
        #=============================刷新结果显示在lineedit========================
                self.lineEdit.setText(rec[2])
                self.lineEdit_2.setText((rec[3]))
                self.lineEdit_3.setText((rec[5]))
                self.lineEdit_4.setText((rec[6]))
                self.lineEdit_5.setText((rec[7]))
                self.lineEdit_6.setText((rec[8]))
                self.lineEdit_7.setText((rec[10]))
                self.lineEdit_8.setText((rec[11]))
                self.lineEdit_9.setText((rec[12]))
                self.lineEdit_51.setText((rec[13]))
                self.lineEdit_52.setText((rec[14]))
                self.lineEdit_10.setText((rec[15]))
                self.lineEdit_11.setText((rec[17]))
                self.lineEdit_12.setText((rec[18]))
                self.lineEdit_13.setText((rec[16]))
                self.lineEdit_14.setText((rec[20]))
                self.lineEdit_15.setText((rec[21]))
                self.lineEdit_16.setText((rec[22]))
                self.lineEdit_19.setText((rec[23]))
                self.lineEdit_20.setText((rec[24]))
                self.lineEdit_21.setText((rec[25]))
                self.lineEdit_22.setText((rec[27]))
                self.lineEdit_23.setText((rec[28]))
                self.lineEdit_24.setText((rec[29]))
                self.lineEdit_25.setText((rec[30]))
                self.lineEdit_26.setText((rec[31]))
            #=============================实时界面图片加载===============================

                pixmap.load(rec[32])
                scaredPixmap = pixmap.scaled(2000, 430, aspectRatioMode=Qt.KeepAspectRatio)
                self.scene.items()[0].setPixmap(scaredPixmap)
                self.graphicsView.setScene(self.scene)








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
            data = "select * from CHECK_IN_INFOR8 order by ID desc limit 1"
            self.update_date.emit(data)
            time.sleep(3)



# ==========================================用Thread(Qthread)定时发送pf=====================================
class Thread(QThread):
    finished_signal = pyqtSignal(str)
    def run(self):
        while True:
            pf = "/home/fj/run_keras_server.lock"
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
        cmd = "/home/fj/run.sh"
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
        self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.buttonExit)
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.buttonTest)
        self.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.buttonclean)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.buttonoutfile)
        self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.buttonrestart)
        self.connect(self.pushButton_11,QtCore.SIGNAL('clicked()'), self.buttonconnect)
        self.connect(self.pushButton_12, QtCore.SIGNAL('clicked()'), self.buttonunconnect)
        self.connect(self.pushButton_9, QtCore.SIGNAL('clicked()'), self.buttonunshowpic)

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
                self._diawidth = 60  # 设置实例成员_diawidth,它的值为300
                self._diaheight = 50
                self.setWindowTitle("")  # 设置窗口标题
                self.pwd = QtGui.QLabel(self)
                self.pwd.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示
                self.pwd.setText(u'创建连接')

# =========================================操作提示小窗口定义==================================================
class Dialog3(QtGui.QDialog):
        def __init__(self, parent=None):
                QtGui.QDialog.__init__(self, parent)
                self._diawidth = 60  # 设置实例成员_diawidth,它的值为300
                self._diaheight = 50
                self.setWindowTitle("")  # 设置窗口标题
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

