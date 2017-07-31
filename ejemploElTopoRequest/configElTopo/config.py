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
        self.Route = route

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

    def setRoute(self, route):
        self.Route = route

    def getRoute(self):
        return self.Route

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def writeFileJSON(self,file):
        outfile = open(file, 'w')
        outfile.write(self.toJSON())
        outfile.close()

