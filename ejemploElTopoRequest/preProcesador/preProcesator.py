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
        self.copyList = []

    ##estan llamados asi porque son pruebas
    def metodo(self, WebPageInfo):
        for i in WebPageInfo.getChildren():
             elementChildWPInfo = webPageInfo(dictionary=i)
             self.outputWPInfo.append(elementChildWPInfo)
    ##llamado asi porque es una prueba
    def metodo2(self):
        for elementCopy in self.copyList:
            self.outputWPInfo.append(elementCopy)

    ##borrar son pruebas
    def metodo3(self):
        for e in self.copyList:
            self.outputWPInfo.pop()
            index = self.outputWPInfo.index(e)
            self.copyList.pop(index)

    def process(self):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        for webPageInfoObject in allObjects:
            resultList = self.splitter(webPageInfoObject)
            ##self.metodo(webPageInfoObject)
            ##self.metodo2()
            self.metodo3()
        for element in self.outputWPInfo:
            domain = element.getUrl()
            hostname = urlparse(domain).hostname.split(".")
            hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
            path = self.finalPath + hostname + ".json"
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


            for elementChild in WebPageInfoObject.getChildren():
                elementChildWPInfo = webPageInfo(dictionary=elementChild)
                childUrl = elementChildWPInfo.getUrl()
                self.outputWPInfo.append(elementChildWPInfo)
                elementChildDomain = urlparse(childUrl).hostname.split(".")
                elementChildDomain = ".".join(len(elementChildDomain[-2]) < 4 and elementChildDomain[-3:] or elementChildDomain[-2:])
                if (elementChildDomain == currentDomain):
                    print("Dominios iguales hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    ##recursiva a splitter
                    self.splitter(elementChildWPInfo)
                else:
                    print("Dominios diferentes hijo: " + elementChildDomain + " Padre: " + currentDomain)
                    ##quitar el elemento child de la lista getCHildren que recorremos, meterle a la lista final dicho objeto,
                    self.copyList.append(elementChildWPInfo)


