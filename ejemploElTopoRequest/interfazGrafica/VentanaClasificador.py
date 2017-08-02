from tkinter import *
from tkinter import ttk
from spyder.spyder import spyder
import os
import sys
from tkinter.filedialog import askdirectory




class VentanaClasificador():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title('Crawler')
        self.toolbar = Frame(self.ventana)
        self.toolbar.pack(side="top", fill="x")


        b1 = Button(self.ventana, text="Iniciar", command=self.print_stdout)


        b2 = Button(self.ventana, text="Abrir directorio",command=self.ruta_text)
        self.url = Entry(self.ventana,width = 80)




        b1.pack(in_=self.toolbar, side="left")
        b2.pack(in_=self.toolbar, side="left")
        self.url.pack(in_=self.toolbar,side = "left")

        self.text = Text(self.ventana, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text, "stdout")
       # sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):
        theSpyder = spyder(rutaConfig= "./configElTopo/config.json")
        theSpyder.launch()
        #print ("this is stdout")

    def ruta_text(self):

        result = askdirectory()
        self.url.delete(0,'end')
        self.url.insert(0,result)
        self.url.pack(in_=self.toolbar,side = "left")


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
