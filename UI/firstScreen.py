# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\projTry\UI\firstScreen1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd


class Ui_MainWindow(object):

    def __init__(self, controller):
        self.controller = controller
        self.ins_dict = {}
        self.lec_dict = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(255, 308)
        self.rate_label = QtWidgets.QWidget(MainWindow)
        self.rate_label.setObjectName("rate_label")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rate_label)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ins_combo_box = QtWidgets.QComboBox(self.rate_label)
        self.ins_combo_box.setObjectName("ins_combo_box")
        self.ins_combo_box.addItem("")
        ###my add
        self.add_ins_to_combobox()
        self.ins_combo_box.currentIndexChanged.connect(self.ins_combo_box_on_change_listener)
        ###
        self.verticalLayout.addWidget(self.ins_combo_box)
        self.lec_combo_box = QtWidgets.QComboBox(self.rate_label)
        self.lec_combo_box.setObjectName("lec_combo_box")
        ##my add
        self.lec_combo_box.currentIndexChanged.connect(self.lec_combo_box_on_change_listener)
        ##
        self.verticalLayout.addWidget(self.lec_combo_box)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(80, 50, 80, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rate_btn = QtWidgets.QPushButton(self.rate_label)
        self.rate_btn.setObjectName("rate_btn")
        self.verticalLayout_4.addWidget(self.rate_btn)

        # my add
        self.rate_btn.clicked.connect(self.on_rate_click_listener)
        #
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.rate_label)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.histogram_btn = QtWidgets.QPushButton(self.rate_label)
        self.histogram_btn.setObjectName("histogram_btn")
        self.verticalLayout_5.addWidget(self.histogram_btn)
        ##my Add
        self.histogram_btn.clicked.connect(self.on_show_histogram_listener)
        ##
        MainWindow.setCentralWidget(self.rate_label)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 255, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ins_combo_box.setItemText(0, _translate("MainWindow", "בחר מוסד לימודים..."))
        self.rate_btn.setText(_translate("MainWindow", "Get rate"))
        self.label.setText(_translate("MainWindow", ""))
        self.histogram_btn.setText(_translate("MainWindow", "Show histogram"))
        self.histogram_btn.setVisible(0)
        self.rate_btn.setVisible(0)

    def add_ins_to_combobox(self):
        self.ins_dict = self.controller.get_institutes()
        self.ins_dict = {str(k): v for k, v in self.ins_dict.items()}
        self.ins_combo_box.addItems(self.ins_dict)

    def ins_combo_box_on_change_listener(self):
        self.lec_combo_box.clear()
        self.lec_dict = self.controller.get_lecturers(self.ins_dict.get(self.ins_combo_box.currentText()))
        self.lec_dict = {str(k): v for k, v in self.lec_dict.items()}
        self.lec_combo_box.addItems(self.lec_dict)
        self.rate_btn.setVisible(1)

    def lec_combo_box_on_change_listener(self):
        self.histogram_btn.setVisible(0)

    def on_rate_click_listener(self):
        rating = self.controller.get_rate(self.lec_dict.get(self.lec_combo_box.currentText()))
        if rating != -1:
            self.label.setText("Rate - " + str(round(rating, 2)))
            self.histogram_btn.setVisible(1)
        else:
            self.label.setText("No comments for this lecturer")

    def on_show_histogram_listener(self):
        data_dict = self.controller.get_histogram(self.lec_dict.get(self.lec_combo_box.currentText()))
        data_dict['comments_num'].reverse()
        data_dict['rates'].reverse()
        frequencies = data_dict['rates']
        # In my original code I create a series and run on that,
        # so for consistency I create a series from the list.
        freq_series = pd.Series.from_array(frequencies)
        data_dict['years'].reverse()

        x_labels = data_dict['years']

        # Plot the figure.
        plt.figure(figsize=(12, 8))
        ax = freq_series.plot(kind='bar')
        ax.set_title(self.lec_combo_box.currentText()[::-1])
        ax.set_xlabel('Years')
        ax.set_ylabel('Rate')
        ax.set_xticklabels(x_labels)

        rects = ax.patches

        # For each bar: Place a label
        for rect in rects:
            # Get X and Y placement of label from rect.
            y_value = rect.get_height()
            x_value = rect.get_x() + rect.get_width() / 2

            # Number of points between bar and label. Change to your liking.
            space = -30
            # Vertical alignment for positive values
            va = 'bottom'

            # If value of bar is negative: Place label below bar
            if y_value < 0:
                # Invert space to place label below
                space *= -1
                # Vertically align label at top
                va = 'top'

            # Use Y value as label and format number with one decimal place

            label = str("{:.2f}".format(y_value))+"\n#"+str(data_dict['comments_num'][0])
            data_dict['comments_num'].pop(0)
            # Create annotation
            plt.annotate(
                label,  # Use `label` as label
                (x_value, y_value),  # Place label at end of the bar
                xytext=(0, space),  # Vertically shift label by `space`
                textcoords="offset points",  # Interpret `xytext` as offset in points
                ha='center',  # Horizontally center label
                va=va)  # Vertically align label differently for
        plt.show()

