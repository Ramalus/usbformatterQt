# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usbformatter.ui'
#
# Created: Fri Feb 21 00:30:32 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(377, 152)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/loading.gif")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name_edit = QtGui.QLineEdit(self.centralwidget)
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.gridLayout.addWidget(self.name_edit, 1, 2, 1, 1)
        self.devices_combo = QtGui.QComboBox(self.centralwidget)
        self.devices_combo.setObjectName(_fromUtf8("devices_combo"))
        self.gridLayout.addWidget(self.devices_combo, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.format_button = QtGui.QPushButton(self.centralwidget)
        self.format_button.setMinimumSize(QtCore.QSize(100, 70))
        self.format_button.setObjectName(_fromUtf8("format_button"))
        self.horizontalLayout.addWidget(self.format_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.refresh_button = QtGui.QPushButton(self.centralwidget)
        self.refresh_button.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_button.setObjectName(_fromUtf8("refresh_button"))
        self.gridLayout_2.addWidget(self.refresh_button, 1, 0, 1, 1)
        self.label_status = QtGui.QLabel(self.centralwidget)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_2.addWidget(self.label_status, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Application = QtGui.QMenu(self.menubar)
        self.menu_Application.setObjectName(_fromUtf8("menu_Application"))
        MainWindow.setMenuBar(self.menubar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_Application.addAction(self.action_exit)
        self.menubar.addAction(self.menu_Application.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "USBFormatter", None))
        self.label_2.setText(_translate("MainWindow", "New Name:", None))
        self.label.setText(_translate("MainWindow", "Device:", None))
        self.format_button.setText(_translate("MainWindow", "Format", None))
        self.refresh_button.setText(_translate("MainWindow", "Refresh", None))
        self.label_status.setText(_translate("MainWindow", "Welcome to USBFormatter.", None))
        self.menu_Application.setTitle(_translate("MainWindow", "&Application", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))
        self.action_exit.setText(_translate("MainWindow", "E&xit", None))

