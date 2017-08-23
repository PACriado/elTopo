from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from Entidades.webPageInfo import webPageInfo


class Preprocesator:
    ##"/home/usertfm/SalidaJSON/1501436636356/onLine/"
    def __init__(self, Path, FinalPath):
        self.path = Path
        self.outputWPInfo = []
        self.finalPath = FinalPath
        self.finalArray = []

    def process(self):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        for webPageInfoObject in allObjects:
            self.splitter(webPageInfoObject)

        '''
        HAY QUE JUNTAR LOS ARRAYS allObject y self.outputWPInfo.
        lo primero que hay que hacer es crear un array final, que sera donde se junten los 2 arrays.
        añadir a este array final unicamente un objeto por cada dominio. (usa el getDomain() que he creado para los webPageInfos)
        si se encuentra otro objeto con el mismo dominio que uno que ya se ha insertado, añadirle como hijo del objeto existente que tiene el mismo dominio.

        Esta operacion hay que hacerla tambien con el array self.outputWPInfo.

        luego solo hay que recorrer el array final que tienes que crear, y crear los ficheros tal y como tienes abajo.

        '''
        self.mergeLists(allObjects)
        self.mergeLists(self.outputWPInfo)
        ##PRUEBA
        for webPageInfoObject in self.finalArray:
            hostname = webPageInfoObject.getDomain()
            path = self.finalPath + hostname + ".json"
            print("DOMINIO: " + hostname + " FICHERO: " + path)
            self.writeFile(path, webPageInfoObject)

        '''for element in self.outputWPInfo:
            hostname = element.getDomain()
            path = self.finalPath + hostname + ".json"
            print("DOMINIO: " + hostname + " FICHERO: "+ path)
            self.writeFile(path, element)'''
        ##FIN PRUEBA

    ##Metodo para escribir los json con la informacion necesaria
    def writeFile(self, finalPath, element):
        file = open(finalPath, "w")
        file.write(element.toJSON())
        file.close()

    ##Metodo para dividir y clasificar en diferentes json, dependiendo del dominio
    def splitter(self, WebPageInfoObject):
        currentDomain = WebPageInfoObject.getDomain()

        if (not WebPageInfoObject.getChildren()):
            # print(WebPageInfoObject.getUrl() + " No tiene hijos")
            pass
        else:
            # print(WebPageInfoObject.getUrl() + " Tiene hijos")
            indicesEliminar = []
            arrayChildrens = WebPageInfoObject.getChildren()
            for i in range(0, len(arrayChildrens)):
                elementChildWPInfo = webPageInfo(dictionary=arrayChildrens[i])
                elementChildDomain = elementChildWPInfo.getDomain()
                if (elementChildDomain == currentDomain):
                    # print("Dominios iguales hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    ##recursiva a splitter
                    self.splitter(elementChildWPInfo)
                else:
                    # print("Dominios diferentes hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    indicesEliminar.append(i)
                    self.splitter(elementChildWPInfo)
            ##quitar el elemento child de la lista getCHildren que recorremos, meterle a la lista final dicho objeto,
            # print("***** Eliminar los indices"+str(indicesEliminar))
            # Recorremos los indices al reves(Damos la vuelta al array), para no salirnos del array segun eliminamos elementos
            indicesEliminar = indicesEliminar[::-1]
            for i in range(0, len(indicesEliminar)):
                eliminarEsteIndice = indicesEliminar[i]
                elementoHijoAPadre = WebPageInfoObject.getChildren().pop(eliminarEsteIndice)
                self.outputWPInfo.append(webPageInfo(dictionary=elementoHijoAPadre))

    def mergeLists(self, allObjects):
        existe = False
        padre = None
        for wpiObject in allObjects:
            if not self.finalArray:
                self.finalArray.append(wpiObject)
            else:
                for existObject in self.finalArray:
                    if wpiObject.getDomain() == existObject.getDomain():
                        existe = True
                        padre = existObject
                        # print("DOMINIO YA EXISTE")
                        break
                    else:
                        existe = False
                        # print("DOminio no existe")

                if (existe):
                    padre.getChildren().append(wpiObject)
                else:
                    self.finalArray.append(wpiObject)
