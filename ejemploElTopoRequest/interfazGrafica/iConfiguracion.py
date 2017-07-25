from tkinter import *
from tkinter import ttk
from configElTopo.config import config

class Ventana():
    def __init__(self):
        self.rutaConfig= "./configElTopo/config.json"
        self.configuracion = config(route=self.rutaConfig)

        self.ventana = Tk()
        self.ventana.geometry('300x200')
        self.ventana.title('Prueba3')
        #Creamos una caja de texto
        self.tinfo = Text(self.ventana, width=40, height = 10)
        self.tinfo.pack(side=TOP)
        self.botoninfo = ttk.Button(self.ventana, text = 'Info', command = self.verinfo)
        self.botoninfo.pack(side = LEFT)
        self.botonsalir =ttk.Button(self.ventana, text='Salir',command=self.ventana.destroy)
        self.botonsalir.pack(side=RIGHT)
        #Resaltamos el borde del botoninfo
        self.botoninfo.focus_set()
        self.ventana.mainloop()


    def verinfo(self):
        #Borrar contenido de la caja de texto
        self.tinfo.delete("1.0",END)

        #Contruimos una cadena de texto con toda la info y la insertamos en la cadena de texto creada

        configuracion = config ()
        info = configuracion.toJSON()
        self.tinfo.insert("1.0",info)


