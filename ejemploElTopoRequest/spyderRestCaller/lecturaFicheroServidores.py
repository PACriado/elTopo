import json


class lecturaFicheroServidores:
    def leerDireccionesDiccionario(ruta):
        direcciones = []
        infile = open(ruta, 'r')
        for line in infile:
            line = line.replace("\n", "")
            direcciones.append(line)
        infile.close()
        return direcciones
