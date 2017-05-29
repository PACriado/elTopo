import time
import re

class jsonUtil:
    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory

    def escribirJson(self,contenido,fileName, format):
        outfile = open(self.baseDirectory+ self.nombreFichero(fileName)+format, 'w')
        outfile.write(contenido)
        outfile.close()

    def nombreFichero(self, fileName):
        millis = int(round(time.time() * 1000))
        patron = re.compile("\W")
        nombreSinCaracteresNoAlfanumericos = patron.sub("", fileName)
        nombreConTimeStamp = str(millis)+"-"+nombreSinCaracteresNoAlfanumericos
        return nombreConTimeStamp

