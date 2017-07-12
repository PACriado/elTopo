import json


class lecturaFicheroConfig:
    def leerRutaSalida(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['RutaSalida']

    def leerRutaDiccionario(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['RutaDiccionario']

    def leerMaxDepth(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['MaxDepth']

    def leerUsarDiccionario(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['UsarDiccionario']

    def leerSiempreTor(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['UsarSiempreTor']

    def leerRenovarSiempreCircuitoTor(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['RenovarSiempreCircuitoTor']

    def leerDelayIntentoRenovacionCircuitoTor(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['DelayIntentoRenovacionCircuitoTor']



