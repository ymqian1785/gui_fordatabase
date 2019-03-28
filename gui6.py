# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui6.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread,QDateTime
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import (QGraphicsView,QGraphicsScene,QApplication,QGraphicsPixmapItem)
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import cx_Oracle
import os,cv2
import csv
import sys
import time
import math
from datetime import datetime
import os
import xlsxwriter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        self.conn = cx_Oracle.connect('TJOCR/TJOCR@127.0.0.1/orcl')
        # self.conn= cx_Oracle.connect('airport/jcfj2017@10.92.172.110:1521/orcl')
        # self.conn = cx_Oracle.connect('airport','jcfj2017','10.92.172.110:1521/orcl')
        self.cursor = self.conn.cursor()
        self.sqlstring = "select * from PSG_AJ_OCR where"
        self.sqlstring1 = "select * from（select * from PSG_AJ_ZC order by ID desc）where rownum=1 AND"


        MainWindow.resize(856, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        stylesheet = """ 
                        QTabBar::tab:selected {background: gray;}
                        QTabWidget>QWidget>QWidget{background: gray;}
                       """
        self.setStyleSheet(stylesheet)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_6.addWidget(self.lineEdit_23, 0, 2, 1, 2)
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_7)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 5, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 7, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 8, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_6.addWidget(self.lineEdit_26, 3, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_7)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_7)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_7)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 2, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_6.addWidget(self.lineEdit_25, 2, 3, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_6.addWidget(self.lineEdit_24, 1, 3, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_6.addWidget(self.lineEdit_28, 5, 3, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_6.addWidget(self.lineEdit_29, 6, 3, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_6.addWidget(self.lineEdit_30, 7, 3, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_6.addWidget(self.lineEdit_31, 8, 3, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_6.addWidget(self.lineEdit_27, 4, 3, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_8.addWidget(self.lineEdit_32, 0, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_8.addWidget(self.lineEdit_33, 1, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_8.addWidget(self.lineEdit_35, 3, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_8.addWidget(self.lineEdit_34, 2, 1, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_8.addWidget(self.lineEdit_36, 4, 1, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_8.addWidget(self.lineEdit_37, 5, 1, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_8.addWidget(self.lineEdit_39, 7, 1, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_8.addWidget(self.lineEdit_40, 8, 1, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_8.addWidget(self.lineEdit_38, 6, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_8)
        self.label_30.setObjectName("label_30")
        self.gridLayout_8.addWidget(self.label_30, 3, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_8)
        self.label_39.setObjectName("label_39")
        self.gridLayout_8.addWidget(self.label_39, 2, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_8)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_8)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 1, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_8)
        self.label_31.setObjectName("label_31")
        self.gridLayout_8.addWidget(self.label_31, 4, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_8)
        self.label_32.setObjectName("label_32")
        self.gridLayout_8.addWidget(self.label_32, 5, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_8)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 8, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_8)
        self.label_33.setObjectName("label_33")
        self.gridLayout_8.addWidget(self.label_33, 6, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_8)
        self.label_34.setObjectName("label_34")
        self.gridLayout_8.addWidget(self.label_34, 7, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        stylesheet = """ 
                         QTabBar::tab:selected {background: gray;}
                         QTabWidget>QWidget>QWidget{background: gray;}
                        """
        self.tab_2.setStyleSheet(stylesheet)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_3.addWidget(self.lineEdit_22, 0, 1, 1, 3)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 4, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")


        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit_2.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout_5.addWidget(self.dateTimeEdit_2, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.dateTimeEdit.setDateTime(QDateTime.fromString(self.now_time, 'yyyy-MM-dd hh:mm:ss'))
        self.gridLayout_5.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(21)
        self.tableWidget.setRowCount(1000000)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        stylesheet = """ 
                        QTabBar::tab:selected {background: gray;}
                        QTabWidget>QWidget>QWidget{background: gray;}
                       """
        self.tab_3.setStyleSheet(stylesheet)
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout_10.addWidget(self.graphicsView_4, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 2, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.gridLayout_9.addWidget(self.dateTimeEdit_4, 1, 1, 1, 1)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.gridLayout_9.addWidget(self.dateTimeEdit_3, 0, 1, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_9.addWidget(self.checkBox_11, 0, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_9.addWidget(self.lineEdit_20, 2, 1, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_9.addWidget(self.lineEdit_41, 2, 0, 1, 1)
        self.gridLayout_9.setColumnStretch(0, 2)
        self.gridLayout_9.setColumnStretch(1, 2)
        self.gridLayout_12.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 1, 1, 1)
        self.gridLayout_12.setColumnStretch(0, 3)
        self.gridLayout_12.setColumnStretch(1, 1)
        self.gridLayout_12.setRowStretch(0, 1)
        self.gridLayout_12.setRowStretch(1, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "机场公安分局安检信息数据库查询系统"))
        self.groupBox_7.setTitle(_translate("MainWindow", "表一"))
        self.label_25.setText(_translate("MainWindow", "出生日期"))
        self.label_26.setText(_translate("MainWindow", "入库时间"))
        self.label_27.setText(_translate("MainWindow", "证件类型"))
        self.label_28.setText(_translate("MainWindow", "旅客编号"))
        self.label_29.setText(_translate("MainWindow", "机器号"))
        self.label_21.setText(_translate("MainWindow", "识别证件号"))
        self.label_36.setText(_translate("MainWindow", "英文名"))
        self.label_22.setText(_translate("MainWindow", "姓名"))
        self.label_24.setText(_translate("MainWindow", "性别"))
        self.groupBox_8.setTitle(_translate("MainWindow", "表二"))
        self.label_30.setText(_translate("MainWindow", "行李数"))
        self.label_39.setText(_translate("MainWindow", "座位号"))
        self.label_37.setText(_translate("MainWindow", "订票证件号"))
        self.label_38.setText(_translate("MainWindow", "航班号"))
        self.label_31.setText(_translate("MainWindow", "陪人数"))
        self.label_32.setText(_translate("MainWindow", "登机号"))
        self.label_35.setText(_translate("MainWindow", "起飞时间"))
        self.label_33.setText(_translate("MainWindow", "登机口"))
        self.label_34.setText(_translate("MainWindow", "起飞日期"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "实时进港旅客"))
        self.label_20.setText(_translate("MainWindow", "旅客检索"))
        self.pushButton_7.setText(_translate("MainWindow", "检索"))
        self.checkBox_3.setText(_translate("MainWindow", "证件号"))
        self.checkBox_4.setText(_translate("MainWindow", "姓名"))
        self.checkBox_5.setText(_translate("MainWindow", "英文名"))
        self.checkBox.setText(_translate("MainWindow", "入库时间"))
        self.label_23.setText(_translate("MainWindow", "查询条件"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "旅客编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "证件缩略图地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "证件人像切图"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "识别证件号"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "民族"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "出生日期"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "住址"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "出生地"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "有效期至"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "英文名"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "MRZZ"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "国籍"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "入客户端时间"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "null"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "证件类型"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "证件有效期开始"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "证件有效期结束"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "null"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查询系统"))
        self.checkBox_11.setText(_translate("MainWindow", "CheckBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "模式分析"))


    def keyPressEvent(self, e):  # 不懂这个函数用在哪里？
        # 重写控件centralwidget的键盘按下事件
        if e.key() == QtCore.Qt.Key_Escape:
            # 如果按下了ESC键则执行buttonExit函数
            self.buttonExit()

    def buttonExit(self):
        self.cursor.close()
        self.conn.close()
        self.close()

    def buttonsearch(self):
        self.tableWidget.clearContents()
        temp_sqlstring = self.sqlstring
        is_first = True

        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " IDCARD='%s'" % self.lineEdit_22.text()
            else:
                temp_sqlstring += " and IDCARD='%s'" % self.lineEdit_22.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " NAME='%s'" % self.lineEdit_22.text()
            else:
                temp_sqlstring += " and NAME='%s'" % self.lineEdit_22.text()

        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " ENGLISHNAME='%s'" % self.lineEdit_22.text()
            else:
                temp_sqlstring += " and ENGLISHNAME='%s'" % self.lineEdit_22.text()

        if self.checkBox.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            else:
                temp_sqlstring += " and INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')


        if temp_sqlstring =='select * from PSG_AJ_OCR where':
                window = Dialog(self)
                window.show()
        else:
             self.cursor.execute(temp_sqlstring)
             data = self.cursor.fetchall()
             if data:
                 k = 0
                 for i in data:
                    w = 0
                    for j in i:
                        if type(j) == int:
                            newItem = QtWidgets.QTableWidgetItem(str(j))
                        if type(j) == datetime:
                            newItem = QtWidgets.QTableWidgetItem(str(j))
                        else:
                            newItem = QtWidgets.QTableWidgetItem(j)
                        self.tableWidget.setItem(k, w, newItem)
                        w += 1
                    k += 1
                 window = Dialog2(self)
                 window.show()
             else:
                   window = Dialog(self)
                   window.show()


#=================================实时刷新部分====================================
    def buttonstart(self, data):  # 多线程下用每秒发送的data执行的函数
        # ==========================断开数据库======================================
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

        self.cursor.execute(str(data))
        alldata = self.cursor.fetchall()
        temp_sqlstring1 = self.sqlstring1
        for rec in alldata:
            self.lineEdit_23.setText(rec[4])
            self.lineEdit_24.setText(rec[5])
            self.lineEdit_25.setText(rec[6])
            self.lineEdit_26.setText(rec[10])
            self.lineEdit_27.setText(rec[12])
            self.lineEdit_28.setText(str(rec[15]))
            self.lineEdit_29.setText(str(rec[17]))
            temp_sqlstring1 += " PASSENGERNO='%s'" % rec[1]
            # pixmap.load(rec[])
            # scaredPixmap = pixmap.scaled(2000, 430, aspectRatioMode=Qt.KeepAspectRatio)
            # self.scene.items()[0].setPixmap(scaredPixmap)
            # self.graphicsView.setScene(self.scene)

        self.cursor.execute(temp_sqlstring1)
        data1 = self.cursor.fetchall()
        for rec in data1:
            self.lineEdit_30.setText(rec[1])
            self.lineEdit_31.setText(rec[2])
            self.lineEdit_32.setText(rec[4])
            self.lineEdit_33.setText(rec[6])
            self.lineEdit_34.setText(rec[7])
            self.lineEdit_35.setText(str(rec[8]))
            self.lineEdit_36.setText(str(rec[9]))
            self.lineEdit_37.setText(rec[10])
            self.lineEdit_38.setText(rec[11])
            self.lineEdit_39.setText(rec[12])
            self.lineEdit_40.setText((rec[13]))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        #连接按钮与函数
        self.pushButton_7.clicked.connect(self.buttonsearch)
        #实例线程并开始
        self.b = Backend()
        self.b.update_date.connect(self.buttonstart)
        self.b.start()

class Backend(QThread):
    update_date = pyqtSignal(str)
    def run(self):
        while True:
            # data = "select * from PSG_AJ_OCR"
            data = "select * from（select * from PSG_AJ_OCR order by NO desc）where rownum=1"
            self.update_date.emit(data)
            time.sleep(3)

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self._diawidth = 240  # 设置实例成员_diawidth,它的值为300
        self._diaheight = 100
        self.setWindowTitle("提示")  # 设置窗口标题
        self.pwd = QtWidgets.QLabel(self)
        self.pwd.setAlignment(Qt.AlignJustify)  # 设置QLabel居中显示
        self.pwd.setText(u'查询为空')

class Dialog2(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self._diawidth = 240  # 设置实例成员_diawidth,它的值为300
        self._diaheight = 100
        self.setWindowTitle("提示")  # 设置窗口标题
        self.pwd = QtWidgets.QLabel(self)
        self.pwd.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示
        self.pwd.setText(u'查询结果已出')

#=========================================登入界面的输入账号和密码窗口定义===============================================
class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('天津')
        self.user = QtWidgets.QLineEdit(self)
        self.user.move(10, 20)
        self.user.setText('')
        self.pwd = QtWidgets.QLineEdit(self)
        self.pwd.move(10, 60)
        self.pwd.setText("")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginBtn = QtWidgets.QPushButton('Login', self)
        self.loginBtn.move(100, 90)
        self.loginBtn.clicked.connect(self.login)  # 绑定方法判断用户名和密码

    def login(self):
        if self.user.text() == 'admin' and self.pwd.text() == '123456':
            # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', 'User name or password error')

#主程序开始部分
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 建立一个app，把框架放在这个app中执行
    app.aboutToQuit.connect(app.deleteLater)
    pixmap = QtGui.QPixmap()
    dialog = LoginDialog()
    if dialog.exec_():
        myshow = MyWindow()
        myshow.setStyleSheet("#MainWindow{border-image:url(./timg.jpg);}")
        myshow.show()
        sys.exit(app.exec_())  # 也可以写成app.exec_() sys.exit(0)，前者是循环整个界面，后者是退出app
    myshow = MyWindow()
    myshow.setStyleSheet("#MainWindow{border-image:url(./timg.jpg);}")
    myshow.show()
    sys.exit(app.exec_())