from tkinter import *
from tkinter import ttk,font
from configElTopo.config import config



class VentanaConfig():
    def __init__(self):
        self.rutaConfig= "./configElTopo/config.json"
        self.configuracion = config(route=self.rutaConfig)


        self.ventana = Tk()
        self.ventana.title('Configuracion')




        self.marco = ttk.Frame(self.ventana, borderwidth=2)
        self.marco.grid(row=0,column=0)


        # row 1 : Primera fila
        self.LBLRutaSalida = ttk.Label(self.marco,text="Ruta de salida:")
        self.LBLRutaSalida.grid(row=0,column=0,sticky=W)
        rutaS_str = self.configuracion.getRutaSalida()
        self.TXTRutaSalida = ttk.Entry(self.marco,width=30)
        self.TXTRutaSalida.insert(0,rutaS_str)
        #TXTRutaSalida.pack()
        self.TXTRutaSalida.grid(row=0,column=1)


        #row 2 : Segunda fila
        self.LBLRutaDiccionario = ttk.Label(self.marco,text="Ruta diccionario:")
        self.LBLRutaDiccionario.grid(row=1,column=0,sticky=W)
        rutaD_str = self.configuracion.getUsarDiccionario()
        self.TXTRutaDiccionario = ttk.Entry(self.marco,width=30)
        self.TXTRutaDiccionario.insert(0,rutaD_str)
        self.TXTRutaDiccionario.grid(row=1,column=1)

        #row 3 : Tercera fila
        self.LBLMaxDepth = ttk.Label(self.marco,text="Maxdepth:")
        self.LBLMaxDepth.grid(row=2,column=0,sticky=W)
        maxD_str = self.configuracion.getMaxDepth()
        self.TXTMaxDepth = ttk.Entry(self.marco,width=30)
        self.TXTMaxDepth.insert(0,maxD_str)
        self.TXTMaxDepth.grid(row=2,column=1)

        self.LBLUsarDic = ttk.Label(self.marco,text="Usar Diccionario:")
        self.LBLUsarDic.grid(row=3,column=0,sticky=W)
        usarD_str = self.configuracion.getUsarDiccionario()
        self.TXTUsarDic = ttk.Entry(self.marco,width=30)
        self.TXTUsarDic.insert(0,usarD_str)
        self.TXTUsarDic.grid(row=3,column=1)

        #row 5 :
        self.LBLUsarTor = ttk.Label(self.marco,text="Usar Tor:")
        self.LBLUsarTor.grid(row=4,column=0,sticky=W)
        usarT_str = self.configuracion.getUsarSiempreTor()
        self.TXTUsarTor = ttk.Entry(self.marco,width=30)
        self.TXTUsarTor.insert(0,usarT_str)
        self.TXTUsarTor.grid(row=4,column=1)

        #row 6 : Tercera fila
        self.LBLRenovarC= ttk.Label(self.marco,text="Renovar circuito siempre:")
        self.LBLRenovarC.grid(row=5,column=0,sticky=W)
        renovarC_str = self.configuracion.getRenovarSiempreCircuitoTor()
        self.TXTRenovarC = ttk.Entry(self.marco,width=30)
        self.TXTRenovarC.insert(0,renovarC_str)
        self.TXTRenovarC.grid(row=5,column=1)

        #row 7 : Tercera fila
        self.LBLDelaysC = ttk.Label(self.marco,text="Delays renovacion circuito:")
        self.LBLDelaysC.grid(row=6,column=0,sticky=W)
        delaysC_str = self.configuracion.getDelayIntentoRenovacionCircuitoTor()
        self.TXTDelaysC = ttk.Entry(self.marco,width=30)
        self.TXTDelaysC.insert(0,delaysC_str)
        self.TXTDelaysC.grid(row=6,column=1)

        self.separador1= ttk.Separator(self.marco,orient=HORIZONTAL)
        self.separador1.grid(row=8,column=0)


        self.BTN1 = ttk.Button(self.marco,text="Aceptar",command=quit)
        self.BTN1.grid(row=9,column=0)










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


