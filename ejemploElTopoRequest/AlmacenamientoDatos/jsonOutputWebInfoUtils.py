import time
import re
import os

class jsonOutputWebInfoUtils:
    def __init__(self, baseDirectory):
        millis = int(round(time.time() * 1000))
        self.baseDirectory = baseDirectory  + str(millis)+ "/"

    def escribirJsonContenidoWeb(self,contenido,fileName, format):
        if not os.path.exists(self.baseDirectory): os.makedirs(self.baseDirectory)#con esto nos aseguramos que la ruta donde guardamos los datos existe
        outfile = open(self.baseDirectory+ self.nombreFichero(fileName)+format, 'w')
        outfile.write(contenido)
        outfile.close()

    def nombreFichero(self, fileName):
        millis = int(round(time.time() * 1000))
        patron = re.compile("\W")
        nombreSinCaracteresNoAlfanumericos = patron.sub("", fileName)
        nombreConTimeStamp = str(millis)+"-"+nombreSinCaracteresNoAlfanumericos
        return nombreConTimeStamp
