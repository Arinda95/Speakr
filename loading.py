# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from PyQt4 import QtCore, QtGui
import sys, getopt
import re
import docx2txt
import os
from comtypes.client import CreateObject
import comtypes.client
import urlparse
import os.path
import threading

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
        Dialog.resize(447, 113)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imgs/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: black;"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet(_fromUtf8("color: white;"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SPEAKr", None))
        self.label.setText(_translate("Dialog", "Processing data...Please Wait. Could take up to 5 minutes. Do not close even when if freezes", None))

def processing():
    QtCore.QCoreApplication.processEvents()
    ConfigFile = open("conf/conf.svcg", 'r')
    ConfigFileRead = ConfigFile.read()
    filename = re.findall(r'svfn(.*?)svfn',ConfigFileRead)
    file_name = filename[0]
    def audioWise():
        File = open("text/loadedFile.svcg", 'r')
        text = File.read()
        engine = CreateObject("SAPI.SpVoice")
        stream = CreateObject("SAPI.SpFileStream")
        from comtypes.gen import SpeechLib
        stream.Open('media/AudioBook.wav', SpeechLib.SSFMCreateForWrite)
        engine.AudioOutputStream = stream
        engine.speak(text)
        stream.Close()

    def convert(fname):
        manager = PDFResourceManager()
        output = StringIO()
        codec = 'ascii'
        laparams=LAParams()
        converter = TextConverter(manager, output, codec=codec)
        interpreter = PDFPageInterpreter(manager, converter)
        infile = file(fname, 'rb')
        maxpages = 0
        password = ""
        caching = True
        pagenums = set()
        for page in PDFPage.get_pages(infile, pagenums,  maxpages=maxpages, password=password, caching=caching):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
        return text


    if file_name[-5:] == ".docx":
        wdFormatPDF = 17
        in_file = os.path.abspath(file_name)
        newFile = in_file[:-5]
        newOutFile = str(""+newFile+".pdf")
        book = os.path.splitext(os.path.basename(urlparse.urlsplit(newOutFile).path))
        data_dest = str(book[0]+book[1])
        out_file = os.path.abspath("temp/"+data_dest+"")
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        doc_data = convert(out_file)
        doc_write = open("text/loadedFile.svcg", 'w')
        doc_write.write(doc_data)
        doc_write.close()
        audioWise()

    elif file_name[-4:] == ".txt":
        txt = open(file_name, 'r')
        txt_write = txt.read()
        new_file = open("text/loadedFile.svcg", 'w')
        new_file.write(txt_write)
        new_file.close()
        audioWise()

    elif file_name[-4:] == ".pdf":
        file_data = convert(file_name)
        txt_write = open("text/loadedFile.svcg", 'w')
        txt_write.write(file_data)
        txt_write.close()
        audioWise()

        #resource_manager = PDFResourceManager()
        #ret_string = StringIO()
        #codec = 'utf-8'
        #laparams = LAParams()
        #device = TextConverter(resource_manager, ret_string, codec=codec)
        #file_path = file(file_name, 'rb')
        #interpreter = PDFPageInterpreter(resource_manager, device)
        #password = ""
        #maxpages = 0
        #caching = True
        #pagenos = set()
        #print "i get there"
        #for page in PDFPage.get_pages(file_path, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            #interpreter.process_page(page)
            #text = ret_string.getvalue()
            #save_to_tempFile = open("text/loadedFile.svcg", 'w')
            #save_to_tempFile.write(text)
            #audioWise()

    os.startfile("main.pyw")
    sys.exit()
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    processing()
    sys.exit(app.exec_())
