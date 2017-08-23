from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from configElTopo.config import config


class VentanaConfigCrawler():
    def __init__(self):
        self.rutaConfig = "./configElTopo/config.json"
        self.configuracion = config(route=self.rutaConfig)

        self.ventana = Tk()
        self.ventana.title('Configuracion Crawler Remoto')

        self.marco = ttk.Frame(self.ventana, borderwidth=2)
        self.marco.grid(row=0, column=0)

        self.LBLURLs = ttk.Label(self.marco, text="Urls:")
        self.LBLURLs.grid(row=0, column=0, sticky=W)

        self.TXTURLs = ScrolledText(self.marco, width=30)
        self.leerDatos()

        self.BTNGuardar = ttk.Button(self.marco, text="Guardar", command=self.guardarCambios)
        self.BTNGuardar.grid(row=2, column=0)

        self.ventana.mainloop()

    def leerDatos(self):
        infile = open(self.configuracion.getRutaServidoresSpyderRest(), 'r')

        for line in infile:
            print(line)
            self.TXTURLs.insert(INSERT, line)
            self.TXTURLs.grid(row=0, column=1)

            # Cerramos el fichero.
        infile.close()

    def guardarCambios(self):
        outfile = open(self.configuracion.getRutaServidoresSpyderRest(),
                       'w')  # Indicamos el valor 'w' para sobreescribir
        allURLs = self.TXTURLs.get(1.0, END)
        outfile.write(allURLs.rstrip())
        outfile.close()
        self.ventana.destroy()
