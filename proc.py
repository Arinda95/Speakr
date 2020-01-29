##This facilitates processing with no window
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys, getopt
import re
import docx2txt
import os
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
import comtypes.client
import urlparse
import os.path
import threading
import subprocess as sp


def processing():
    ConfigFile = open("conf/conf.svcg", 'r')
    ConfigFileRead = ConfigFile.read()
    filename = re.findall(r'svfn(.*?)svfn',ConfigFileRead)
    file_name = filename[0]
    def audioWise():
        File = open("text/loadedFile.svcg", 'r')
        text = File.read()
        engine = CreateObject("SAPI.SpVoice")
        stream = CreateObject("SAPI.SpFileStream")
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

process = sp.Popen('loading.py')
PID = process.pid 
print PID
#processing()
#os.startfile('main.pyw')
#sys.exit()

