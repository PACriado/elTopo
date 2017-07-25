from tkinter import *
from tkinter import ttk
from configElTopo.config import config

class VentanaConfig():
    def __init__(self):
        self.rutaConfig= "./configElTopo/config.json"
        self.configuracion = config(route=self.rutaConfig)

        self.ventana = Tk()
        self.ventana.geometry('300x200')
        self.ventana.title('Configuracion')
        #Creamos una caja de texto
        self.TXTRutaSalida = Text(self.ventana, width=40, height = 1)
        self.TXTRutaSalida.pack(side=TOP)
        #Cargamos los datos de la configuracion
        self.TXTRutaSalida.insert("1.0",self.configuracion.getRutaSalida())


        self.BTNGuardar = ttk.Button(self.ventana, text = 'Guardar', command = self.guardarConfig)
        self.BTNGuardar.pack(side = LEFT)

        self.BTNSalir =ttk.Button(self.ventana, text='Salir',command=self.ventana.destroy)
        self.BTNSalir.pack(side=RIGHT)

        #Resaltamos el borde del botoninfo
        self.BTNGuardar.focus_set()
        self.ventana.mainloop()



    def guardarConfig(self):
        #Borrar contenido de la caja de texto
        self.TXTRutaSalida.delete("1.0",END)

        #Contruimos una cadena de texto con toda la info y la insertamos en la cadena de texto creada

        configuracion = config ()
        info = configuracion.toJSON()
        self.TXTRutaSalida.insert("1.0",info)


