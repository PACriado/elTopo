import json

class lecturaFicheroUrlOnion:

    def leerDireccionesOnion(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero[0]['url']
