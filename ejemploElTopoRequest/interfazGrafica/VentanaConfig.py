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

        # row 1 : Primera fila
        self.LBLRutaSalida = Label(self.ventana,text="Ruta de salida :")
        self.LBLRutaSalida.grid(row=1,column=1,sticky=W)
        rutaS_str = self.configuracion.getRutaSalida()
        TXTRutaSalida = Entry(self.ventana)
        TXTRutaSalida.insert(0,rutaS_str)
        #TXTRutaSalida.pack()
        TXTRutaSalida.grid(row=1,column=2)


        #row 2 : Segunda fila
        self.LBLRutaDiccionario = Label(self.ventana,text="Ruta diccionario :")
        self.LBLRutaDiccionario.grid(row=2,column=1,sticky=W)
        rutaD_str = self.configuracion.getUsarDiccionario()
        TXTRutaDiccionario = Entry(self.ventana)
        TXTRutaDiccionario.insert(0,rutaD_str)
        TXTRutaDiccionario.grid(row=2,column=2)

        #row 3 : Tercera fila
        self.LBLMaxDepth = Label(self.ventana,text="Maxdepth :")
        self.LBLMaxDepth.grid(row=3,column=1,sticky=W)
        maxD_str = self.configuracion.getMaxDepth()
        TXTMaxDepth = Entry(self.ventana)
        TXTMaxDepth.insert(0,maxD_str)
        TXTMaxDepth.grid(row=3,column=2)

        self.LBLUsarDic = Label(self.ventana,text="Usar Diccionario :")
        self.LBLUsarDic.grid(row=4,column=1,sticky=W)
        usarD_str = self.configuracion.getUsarDiccionario()
        TXTUsarDic = Entry(self.ventana)
        TXTUsarDic.insert(0,usarD_str)
        TXTUsarDic.grid(row=4,column=2)

        #row 5 :
        self.LBLUsarTor = Label(self.ventana,text="Usar Tor :")
        self.LBLUsarTor.grid(row=5,column=1,sticky=W)
        usarT_str = self.configuracion.getUsarSiempreTor()
        TXTUsarTor = Entry(self.ventana)
        TXTUsarTor.insert(0,usarT_str)
        TXTUsarTor.grid(row=5,column=2)

        #row 6 : Tercera fila
        self.LBLRenovarC= Label(self.ventana,text="Renovar circuito siempre :")
        self.LBLRenovarC.grid(row=6,column=1,sticky=W)
        renovarC_str = self.configuracion.getRenovarSiempreCircuitoTor()
        TXTRenovarC = Entry(self.ventana)
        TXTRenovarC.insert(0,renovarC_str)
        TXTRenovarC.grid(row=6,column=2)

        #row 7 : Tercera fila
        self.LBLDelaysC = Label(self.ventana,text="Delays renovacion circuito :")
        self.LBLDelaysC.grid(row=7,column=1,sticky=W)
        delaysC_str = self.configuracion.getDelayIntentoRenovacionCircuitoTor()
        TXTDelaysC = Entry(self.ventana)
        TXTDelaysC.insert(0,delaysC_str)
        TXTDelaysC.grid(row=7,column=2)



        self.finish = Button(self.ventana,text="finalizar",command=self.ventana.quit)
        self.finish.grid(row=9,column=2)





        #Creamos una caja de texto
      #  self.TXTRutaSalida = Text(self.ventana, width=40, height = 1)
      #  self.TXTRutaSalida.pack(side=TOP)
        #Cargamos los datos de la configuracion
      #  self.TXTRutaSalida.insert("1.0",self.configuracion.getRutaSalida())

      #  self.LBLRutaSalida = Tk.Label(self.ventana, text="Ruta de salida", width=30)








       # self.BTNGuardar = ttk.Button(self.ventana, text = 'Guardar', command = self.guardarConfig)
       # self.BTNGuardar.pack(side = LEFT)

     #   self.BTNSalir =ttk.Button(self.ventana, text='Salir',command=self.ventana.destroy)
     #   self.BTNSalir.pack(side=RIGHT)

        #Resaltamos el borde del botoninfo
     #   self.BTNGuardar.focus_set()
        self.ventana.mainloop()



 #   def guardarConfig(self):
        #Borrar contenido de la caja de texto
      #  self.TXTRutaSalida.delete("1.0",END)

        #Contruimos una cadena de texto con toda la info y la insertamos en la cadena de texto creada

      #  configuracion = config ()
    # info = configuracion.toJSON()
    #    self.TXTRutaSalida.insert("1.0",info)


