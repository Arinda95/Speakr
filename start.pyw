# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
from PyQt4.QtGui import QFileDialog
import sys
import os

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(650, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: black;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px"))
        cwd = os.getcwd()
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///"+cwd+"/imgs/logo.png")))
        self.gridLayout.addWidget(self.webView, 0, 0, 9, 1)
        self.pushButton_about = QtGui.QPushButton(self.centralwidget)
        self.pushButton_about.setObjectName(_fromUtf8("pushButton_about"))
        self.gridLayout.addWidget(self.pushButton_about, 0, 4, 1, 1)
        self.pushButton_about.setStyleSheet(_fromUtf8("background-color: rgb(53, 53, 53);\n"
"font: 25 10pt \"Roboto Bold\";\n"
"color: rgb(230, 230, 230);\n"
"padding: 5px;\n"
"border-radius: 2px;"))

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 4)
        ##
        rece_list = open("conf/rece.svcg").readlines()
        self.comboBox.addItems(rece_list)
        self.comboBox.setStyleSheet(_fromUtf8("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"padding: 5px;\n"
"border-radius: 2px"))

        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.gridLayout.addWidget(self.pushButton_browse, 2, 4, 1, 1)
        self.pushButton_browse.setStyleSheet(_fromUtf8("background-color: rgb(53, 53, 53);\n"
"font: 25 10pt \"Roboto Bold\";\n"
"color: rgb(230, 230, 230);\n"
"padding: 5px;\n"
"border-radius: 2px;"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 3)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"font: 25 10pt \"Roboto Bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.pushButton_sns = QtGui.QPushButton(self.centralwidget)
        self.pushButton_sns.setObjectName(_fromUtf8("pushButton_sns"))
        self.gridLayout.addWidget(self.pushButton_sns, 6, 1, 1, 4)
        self.pushButton_sns.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 186, 86, 255), stop:0.465909 rgba(235, 112, 61, 255), stop:1 rgba(167, 28, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.pushButton_direct = QtGui.QPushButton(self.centralwidget)
        self.pushButton_direct.setObjectName(_fromUtf8("pushButton_direct"))
        self.gridLayout.addWidget(self.pushButton_direct, 7, 1, 1, 4)
        self.pushButton_direct.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 186, 86, 255), stop:0.465909 rgba(235, 112, 61, 255), stop:1 rgba(167, 28, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.pushButton_exit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.gridLayout.addWidget(self.pushButton_exit, 8, 1, 1, 4)
        self.pushButton_exit.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 186, 86, 255), stop:0.465909 rgba(235, 112, 61, 255), stop:1 rgba(167, 28, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto Bold\";\n"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto Bold\";\n"))
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.gridLayout.addWidget(self.label_title, 5, 1, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pushButton_browse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_browse)
        QtCore.QObject.connect(self.pushButton_direct, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_speakr)
        QtCore.QObject.connect(self.pushButton_sns, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_saveAndStart)
        QtCore.QObject.connect(self.pushButton_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_exit)
        QtCore.QObject.connect(self.pushButton_about, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_about)
        ##
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.run_switch)
        QtCore.QObject.connect(self.pushButton_browse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_switch)
        ##
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.run_switch2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SPEAKr", None))
        self.pushButton_about.setText(_translate("MainWindow", "About", None))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_sns.setText(_translate("MainWindow", "Save and start", None))
        self.pushButton_direct.setText(_translate("MainWindow", "Use Direct SPEAKr", None))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit", None))
        self.label.setText(_translate("MainWindow", "Browse for file", None))
        self.label_2.setText(_translate("MainWindow", "Previous file", None))
        self.label_title.setText(_translate("MainWindow", "Book title", None))

    def run_switch(self):
        self.comboBox.setEnabled(False)

    def run_switch2(self):
        selected = self.comboBox.currentText()
        global current_file
        current_file = str(selected)
        self.pushButton_browse.setEnabled(False)
        self.lineEdit.setEnabled(False)

    def run_browse(self):
        filename = QFileDialog.getOpenFileName(parent=None, caption='Open File', directory='', filter='PDF files, Docx files, Text files, (*.pdf;*.docx;*.txt)')
        self.lineEdit.setText(filename)
        global current_file
        current_file = str(filename)

    def run_speakr(self):
        os.startfile("speakr.exe")

    def run_saveAndStart(self):
        settings = "curr_config: FILENAME = svfn"+current_file+"svfn."
        with open("conf/conf.svcg", "w") as config_file:
            config_file.write(settings)

        with open("conf/rece.svcg", "w") as recent_file:
            recent_file.write("{}".format(current_file))
        os.startfile("loading.exe")
        sys.exit()

    def run_exit(self):
        sys.exit()

    def run_about(self):
        cwd = os.getcwd()
        os.startfile(""+cwd+"\info\info.pdf")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
