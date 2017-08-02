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
        self.mDomains = []
        self.finalPath = FinalPath

    def process(self):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        for webPageInfoObject in allObjects:
            resultList = self.splitter(webPageInfoObject)

        ##return resultList
        for element in resultList:
            print(element)
            domain = element.getUrl()
            hostname = urlparse(domain).hostname.split(".")
            hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
            path = self.finalPath + hostname + ".json"
            self.writeFile(path, element)

    def writeFile(self,finalPath, element):
        file = open(finalPath,"w")
        file.write(element.toJSON())
        file.close()

    def splitter(self, WebPageInfoObject):

        webPageInfoObjectInArray = WebPageInfoObject
        domain = webPageInfoObjectInArray.getUrl()
        hostname = urlparse(domain).hostname.split(".")
        hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])

        if webPageInfoObjectInArray.getChildren() is not None:
            if hostname in self.mDomains:
                print(hostname)
            else:
                ##self.mDomains.append(hostname)
                ##self.mDomains.append(webPageInfoObjectInArray.getUrl())
                self.mDomains.append(webPageInfoObjectInArray)
            for children in WebPageInfoObject.getChildren():
                wpInfo = webPageInfo(dictionary=children)
                ##while wpInfo.getChildren() is not None:
                print(wpInfo.getUrl())
                self.splitter(wpInfo)


        ##print(self.mDomains)
        return self.mDomains
        ##child = webPageInfo(children)
        ##print(child.toJSON())
        ##child= webPageInfo(child.toJSON())
