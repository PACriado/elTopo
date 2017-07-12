import json


class lecturaFicherosURL:
    def leerDireccionesJSON(ruta):
        fichero = json.loads(open(ruta).read())
        return fichero['url']

    def leerDireccionesDiccionario(ruta):
        direcciones = []
        infile = open(ruta, 'r')
        for line in infile:
            line = line.replace("\n", "")
            direcciones.append(line)
        infile.close()
        return direcciones
