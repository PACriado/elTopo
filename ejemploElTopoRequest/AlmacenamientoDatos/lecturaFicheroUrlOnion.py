import json


class lecturaFicheroUrlOnion:
    def leerDireccionesOnionJSON(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['url']

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



    def leerDireccionesOnionDiccionario(ruta):
        direcciones = []
        infile = open(ruta, 'r')
        for line in infile:
            line = line.replace("\n", "")
            direcciones.append(line)
        infile.close()
        return direcciones
