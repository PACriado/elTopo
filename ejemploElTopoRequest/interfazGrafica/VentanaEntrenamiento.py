from tkinter import *
from tkinter import ttk
from spyder.spyder import spyder
import os
import sys
from tkinter.filedialog import askdirectory


class VentanaEntrenamiento():

    def __init__(self):

        self.ventanaE = Tk()
        self.ventanaE.title('Entrenamiento')
        self.toolbar = Frame(self.ventanaE)
        self.toolbar.pack(side="top", fill="x")


        BTN_Iniciar = Button(self.ventanaE, text="Iniciar", command=self.print_stdout)


        BTN_Abrirdir = Button(self.ventanaE, text="Abrir directorio",command=self.ruta_text)
        self.url = Entry(self.ventanaE,width = 80)




        BTN_Iniciar.pack(in_=self.toolbar, side="left")
        BTN_Abrirdir.pack(in_=self.toolbar, side="left")
        self.url.pack(in_=self.toolbar,side = "left")

        self.text = Text(self.ventanaE, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")

    def print_stdout(self):
        theSpyder = spyder(rutaConfig= "./configElTopo/config.json")
        theSpyder.launch()
        #print ("this is stdout")

    def ruta_text(self):

        result = askdirectory()
        self.url.delete(0,'end')
        self.url.insert(0,result)
        self.url.pack(in_=self.toolbar,side = "left")




class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
