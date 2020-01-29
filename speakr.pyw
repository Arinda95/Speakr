# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mini_speakr.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import pyttsx

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

class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(379, 387)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: black;"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_close = QtGui.QPushButton(Dialog)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.gridLayout.addWidget(self.pushButton_close, 2, 0, 1, 1)
        self.pushButton_close.setStyleSheet(_fromUtf8("background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.pushButton_read = QtGui.QPushButton(Dialog)
        self.pushButton_read.setObjectName(_fromUtf8("pushButton_read"))
        self.gridLayout.addWidget(self.pushButton_read, 1, 0, 1, 1)
        self.pushButton_read.setStyleSheet(_fromUtf8("background-color: rgb(53, 53, 53);\n"
"color: rgb(255, 255, 255);\n"
"font: 25 10pt \"Roboto bold\";\n"
"padding: 5px;\n"
"border-radius: 2px"))
        self.speedSlider = QtGui.QSlider(Dialog)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setValue(50)
        self.speedSlider.setObjectName(_fromUtf8("speedSlider"))
        self.gridLayout.addWidget(self.speedSlider, 2, 2, 1, 1)
        self.speedSlider.setStyleSheet(_fromUtf8("""
            QSlider{
            padding: 0px;
            border-radius: 4px;
            }
            QSlider::groove:horizontal {
                background: black;
                height: 40px;
            }

            QSlider::sub-page:horizontal {
                background: rgb(63, 0, 0);
                height: 40px;
            }

            QSlider::add-page:horizontal {
                background: rgb(35, 35, 35);
                height: 40px;
            }

            QSlider::handle:horizontal {
                background: white;
                border: 0px;
                width: 5px;
                margin-top: 0px;
                margin-bottom: 0px;
                border-radius: 0px;
            } """))
        self.volumeSlider = QtGui.QSlider(Dialog)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.gridLayout.addWidget(self.volumeSlider, 1, 2, 1, 1)
        self.volumeSlider.setStyleSheet(_fromUtf8("""
            QSlider{
            padding: 0px;
            border-radius: 4px;
            }
            QSlider::groove:horizontal {
                background: black;
                height: 40px;
            }

            QSlider::sub-page:horizontal {
                background: rgb(63, 0, 0);
                height: 40px;
            }

            QSlider::add-page:horizontal {
                background: rgb(35, 35, 35);
                height: 40px;
            }

            QSlider::handle:horizontal {
                background: white;
                border: 0px;
                width: 5px;
                margin-top: 0px;
                margin-bottom: 0px;
                border-radius: 0px;
            } """))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_2.setStyleSheet(_fromUtf8("color: white;"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label.setStyleSheet(_fromUtf8("color: white;"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label_3.setStyleSheet(_fromUtf8("color: white;"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_4.setStyleSheet(_fromUtf8("color: white;"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: white;"))
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.volumeSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_3.setNum)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_4.setNum)
        QtCore.QObject.connect(self.pushButton_read, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_read)
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SPEAKr", None))
        self.pushButton_close.setText(_translate("Dialog", "Close", None))
        self.pushButton_read.setText(_translate("Dialog", "Read", None))
        self.label_2.setText(_translate("Dialog", "Speed", None))
        self.label.setText(_translate("Dialog", "Volume", None))
        self.label_3.setText(_translate("Dialog", "50", None))
        self.label_4.setText(_translate("Dialog", "50", None))

    def run_read(self):
        input_data = self.plainTextEdit.toPlainText()
        speed_raw = self.speedSlider.value()
        volume_raw = self.volumeSlider.value()
        speed_num = speed_raw - 70
        volume_num = volume_raw/100
        engine = pyttsx.init()
        speed = engine.getProperty('rate')
        engine.setProperty('rate', speed+speed_num)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume-volume_num)
        engine.say(input_data)
        engine.runAndWait()


    def run_close(self):
        sys.exit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())