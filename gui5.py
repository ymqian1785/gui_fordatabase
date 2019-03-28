# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
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

        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem()
        self.scene.addItem(item)

        self.conn = cx_Oracle.connect('TJOCR/TJOCR@127.0.0.1/orcl')
        # conn= cx_Oracle.connect('airport/jcfj@10.92.172.110/orcl')
        self.cursor = self.conn.cursor()
        self.sqlstring = "select * from（select * from PSG_AJ_OCR order by NO desc）where rownum=1 AND"
        self.sqlstring1 = "select * from（select * from PSG_AJ_ZC order by ID desc）where rownum=1 AND"
        self.sqlstring2 = "select * from PSG_AJ_IDCARD_FACE where"

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 574)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 4, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 5, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 5, 3, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_4.addWidget(self.lineEdit_14, 4, 4, 1, 2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 5, 4, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 3, 3, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 3, 4, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 3, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 6, 4, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 6, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 6, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_4.addWidget(self.lineEdit_6, 6, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 7, 3, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 7, 4, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 8, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 8, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 8, 2, 1, 2)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_4.addWidget(self.lineEdit_18, 8, 4, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 9, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_4.addWidget(self.lineEdit_9, 9, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 9, 2, 1, 2)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_4.addWidget(self.lineEdit_19, 9, 4, 1, 2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 10, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 10, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout.addWidget(self.graphicsView_2)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        stylesheet = """ 
                 QTabBar::tab:selected {background: gray;}
                 QTabWidget>QWidget>QWidget{background: gray;}
                """
        self.tab_2.setStyleSheet(stylesheet)
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_6.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_6.addWidget(self.lineEdit_22, 0, 1, 1, 2)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_6.addWidget(self.checkBox_8, 0, 3, 1, 2)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_6.addWidget(self.lineEdit_32, 0, 5, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_6.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_6.addWidget(self.lineEdit_23, 1, 1, 1, 2)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_6.addWidget(self.checkBox_9, 1, 3, 1, 2)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_6.addWidget(self.lineEdit_33, 1, 5, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_6.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_6.addWidget(self.lineEdit_24, 2, 1, 1, 2)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_6.addWidget(self.checkBox_10, 2, 3, 1, 2)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_6.addWidget(self.lineEdit_34, 2, 5, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_6)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 3, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_6.addWidget(self.lineEdit_25, 3, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.groupBox_6)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 3, 3, 1, 2)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_6.addWidget(self.lineEdit_35, 3, 5, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_6.addWidget(self.checkBox_6, 4, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_6.addWidget(self.lineEdit_26, 4, 1, 1, 2)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_6.addWidget(self.lineEdit_36, 4, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 5, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_6.addWidget(self.lineEdit_27, 5, 1, 1, 2)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_6.addWidget(self.lineEdit_37, 5, 5, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_6)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 6, 0, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_6.addWidget(self.lineEdit_28, 6, 1, 1, 2)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_6.addWidget(self.lineEdit_38, 6, 5, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 7, 0, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_6.addWidget(self.lineEdit_29, 7, 2, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_6.addWidget(self.lineEdit_39, 7, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 8, 0, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_6.addWidget(self.lineEdit_30, 8, 2, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_6.addWidget(self.lineEdit_40, 8, 5, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_6.addWidget(self.checkBox_7, 9, 0, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.groupBox_6)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 5, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_6)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 4, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_6)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 6, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_6)
        self.label_34.setObjectName("label_34")
        self.gridLayout_6.addWidget(self.label_34, 7, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_6)
        self.label_35.setObjectName("label_35")
        self.gridLayout_6.addWidget(self.label_35, 8, 3, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_6.addWidget(self.lineEdit_31, 9, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 0, 0, 3, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_2.addWidget(self.graphicsView_3)
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_5.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_4)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_5.addWidget(self.dateTimeEdit_2, 2, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 3, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_5.addWidget(self.lineEdit_21, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 5, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 2, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 4)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_7.setRowStretch(0, 2)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_7.setRowStretch(2, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        stylesheet = """ 
                 QTabBar::tab:selected {background: gray;}
                 QTabWidget>QWidget>QWidget{background: gray;}
                """
        self.tab_3.setStyleSheet(stylesheet)
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", "行李数"))
        self.label_5.setText(_translate("MainWindow", "英文名"))
        self.label_15.setText(_translate("MainWindow", "陪人数"))
        self.label_4.setText(_translate("MainWindow", "出生日期"))
        self.label_3.setText(_translate("MainWindow", "性别"))
        self.label_13.setText(_translate("MainWindow", "座位号"))
        self.label_12.setText(_translate("MainWindow", "航班号"))
        self.label_7.setText(_translate("MainWindow", "证件类型"))
        self.label_16.setText(_translate("MainWindow", "登机号"))
        self.label_6.setText(_translate("MainWindow", "入库时间"))
        self.label_17.setText(_translate("MainWindow", "登机口"))
        self.label_8.setText(_translate("MainWindow", "旅客编号"))
        self.label_18.setText(_translate("MainWindow", "起飞日期"))
        self.label.setText(_translate("MainWindow", "识别证件号"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.label_9.setText(_translate("MainWindow", "机器号"))
        self.label_19.setText(_translate("MainWindow", "起飞时间"))
        self.label_10.setText(_translate("MainWindow", "屏幕证件号"))
        self.label_11.setText(_translate("MainWindow", "订票证件号"))
        self.groupBox_2.setTitle(_translate("MainWindow", ""))
        self.label_21.setText(_translate("MainWindow", "证件原图缩略图"))
        self.label_22.setText(_translate("MainWindow", "则行间人像切图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "实时"))
        self.groupBox_6.setTitle(_translate("MainWindow", ""))
        self.checkBox_3.setText(_translate("MainWindow", "识别证件号"))
        self.checkBox_8.setText(_translate("MainWindow", "订票证件号"))
        self.checkBox_4.setText(_translate("MainWindow", "姓名"))
        self.checkBox_9.setText(_translate("MainWindow", "航班号"))
        self.checkBox_5.setText(_translate("MainWindow", "性别"))
        self.checkBox_10.setText(_translate("MainWindow", "座位号"))
        self.label_25.setText(_translate("MainWindow", "出生日期"))
        self.label_30.setText(_translate("MainWindow", "行李数"))
        self.checkBox_6.setText(_translate("MainWindow", "英文名"))
        self.label_26.setText(_translate("MainWindow", "入库时间"))
        self.label_27.setText(_translate("MainWindow", "证件类型"))
        self.label_28.setText(_translate("MainWindow", "旅客编号"))
        self.label_29.setText(_translate("MainWindow", "机器号"))
        self.checkBox_7.setText(_translate("MainWindow", "屏幕证件号"))
        self.label_32.setText(_translate("MainWindow", "登机号"))
        self.label_31.setText(_translate("MainWindow", "陪人数"))
        self.label_33.setText(_translate("MainWindow", "登机口"))
        self.label_34.setText(_translate("MainWindow", "起飞日期"))
        self.label_35.setText(_translate("MainWindow", "起飞时间"))
        self.groupBox_5.setTitle(_translate("MainWindow", ""))
        self.label_20.setText(_translate("MainWindow", "图片"))
        self.groupBox_4.setTitle(_translate("MainWindow", ""))
        self.label_23.setText(_translate("MainWindow", "查询条件"))
        self.checkBox.setText(_translate("MainWindow", "入库日期"))
        self.checkBox_2.setText(_translate("MainWindow", "机器号"))
        self.groupBox_3.setTitle(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", "退出"))
        self.label_24.setText(_translate("MainWindow", "功能模块"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_5.setText(_translate("MainWindow", "导出"))
        self.pushButton_3.setText(_translate("MainWindow", "上一条"))
        self.pushButton_4.setText(_translate("MainWindow", "下一条"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "模式分析"))

    def buttonExit(self):
        self.cursor.close()
        self.conn.close()
        self.close()

    def buttonclear(self):
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
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

    def buttonsearch(self):
        temp_sqlstring = self.sqlstring
        temp_sqlstring1 = self.sqlstring1
        temp_sqlstring2 = self.sqlstring2
        is_first = True
        is_first1 = True

        if self.checkBox_3.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " IDCARD='%s'" % self.lineEdit_22.text()
            else:
                temp_sqlstring += " and IDCARD='%s'" % self.lineEdit_22.text()

        if self.checkBox_4.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " NAME='%s'" % self.lineEdit_23.text()
            else:
                temp_sqlstring += " and NAME='%s'" % self.lineEdit_23.text()

        if self.checkBox_5.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " GENDER='%s'" % self.lineEdit_24.text()
            else:
                temp_sqlstring += " and GENDER='%s'" % self.lineEdit_24.text()

        if self.checkBox_6.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " ENGLISHNAME='%s'" % self.lineEdit_26.text()
            else:
                temp_sqlstring += " and ENGLISHNAME='%s'" % self.lineEdit_26.text()

        if self.checkBox_7.isChecked():
            is_first1 = False
            if is_first:
                is_first = False
                temp_sqlstring1 += " IDCARD='%s'" % self.lineEdit_31.text()
            else:
                temp_sqlstring1 += " and IDCARD='%s'" % self.lineEdit_31.text()

        if self.checkBox_8.isChecked():
            is_first1 = False
            if is_first:
                is_first = False
                temp_sqlstring1 += " IDCARD_ORDER='%s'" % self.lineEdit_32.text()
            else:
                temp_sqlstring1 += " and IDCARD_ORDER='%s'" % self.lineEdit_32.text()

        if self.checkBox_9.isChecked():
            is_first1 = False
            if is_first:
                is_first = False
                temp_sqlstring1 += " FLIGHTNO='%s'" % self.lineEdit_33.text()
            else:
                temp_sqlstring1 += " and FLIGHTNO='%s'" % self.lineEdit_33.text()

        if self.checkBox_10.isChecked():
            is_first1 = False
            if is_first:
                is_first = False
                temp_sqlstring1 += " SEATNO='%s'" % self.lineEdit_34.text()
            else:
                temp_sqlstring1 += " and SEATNO='%s'" % self.lineEdit_34.text()

        if self.checkBox_2.isChecked():
            is_first1 = False
            if is_first:
                is_first = False
                temp_sqlstring1 += " MACHINENO='%s'" % self.lineEdit_21.text()
            else:
                temp_sqlstring1 += " and MACHINENO='%s'" % self.lineEdit_21.text()

        if self.checkBox.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            else:
                temp_sqlstring += " and INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')

        print(temp_sqlstring)
        if is_first1:
            try:
                self.cursor.execute(temp_sqlstring)
                data = self.cursor.fetchall()
                if data:
                    for rec in data:
                        self.lineEdit_22.setText(rec[4])
                        self.lineEdit_23.setText(rec[5])
                        self.lineEdit_24.setText(rec[6])
                        self.lineEdit_25.setText(rec[8])
                        self.lineEdit_26.setText(rec[12])
                        self.lineEdit_27.setText(str(rec[15]))
                        self.lineEdit_28.setText(str(rec[17]))
                        temp_sqlstring1 += " PASSENGERNO='%s'" % rec[1]
                        print(temp_sqlstring1)
                        # pixmap.load(rec[])
                        # scaredPixmap = pixmap.scaled(760, 500, aspectRatioMode=Qt.KeepAspectRatio)
                        # item = QGraphicsPixmapItem(scaredPixmap)
                        # self.scene = QGraphicsScene(self)
                        # self.scene.addItem(item)
                        # self.graphicsView_2.setScene(self.scene)
                        self.cursor.execute(temp_sqlstring1)
                        data3 = self.cursor.fetchall()
                        for rec in data3:
                            self.lineEdit_29.setText(rec[1])
                            self.lineEdit_30.setText(rec[2])
                            self.lineEdit_31.setText(rec[3])
                            self.lineEdit_32.setText(rec[4])
                            self.lineEdit_33.setText(rec[6])
                            self.lineEdit_34.setText(rec[7])
                            self.lineEdit_35.setText(str(rec[8]))
                            self.lineEdit_36.setText(str(rec[9]))
                            self.lineEdit_37.setText((rec[10]))
                            self.lineEdit_38.setText((rec[11]))
                            self.lineEdit_39.setText((rec[12]))
                            self.lineEdit_40.setText((rec[13]))

                else:
                    print('false')
                    window = Dialog3(self)
                    window.show()

            except DatabaseError as e:
                print('查询出错')

        else:
            try:
                self.cursor.execute(temp_sqlstring1)
                data1 = self.cursor.fetchall()
                if data1:
                    for rec in data1:
                        self.lineEdit_29.setText(rec[1])
                        self.lineEdit_30.setText(rec[2])
                        self.lineEdit_31.setText(rec[3])
                        self.lineEdit_32.setText(rec[4])
                        self.lineEdit_33.setText(rec[6])
                        self.lineEdit_34.setText(rec[7])
                        self.lineEdit_35.setText(str(rec[8]))
                        self.lineEdit_36.setText(str(rec[9]))
                        self.lineEdit_37.setText((rec[10]))
                        self.lineEdit_38.setText((rec[11]))
                        self.lineEdit_39.setText((rec[12]))
                        self.lineEdit_40.setText((rec[13]))
                        temp_sqlstring += " PASSENGERNO='%s'" % rec[1]

                        self.cursor.execute(temp_sqlstring)
                        data4 = self.cursor.fetchall()
                        for rec in data4:
                            self.lineEdit_22.setText(rec[4])
                            self.lineEdit_23.setText(rec[5])
                            self.lineEdit_24.setText(rec[6])
                            self.lineEdit_25.setText(rec[8])
                            self.lineEdit_26.setText(rec[12])
                            self.lineEdit_27.setText(str(rec[15]))
                            self.lineEdit_28.setText(str(rec[17]))
                else:
                    print('false')
                    window = Dialog3(self)
                    window.show()

            except DatabaseError as e:
                print('查询出错')


    def buttonbefore(self):
        window = Dialog(self)
        window.show()
        print()

    def buttonafter(self):
        print()

    def buttonoutfile(self):
        temp_sqlstring = "select * from PSG_AJ_OCR where"
        is_first = True
        if self.checkBox_2.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " MACHINENO='%s'" % self.lineEdit_21.text()
            else:
                temp_sqlstring += " and MACHINENO='%s'" % self.lineEdit_21.text()

        if self.checkBox.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += " INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            else:
                temp_sqlstring += " and INTIME>=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit.dateTime().toString('yyyy-MM-dd hh:mm:ss') + "and INTIME<=to_date('%s','yyyy-mm-dd hh24:mi:ss')" % self.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd hh:mm:ss')

        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        fname = "E:/" + now + r".csv"
        outputFile = open(fname, "w")
        output = csv.writer(outputFile, dialect='excel')
        self.cursor.execute(temp_sqlstring)
        # self.cursor.execute("select * from PSG_AJ_OCR where PASSENGERNO ='TSN2014_20181107173702351'")

        cols = []
        for col in self.cursor.description:
            cols.append(col[0])
        output.writerow(cols)

        for row in self.cursor:
            output.writerow(row)

        outputFile.close
        window = Dialog2(self)
        window.show()


        # ===============================================ESC退出界面=======================================

    def keyPressEvent(self, e):  # 不懂这个函数用在哪里？
        # 重写控件centralwidget的键盘按下事件
        if e.key() == QtCore.Qt.Key_Escape:
            # 如果按下了ESC键则执行buttonExit函数
            self.buttonExit()

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

         self.cursor.execute(str(data))
         alldata = self.cursor.fetchall()
         temp_sqlstring1 = self.sqlstring1
         for rec in alldata:
             self.lineEdit.setText(rec[4])
             self.lineEdit_2.setText(rec[5])
             self.lineEdit_3.setText(rec[6])
             self.lineEdit_4.setText(rec[8])
             self.lineEdit_5.setText(rec[12])
             self.lineEdit_6.setText(str(rec[15]))
             self.lineEdit_7.setText(str(rec[17]))
             temp_sqlstring1 += " PASSENGERNO='%s'" % rec[1]

         self.cursor.execute(temp_sqlstring1)
         data1 = self.cursor.fetchall()
         for rec in data1:
             self.lineEdit_8.setText(rec[1])
             self.lineEdit_9.setText(rec[2])
             self.lineEdit_10.setText(rec[3])
             self.lineEdit_11.setText(rec[4])
             self.lineEdit_12.setText(rec[6])
             self.lineEdit_13.setText(rec[7])
             self.lineEdit_14.setText(str(rec[8]))
             self.lineEdit_15.setText(str(rec[9]))
             self.lineEdit_16.setText((rec[10]))
             self.lineEdit_17.setText((rec[11]))
             self.lineEdit_18.setText((rec[12]))
             self.lineEdit_19.setText((rec[13]))


class Backend(QThread):
    update_date = pyqtSignal(str)
    def run(self):
        while True:
            # data = "select * from PSG_AJ_OCR"
            data = "select * from（select * from PSG_AJ_OCR order by NO desc）where rownum=1"
            self.update_date.emit(data)
            time.sleep(3)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.buttonsearch)
        self.pushButton_2.clicked.connect(self.buttonclear)
        self.pushButton_3.clicked.connect(self.buttonbefore)
        self.pushButton_4.clicked.connect(self.buttonafter)
        self.pushButton_5.clicked.connect(self.buttonoutfile)
        self.pushButton_6.clicked.connect(self.buttonExit)

        self.b = Backend()
        self.b.update_date.connect(self.buttonstart)
        self.b.start()

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
        self.pwd.setText(u'已导出')

class Dialog3(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self._diawidth = 240  # 设置实例成员_diawidth,它的值为300
        self._diaheight = 100
        self.setWindowTitle("提示")  # 设置窗口标题
        self.pwd = QtWidgets.QLabel(self)
        self.pwd.setAlignment(Qt.AlignCenter)  # 设置QLabel居中显示
        self.pwd.setText(u'查询出错')



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
        self.pwd.setText('')
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginBtn = QtWidgets.QPushButton('Login', self)
        self.loginBtn.move(100, 90)
        self.loginBtn.clicked.connect(self.login)  # 绑定方法判断用户名和密码

    def login(self):
        if self.user.text() == 'tianjin' and self.pwd.text() == 'tianjin':
            # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
            self.accept()
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', 'User name or password error')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 建立一个app，把框架放在这个app中执行
    app.aboutToQuit.connect(app.deleteLater)
    pixmap = QtGui.QPixmap()
    dialog = LoginDialog()
    # if dialog.exec_():
    #     myshow = MyWindow()
    #     myshow.setStyleSheet("#MainWindow{border-image:url(./timg.jpg);}")
    #     myshow.show()
    #     sys.exit(app.exec_())  # 也可以写成app.exec_() sys.exit(0)，前者是循环整个界面，后者是退出app
    myshow = MyWindow()
    myshow.setStyleSheet("#MainWindow{border-image:url(./timg.jpg);}")
    myshow.show()
    sys.exit(app.exec_())
