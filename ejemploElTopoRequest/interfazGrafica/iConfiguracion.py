from tkinter import *
from tkinter import ttk
import json


class config:

    def __init__(self, route=''):
        if route != '':
            #DE ESTA FORMA CARGAMOS UN JSON A ESTA CLASE
            with open(route) as json_data:
                self.__dict__ = json.load(json_data)
        else:
            self.RutaSalida =""
            self.RutaDiccionario=""
            self.MaxDepth=1
            self.UsarDiccionario= False
            self.UsarSiempreTor=False
            self.RenovarSiempreCircuitoTor=False
            self.DelayIntentoRenovacionCircuitoTor=2
            self.url=[]


    def setRutaSalida(self, rutaSalida):
        self.RutaSalida = rutaSalida

    def getRutaSalida(self):
        return self.RutaSalida

    def setRutaDiccionario(self, rutaDiccionario):
        self.RutaDiccionario = rutaDiccionario

    def getRutaDiccionario(self):
        return self.RutaDiccionario

    def setMaxDepth(self, maxDepth):
        self.MaxDepth = maxDepth

    def getMaxDepth(self):
        return self.MaxDepth

    def setUsarDiccionario(self, usarDiccionario):
        self.UsarDiccionario = usarDiccionario

    def getUsarDiccionario(self):
        return self.UsarDiccionario

    def setUsarSiempreTor(self, usarSiempreTor):
        self.UsarSiempreTor = usarSiempreTor

    def getUsarSiempreTor(self):
        return self.UsarSiempreTor

    def setRenovarSiempreCircuitoTor(self, renovarSiempreCircuitoTor):
        self.RenovarSiempreCircuitoTor = renovarSiempreCircuitoTor

    def getRenovarSiempreCircuitoTor(self):
        return self.RenovarSiempreCircuitoTor

    def setDelayIntentoRenovacionCircuitoTor(self, delayIntentoRenovacionCircuitoTor):
        self.DelayIntentoRenovacionCircuitoTor = delayIntentoRenovacionCircuitoTor

    def getDelayIntentoRenovacionCircuitoTor(self):
        return self.DelayIntentoRenovacionCircuitoTor

    def seturl(self, Url):
        self.url = Url

    def geturl(self):
        return self.url

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def writeFileJSON(self,file):
        outfile = open(file, 'w')
        outfile.write(self.toJSON())
        outfile.close()






class Ventana():
    def __init__(self):
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
        self.conf = config()
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







def main():
    app = Ventana()



if __name__ == '__main__':
    main()
