import json


class lecturaFicheroUrlOnion:
    def leerDireccionesOnionJSON(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['url']

    def leerDireccionesOnionDiccionario(ruta):
        direcciones = []
        infile = open(ruta, 'r')
        for line in infile:
            line = line.replace("\n", "")
            direcciones.append(line)
        infile.close()
        return direcciones
