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
