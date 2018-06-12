# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\projTry\UI\table.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView


class table_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 724)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 110, 651, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 20, 651, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "שם המרצה"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "מחלקה"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "מספר תגובות"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "דירוג"))
        self.label.setText(_translate("Form", "רשימת מרצים עבור -"))

    def set_data(self, lecturers, ins_name):

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.label.setText("רשימת מרצים עבור - " + ins_name)
        for lec in lecturers:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(lec["lecturer_name"]))
            self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(lec["faculty"]))
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(lec["num_of_comments"])))
            if lec["rate"] != -1:
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(round(lec["rate"], 4))))
            else:
                self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem("אין דירוג"))
