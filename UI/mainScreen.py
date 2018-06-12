# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\projTry\UI\mainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import numpy
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import sys
from UI.table import table_ui


class Ui_MainWindow(object):

    def __init__(self, controller):
        self.controller = controller
        self.ins_dict = {}
        self.lec_dict = {}

    def open_table(self, lecturers,ins_name):
        self.app = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.ui = table_ui()
        self.ui.setupUi(self.Form)
        self.ui.set_data(lecturers,ins_name)
        self.Form.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 290)
        MainWindow.setMaximumSize(QtCore.QSize(321, 399))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.lec_tab = QtWidgets.QWidget()
        self.lec_tab.setObjectName("lec_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lec_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ins_combo_box = QtWidgets.QComboBox(self.lec_tab)
        self.ins_combo_box.setObjectName("ins_combo_box")
        self.ins_combo_box.addItem("")
        ###my add

        self.ins_combo_box.currentIndexChanged.connect(self.ins_combo_box_on_change_listener)
        ###
        self.verticalLayout.addWidget(self.ins_combo_box)
        self.lec_combo_box = QtWidgets.QComboBox(self.lec_tab)
        self.lec_combo_box.setObjectName("lec_combo_box")
        ##my add
        self.lec_combo_box.currentIndexChanged.connect(self.lec_combo_box_on_change_listener)
        ##
        self.verticalLayout.addWidget(self.lec_combo_box)
        self.rate_btn = QtWidgets.QPushButton(self.lec_tab)
        self.rate_btn.setObjectName("rate_btn")
        self.verticalLayout.addWidget(self.rate_btn, 0, QtCore.Qt.AlignHCenter)
        # my add
        self.rate_btn.clicked.connect(self.on_rate_click_listener)
        #
        self.histogram_btn = QtWidgets.QPushButton(self.lec_tab)
        self.histogram_btn.setObjectName("histogram_btn")
        ##my Add
        self.histogram_btn.clicked.connect(self.on_show_histogram_listener)
        ##
        self.verticalLayout.addWidget(self.histogram_btn, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.lec_tab)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget.addTab(self.lec_tab, "")
        self.ins_tab = QtWidgets.QWidget()
        self.ins_tab.setObjectName("ins_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ins_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.by_ins_comboBox = QtWidgets.QComboBox(self.ins_tab)
        self.by_ins_comboBox.setObjectName("by_ins_comboBox")
        self.by_ins_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.by_ins_comboBox)
        ##my add
        self.by_ins_comboBox.currentIndexChanged.connect(self.by_ins_comboBox_on_change_listener)
        ##
        self.dep_btn = QtWidgets.QPushButton(self.ins_tab)
        self.by_table_btn = QtWidgets.QPushButton(self.ins_tab)
        self.by_table_btn.setObjectName("by_table_btn")
        self.dep_btn.setObjectName("dep_btn")
        ##
        self.dep_btn.clicked.connect(self.on_show_by_dep_clicked)
        self.by_table_btn.clicked.connect(self.on_by_table_clicked)
        ##
        self.verticalLayout_3.addWidget(self.dep_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.by_table_btn, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.ins_tab, "")
        self.cmp_tab = QtWidgets.QWidget()
        self.cmp_tab.setObjectName("cmp_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cmp_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cmp_ins_combo_box = QtWidgets.QComboBox(self.cmp_tab)
        self.cmp_ins_combo_box.setObjectName("cmp_ins_combo_box")
        self.cmp_ins_combo_box.addItem("")
        self.verticalLayout_2.addWidget(self.cmp_ins_combo_box)
        self.cmp_ins2_combo_box = QtWidgets.QComboBox(self.cmp_tab)
        self.cmp_ins2_combo_box.setObjectName("cmp_ins2_combo_box")
        self.cmp_ins2_combo_box.addItem("")
        self.verticalLayout_2.addWidget(self.cmp_ins2_combo_box)
        self.cmp_btn = QtWidgets.QPushButton(self.cmp_tab)
        self.cmp_btn.setObjectName("cmp_btn")
        ##my add
        self.cmp_btn.clicked.connect(self.on_cmp_btn_clicked_listener)
        ##
        self.verticalLayout_2.addWidget(self.cmp_btn, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.cmp_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##my add
        self.add_ins_to_combobox()
        ##

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ins_combo_box.setItemText(0, _translate("MainWindow", "בחר מוסד לימודים..."))
        self.by_ins_comboBox.setItemText(0, _translate("MainWindow", "בחר מוסד לימודים..."))
        self.cmp_ins_combo_box.setItemText(0, _translate("MainWindow", "בחר מוסד לימודים..."))
        self.cmp_ins2_combo_box.setItemText(0, _translate("MainWindow", "בחר מוסד לימודים..."))
        self.rate_btn.setText(_translate("MainWindow", "Get rank"))
        self.histogram_btn.setText(_translate("MainWindow", "Show histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lec_tab), _translate("MainWindow", "By lecturer"))
        self.dep_btn.setText(_translate("MainWindow", "Get rank"))
        self.by_table_btn.setText(_translate("MainWindow", "Get lecturers table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ins_tab), _translate("MainWindow", "By Institute"))
        self.cmp_btn.setText(_translate("MainWindow", "Compare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cmp_tab), _translate("MainWindow", "Compare institutes"))
        self.dep_btn.setVisible(0)
        self.by_table_btn.setVisible(0)
        self.rate_btn.setVisible(0)
        self.histogram_btn.setVisible(0)

    def add_ins_to_combobox(self):
        self.ins_dict = self.controller.get_institutes()
        self.ins_dict = {str(k): v for k, v in self.ins_dict.items()}
        self.ins_combo_box.addItems(self.ins_dict)
        self.by_ins_comboBox.addItems(self.ins_dict)
        self.cmp_ins_combo_box.addItems(self.ins_dict)
        self.cmp_ins2_combo_box.addItems(self.ins_dict)

    def ins_combo_box_on_change_listener(self):
        self.lec_combo_box.clear()
        if self.ins_combo_box.currentText() != "בחר מוסד לימודים...":
            self.lec_dict = self.controller.get_lecturers(self.ins_dict.get(self.ins_combo_box.currentText()))
            self.lec_dict = {str(k): v for k, v in self.lec_dict.items()}
            self.lec_combo_box.addItems(self.lec_dict)
            self.rate_btn.setVisible(1)

        else:
            self.rate_btn.setVisible(0)
            self.label.setText('')

    def by_ins_comboBox_on_change_listener(self):
        if self.by_ins_comboBox.currentText() != "בחר מוסד לימודים...":
            self.dep_btn.setVisible(1)
            self.by_table_btn.setVisible(1)
        else:
            self.dep_btn.setVisible(0)
            self.by_table_btn.setVisible(0)

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

        plt.plot(data_dict['years'], data_dict['rates'], color='red')

        plt.ylabel('Rate')
        plt.xlabel('Year')
        plt.show()
        # frequencies = data_dict['rates']
        # freq_series = pd.Series.from_array(frequencies)
        # x_labels = data_dict['years']
        #
        # # Plot the figure.
        # plt.figure(figsize=(12, 8))
        # ax = freq_series.plot(color='red')
        # ax.set_title(self.lec_combo_box.currentText()[::-1])
        # ax.set_xlabel('Years')
        # ax.set_ylabel('Rate')
        # ax.set_xticklabels(x_labels)
        #
        # rects = ax.patches
        #
        # # For each bar: Place a label
        # for rect in rects:
        #     # Get X and Y placement of label from rect.
        #     y_value = rect.get_height()
        #     x_value = rect.get_x() + rect.get_width() / 2
        #
        #     # Number of points between bar and label. Change to your liking.
        #     space = -30
        #     # Vertical alignment for positive values
        #     va = 'bottom'
        #
        #     # If value of bar is negative: Place label below bar
        #     if y_value <= 0:
        #         # Invert space to place label below
        #         space *= -1
        #         # Vertically align label at top
        #         va = 'top'
        #
        #     # Use Y value as label and format number with one decimal place
        #
        #     label = str("{:.2f}".format(y_value)) + "/5\n#" + str(data_dict['comments_num'][0])
        #     data_dict['comments_num'].pop(0)
        #     # Create annotation
        #     plt.annotate(
        #         label,  # Use `label` as label
        #         (x_value, y_value),  # Place label at end of the bar
        #         xytext=(0, space),  # Vertically shift label by `space`
        #         textcoords="offset points",  # Interpret `xytext` as offset in points
        #         ha='center',  # Horizontally center label
        #         va=va
        #     )  # Vertically align label differently for
        # plt.show()

    def on_show_by_dep_clicked(self):

        data_rec = self.controller.get_by_dep(self.ins_dict.get(self.by_ins_comboBox.currentText()))
        name_list = [name[::-1] for name in data_rec.keys()]
        labels = tuple(name_list)
        sizes = [size[0] for size in data_rec.values()]
        max_rate = sizes.index(max(sizes))
        exp_list = [0] * len(sizes)
        exp_list[max_rate] = 0.1
        explode = tuple(exp_list)

        def absolute_value(val):
            new_sizes = numpy.array(sizes)
            a = val / 100. * new_sizes.sum()
            a = "{:.2f}".format(a)
            return float(a)

        plt.figure(figsize=(15, 15))
        total_comments_num = 0
        rate = 0

        for val in data_rec.values():
            rate += val[0] * val[1]
            total_comments_num += val[1]

        rate = rate / total_comments_num
        plt.text(1.2, 1, "{:.2f}".format(rate) + '/5' + ("דירוג " + self.by_ins_comboBox.currentText() + ': ')[::-1],
                 fontsize=14)
        plt.pie(sizes, explode=explode, labels=labels, colors=None,
                autopct=absolute_value, shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()

    def on_cmp_btn_clicked_listener(self):
        data_rec_ins1 = self.controller.get_histogram_by_ins(self.ins_dict.get(self.cmp_ins_combo_box.currentText()))
        data_rec_ins2 = self.controller.get_histogram_by_ins(self.ins_dict.get(self.cmp_ins2_combo_box.currentText()))

        list1 = sorted(data_rec_ins1);
        list2 = sorted(data_rec_ins2);

        N = len(data_rec_ins1.keys())
        ins1 = tuple(data_rec_ins1[year] for year in list1)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111)
        rects1 = ax.bar(ind, ins1, width, color='royalblue')

        ins2 = tuple(data_rec_ins2[year] for year in list2)

        rects2 = ax.bar(ind + width, ins2, width, color='red')

        # add some
        ax.set_ylabel('Rate')
        ax.set_xticks(ind + width / 2)
        if list1.__len__() > list2.__len__():
            ax.set_xticklabels(list1)
        else:
            ax.set_xticklabels(list2)

        ax.legend((rects1[0], rects2[0]),
                  (self.cmp_ins_combo_box.currentText()[::-1], self.cmp_ins2_combo_box.currentText()[::-1]))

        plt.show()

    def on_by_table_clicked(self):
        lecturers = list(self.controller.get_lecturers_table(self.ins_dict.get(self.by_ins_comboBox.currentText())))
        self.open_table(lecturers,self.by_ins_comboBox.currentText())
