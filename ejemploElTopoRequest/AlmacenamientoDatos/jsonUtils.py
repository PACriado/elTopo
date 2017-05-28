

class jsonUtil:
    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory

    def escribirJson(self,contenido,fileName, format):
        outfile = open(self.baseDirectory+ fileName+format, 'w')
        outfile.write(contenido)
        outfile.close()

