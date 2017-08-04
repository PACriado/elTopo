from tkinter import *
from tkinter import ttk
from spyder.spyder import spyder
import os
import sys
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config

class VentanaCrawler():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title('Crawler Local')
        toolbar = Frame(self.ventana)
        toolbar.pack(side="top", fill="x")
        BTN_Iniciar = Button(self.ventana, text="Iniciar", command=self.print_stdout)

        BTN_Iniciar.pack(in_=toolbar, side="left")
        self.text = Text(self.ventana, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")
       # sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):
        configuracion = config("./configElTopo/config.json")
        theSpyder = spyder(rutaConfig= "./configElTopo/config.json")
        rutaSalidaSpyder = theSpyder.launch()
        procesador = Preprocesator(rutaSalidaSpyder+"onLine/", configuracion.getRutaSalidaPreProcesador())
        procesador.process()
        #print ("this is stdout")
        # def print_stderr(self):
       # sys.stderr.write("this is stderr\n")

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
