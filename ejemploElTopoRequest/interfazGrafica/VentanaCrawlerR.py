from tkinter import *
from tkinter import ttk
from spyder.spyder import spyder
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
import os
import sys


class VentanaCrawlerR():

   # def flush(self):
    #  pass

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title('Crawler Remoto')
        toolbar = Frame(self.ventana)
        toolbar.pack(side="top", fill="x")
        BTN_Iniciar = Button(self.ventana, text="Iniciar", command=self.main)
        BTN_Iniciar.pack(in_=toolbar, side="left")
        #b2.pack(in_=toolbar, side="left")
        self.text = Text(self.ventana, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        sys.stdout = StdoutRedirector(self.text)
        self.ventana.mainloop()



    def main(self):
       os.system('pwd')
       os.system("python ./interfazGrafica/Multihilo.py")

class StdoutRedirector(object):
    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert('end', str)
        self.text_area.see('end')
