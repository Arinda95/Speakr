# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4 import QtWebKit
from PyQt4.QtGui import QFileDialog
import re
from PyQt4.phonon import Phonon
import urlparse
import os.path
import pyPdf
from pyPdf import PdfFileReader
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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(693, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: black;"))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        ##Media Obj
        ConfigFile = open("conf\conf.svcg", 'r')
        ConfigFileRead = ConfigFile.read()
        file_name = re.findall(r'svfn(.*?)svfn',ConfigFileRead)
        self.filename = file_name[0]
        self.media_obj = Phonon.MediaObject(self)
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media_obj, self.audio_output)
        self.media_obj.setCurrentSource(Phonon.MediaSource('media/AudioBook.wav'))
        ##
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        ##
        self.horizontalSlider_2 = Phonon.VolumeSlider(self.centralwidget)
        self.horizontalSlider_2.setAudioOutput(self.audio_output)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout.addWidget(self.horizontalSlider_2, 5, 6, 1, 1)
        self.horizontalSlider_2.setStyleSheet(_fromUtf8("""
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
        ##
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 3, 1, 1, 7)
        cwd = os.getcwd()
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///"+cwd+"/disp/filestop.html")))
        ##
        self.horizontalSlider = Phonon.SeekSlider(self.centralwidget)
        self.horizontalSlider.setMediaObject(self.media_obj)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.setStyleSheet(_fromUtf8("""
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
                background: rgba(35, 35, 35);
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
        ##
        self.gridLayout.addWidget(self.horizontalSlider, 5, 2, 1, 4)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_2.setStyleSheet(_fromUtf8("background-color: black;"))
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 7)
        ##
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line_2"))
        self.line.setStyleSheet(_fromUtf8("background-color: black;"))
        self.gridLayout.addWidget(self.line, 4, 1, 1, 7)
        ##
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 2, 1)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 14pt \"Segoe Script\";\n"
"color: rgb(0, 94, 138);"))
        self.pushButton_play = QtGui.QPushButton(self.centralwidget)
        self.pushButton_play.setObjectName(_fromUtf8("pushButton_play"))
        self.gridLayout.addWidget(self.pushButton_play, 5, 1, 1, 1)
        self.pushButton_play.setIcon(QtGui.QIcon('imgs/playprop.png'))
        self.pushButton_play.setIconSize(QtCore.QSize(32,32))
        self.pushButton_play.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding: 0px;\n"
"border-radius: 0px;"))
        ##pause
        self.pushButton_pause = QtGui.QPushButton(self.centralwidget)
        self.pushButton_pause.setObjectName(_fromUtf8("pushButton_pause"))
        self.pushButton_pause.setIcon(QtGui.QIcon('imgs/pauseprop.png'))
        self.pushButton_pause.setIconSize(QtCore.QSize(32,32))
        self.gridLayout.addWidget(self.pushButton_pause, 5, 1, 1, 1)
        self.pushButton_pause.setVisible(False)
        self.pushButton_pause.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding: 0px;\n"
"border-radius: 0px;"))
        ##
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 2, 3)
        self.label.setStyleSheet(_fromUtf8("font: 75 14pt \"Segoe Script\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 7, 1, 1)
        self.pushButton_2.setIcon(QtGui.QIcon('imgs/ejectprop.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(32,32))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"padding: 0px;\n"
"border-radius: 0px;"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ##
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_play, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_pause.show)
        QtCore.QObject.connect(self.pushButton_pause, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_play.show)
        QtCore.QObject.connect(self.pushButton_pause, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_play.show)
        QtCore.QObject.connect(self.pushButton_play, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_play.hide)
        QtCore.QObject.connect(self.pushButton_pause, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_pause.hide)
        QtCore.QObject.connect(self.pushButton_pause, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_pause)
        QtCore.QObject.connect(self.pushButton_play, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_play)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_export)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SPEAKr", None))
        ##Author
        ConfigFile = open("conf\conf.svcg", 'r')
        ConfigFileRead = ConfigFile.read()
        filename = re.findall(r'svfn(.*?)svfn',ConfigFileRead)
        file_name = filename[0]
        if file_name[-5:] == ".docx":
            import zipfile, lxml.etree
            zf = zipfile.ZipFile(file_name)
            doc = lxml.etree.fromstring(zf.read('docProps/core.xml'))
            ns={'dc': 'http://purl.org/dc/elements/1.1/'}
            creator = doc.xpath('//dc:creator', namespaces=ns)[0].text
            self.label_2.setText(_translate("MainWindow", creator, None))
        elif file_name[-4:] == ".pdf":
            pdfFile = PdfFileReader(file(file_name, 'rb'))
            docInfo = pdfFile.getDocumentInfo()
            for metaItem in docInfo:
                data = '[+] ' + metaItem + ':' + docInfo[metaItem]
                if "Author" in metaItem:
                    print data
                    self.label_2.setText(_translate("MainWindow", data[12:], None))
        #self.pushButton_play.setText(_translate("MainWindow", "play", None))
        #self.pushButton_pause.setText(_translate("MainWindow", "pause", None))
        ##Book title
        book = os.path.splitext(os.path.basename(urlparse.urlsplit(file_name).path))
        print book[0]+book[1]
        self.label.setText(_translate("MainWindow", book[0], None))
        #self.pushButton_2.setText(_translate("MainWindow", "export audio book", None))

    def run_play(self):
        self.media_obj.play()
        cwd = os.getcwd()
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///"+cwd+"/disp/fileplay.html")))
    
    def run_pause(self):
        self.media_obj.pause()
        cwd = os.getcwd()
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///"+cwd+"/disp/filestop.html")))

    #def run_import(self):
    #    importFile = QFileDialog.getOpenFileName(parent=None, caption='Open File', directory='', filter='MP3 files (*.mp3)')
    #    global import_file
    #    import_file = str(importFile)

    def run_export(self):
        ConfigFile = open("conf\conf.svcg", 'r')
        ConfigFileRead = ConfigFile.read()
        filename = re.findall(r'svfn(.*?)svfn',ConfigFileRead)
        file_name = filename[0]
        book = os.path.splitext(os.path.basename(urlparse.urlsplit(file_name).path))
        title = book[0]+book[1]
        exportFile = QFileDialog.getExistingDirectory(self, "Select Directory")
        global export_file
        export_file = str(exportFile)
        source = "media/Audiobook.wav"
        destination = ""+export_file+"/"+str(title)+".wav"
        shutil.copy(source, destination)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())