from tkinter import *
from configElTopo.config import config
from preProcesador.preProcesator import Preprocesator
from spyder.spyder import spyder


class VentanaCrawler():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Crawler Local')
        self.ventana.resizable(0, 0)
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
        print("Iniciando el crawler...")
        configuracion = config("./configElTopo/config.json")
        theSpyder = spyder(rutaConfig="./configElTopo/config.json")
        rutaSalidaSpyder = theSpyder.launch()
        print("\n\n")
        procesador = Preprocesator(rutaSalidaSpyder + "onLine/", configuracion.getRutaSalidaPreProcesador())
        procesador.process()
        # print ("this is stdout")
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

    def flush(self):
        pass
