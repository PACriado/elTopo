from tkinter import *
from tkinter import ttk
from configElTopo.config import config
from tkinter.scrolledtext import ScrolledText


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
        rutaD_str = self.configuracion.getRutaDiccionario()
        self.TXTRutaDiccionario = ttk.Entry(self.marco,width=30)
        self.TXTRutaDiccionario.insert(0,rutaD_str)
        self.TXTRutaDiccionario.grid(row=1,column=1)

        #row 3 : Tercera fila
        self.LBLMaxDepth = ttk.Label(self.marco,text="Maxdepth:")
        self.LBLMaxDepth.grid(row=2,column=0,sticky=W)
        maxD_str = self.configuracion.getMaxDepth()


        self.SBOXMaxDepth = Spinbox(self.marco, from_=1, to=10)

        self.SBOXMaxDepth.grid(row=2,column=1,sticky=W)


        #row 4 BOOL
        self.LBLUsarDic = ttk.Label(self.marco,text="Usar Diccionario:")
        self.LBLUsarDic.grid(row=3,column=0,sticky=W)
        #usarD_str = self.configuracion.getUsarDiccionario()
        #self.TXTUsarDic = ttk.Entry(self.marco,width=30)
        #self.TXTUsarDic.insert(0,usarD_str)
        self.usarD_str=self.configuracion.getUsarDiccionario()

        #print(self.usarD_str)
        #print(int(self.usarD_str))


        self.value=StringVar(self.marco,self.usarD_str)
        self.CMBUsarDic = ttk.Combobox(self.marco,textvariable=self.value,state ='readonly')
        self.CMBUsarDic['values'] = ['False', 'True']
        self.CMBUsarDic.current(int(self.usarD_str))
        self.CMBUsarDic.grid(row=3,column=1,sticky=W)


        #self.checkbox_value = BooleanVar(self)

        #prueba=int(self.var=='True')

        #self.chk1 = Checkbutton(self.marco,variable=prueba)
        #self.chk1.grid(row=3,column=1,sticky=W)


        #self.TXTUsarDic.grid(row=3,column=1)

        #row 5 BOOL
        self.LBLUsarTor = ttk.Label(self.marco,text="Usar Tor:")
        self.LBLUsarTor.grid(row=4,column=0,sticky=W)
        self.usarT_str= self.configuracion.getUsarSiempreTor()


        # self.chk2 = Checkbutton(self.marco,variable=self.usarT_str)

        self.value2=StringVar(self.marco,self.usarT_str)

        self.CMBUsarTor = ttk.Combobox(self.marco,textvariable=self.value2,state ='readonly')
        self.CMBUsarTor['values'] = ['False', 'True']
        self.CMBUsarTor.current(int(self.usarT_str))
        self.CMBUsarTor.grid(row=4,column=1,sticky=W)


        #self.chk2.grid(row=4,column=1,sticky=W)

        #self.TXTUsarTor = ttk.Entry(self.marco,width=30)
        #self.TXTUsarTor.insert(0,usarT_str)
        #self.TXTUsarTor.grid(row=4,column=1)

        #row 6 BOOL
        self.LBLRenovarC= ttk.Label(self.marco,text="Renovar circuito siempre:")
        self.LBLRenovarC.grid(row=5,column=0,sticky=W)
        #renovarC_str = self.configuracion.getRenovarSiempreCircuitoTor()
        self.renovarC_str= self.configuracion.getRenovarSiempreCircuitoTor()


        self.value3=StringVar(self.marco,self.renovarC_str)

        self.CMBRenovarC = ttk.Combobox(self.marco,textvariable=self.value3,state ='readonly')
        self.CMBRenovarC['values'] = ['False', 'True']
        self.CMBRenovarC.current(int(self.renovarC_str))
        self.CMBRenovarC.grid(row=5,column=1,sticky=W)


        #self.chk3 = Checkbutton(self.marco,variable=self.renovarC_str)
        #self.chk3.grid(row=5,column=1,sticky=W)
        #self.TXTRenovarC = ttk.Entry(self.marco,width=30)
        #self.TXTRenovarC.insert(0,renovarC_str)
        #self.TXTRenovarC.grid(row=5,column=1)

        #row 7 : Tercera fila
        self.LBLDelaysC = ttk.Label(self.marco,text="Delays renovacion circuito:")
        self.LBLDelaysC.grid(row=6,column=0,sticky=W)
        delaysC_str = self.configuracion.getDelayIntentoRenovacionCircuitoTor()
        #self.TXTDelaysC = ttk.Entry(self.marco,width=30)
        #self.TXTDelaysC.insert(0,delaysC_str)

        self.TXTDelaysC = Scale(self.marco, from_=10, to=200, orient=HORIZONTAL)
        self.TXTDelaysC.grid(row=6,column=1,sticky=W)

        self.separador1= ttk.Separator(self.marco,orient=HORIZONTAL)
        self.separador1.grid(row=8,column=0)


        self.BTNGuardar = ttk.Button(self.marco,text="Guardar",command=self.salvarCambios)
        self.BTNGuardar.grid(row=10,column=0)


        # row 1 : Primera fila
        self.LBLURLs = ttk.Label(self.marco,text="Urls:")
        self.LBLURLs.grid(row=9,column=0,sticky=W)
        urls_str = self.configuracion.geturl()
        self.TXTURLs = ScrolledText(self.marco,width=30)
        for url in urls_str:
            self.TXTURLs.insert(INSERT,url+"\n")
        #TXTRutaSalida.pack()
        self.TXTURLs.grid(row=9,column=1)


        #self.BTNGuardar = ttk.Button(self.ventana, text = 'Guardar', command = self.guardarConfig)
        #self.BTNGuardar.pack(side = LEFT)

        #self.BTNSalir =ttk.Button(self.ventana, text='Salir',command=self.ventana.destroy)
        #self.BTNSalir.pack(side=RIGHT)

        #Resaltamos el borde del botoninfo
        #self.BTNGuardar.focus_set()
        self.ventana.mainloop()


        #def guardarConfig(self):
        #Borrar contenido de la caja de texto
        #self.TXTRutaSalida.delete("1.0",END)

        #Contruimos una cadena de texto con toda la info y la insertamos en la cadena de texto creada

        #configuracion = config ()
        #info = configuracion.toJSON()
        #self.TXTRutaSalida.insert("1.0",info)
    def salvarCambios(self):
        self.configuracion.setRutaSalida(self.TXTRutaSalida.get())
        self.configuracion.setRutaDiccionario(self.TXTRutaDiccionario.get())
        if(self.CMBUsarDic.get()=='False'):
            varUsarDict = False
        else:
            varUsarDict = True
        self.configuracion.setUsarDiccionario(varUsarDict)

        if(self.CMBUsarTor.get()=='False'):
            varUsarTor = False
        else:
            varUsarTor = True
        self.configuracion.setUsarSiempreTor(varUsarTor)

        if(self.CMBRenovarC.get()=='False'):
            varRenovarTor = False
        else:
            varRenovarTor = True

        self.configuracion.setRenovarSiempreCircuitoTor(varRenovarTor)
        self.configuracion.setMaxDepth(int(self.SBOXMaxDepth.get()))
        self.configuracion.setDelayIntentoRenovacionCircuitoTor(self.TXTDelaysC.get())

        allURLs = self.TXTURLs.get(1.0, END)
        arrayURLS = [i.strip() for i in allURLs.splitlines()]
        arrayURLS.remove('')
        self.configuracion.seturl(arrayURLS)

        self.configuracion.writeFileJSON(self.configuracion.getRoute())

        self.ventana.destroy()

