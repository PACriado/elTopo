from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.classificator import classificator
from Entidades.webPageInfo import webPageInfo
from urllib.parse import urlparse
import os
import re
import time


class Preprocesator:
    ##"/home/usertfm/SalidaJSON/1501436636356/onLine/"
    def __init__(self, Path, FinalPath):
        self.path = Path
        self.outputWPInfo = []
        self.finalPath = FinalPath


    def process(self):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        for webPageInfoObject in allObjects:
            resultList = self.splitter(webPageInfoObject)

        for element in self.outputWPInfo:
            domain = element.getUrl()
            hostname = urlparse(domain).hostname.split(".")
            hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
            path = self.finalPath + hostname + ".json"
            print("DOMINIO: " + hostname + " FICHERO: "+ path)
            self.writeFile(path, element)

    ##Metodo para escribir los json con la informacion necesaria
    def writeFile(self,finalPath, element):
        file = open(finalPath,"w")
        file.write(element.toJSON())
        file.close()

    ##Metodo para dividir y clasificar en diferentes json, dependiendo del dominio
    def splitter(self, WebPageInfoObject):
        currentUrl = WebPageInfoObject.getUrl()
        currentDomain = urlparse(currentUrl).hostname.split(".")
        currentDomain = ".".join(len(currentDomain[-2]) < 4 and currentDomain[-3:] or currentDomain[-2:])

        if (not WebPageInfoObject.getChildren()) :
            print(WebPageInfoObject.getUrl() + " No tiene hijos")

        else:
            print(WebPageInfoObject.getUrl() + " Tiene hijos")
            indicesEliminar = []
            arrayChildrens = WebPageInfoObject.getChildren()
            for i in range(0,len(arrayChildrens)):
                elementChildWPInfo = webPageInfo(dictionary=arrayChildrens[i])
                childUrl = elementChildWPInfo.getUrl()
                elementChildDomain = urlparse(childUrl).hostname.split(".")
                elementChildDomain = ".".join(len(elementChildDomain[-2]) < 4 and elementChildDomain[-3:] or elementChildDomain[-2:])
                if (elementChildDomain == currentDomain):
                    print("Dominios iguales hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    ##recursiva a splitter
                    self.splitter(elementChildWPInfo)
                else:
                    print("Dominios diferentes hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    indicesEliminar.append(i)
            ##quitar el elemento child de la lista getCHildren que recorremos, meterle a la lista final dicho objeto,
            #print("***** Eliminar los indices"+str(indicesEliminar))
            #Recorremos los indices al reves(Damos la vuelta al array), para no salirnos del array segun eliminamos elementos
            indicesEliminar = indicesEliminar[::-1]
            for i in range(0,len(indicesEliminar)):
                eliminarEsteIndice = indicesEliminar[i]
                elementoHijoAPadre = WebPageInfoObject.getChildren().pop(eliminarEsteIndice)
                self.outputWPInfo.append(webPageInfo(dictionary=elementoHijoAPadre))


        '''
        webPageInfoObjectInArray = WebPageInfoObject
        domain = webPageInfoObjectInArray.getUrl()
        hostname = urlparse(domain).hostname.split(".")
        hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
        ##Si el webpage tiene hijos comprobamos el dominio de cada uno, si es el mismo lo dejamos en el json del padre, si es distinto creamos uno nuevo
        if webPageInfoObjectInArray.getChildren() is not None:
            print(hostname)
            ##if any(hostname in s for s in self.mDomains):
            if hostname in self.outputWPInfo:
                print(hostname)
                path = self.finalPath + hostname + ".json"
                with open(path,'wb') as file:
                    file.write(webPageInfoObjectInArray.toJSON())
                    file.close()
            else:
                self.outputWPInfo.append(webPageInfoObjectInArray)

            for children in WebPageInfoObject.getChildren():
                wpInfo = webPageInfo(dictionary=children)
                self.splitter(wpInfo)
        return self.outputWPInfo
        '''
        ##child = webPageInfo(children)
        ##print(child.toJSON())
        ##child= webPageInfo(child.toJSON())
