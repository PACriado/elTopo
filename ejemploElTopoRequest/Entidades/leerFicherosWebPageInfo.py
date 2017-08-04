import glob
from Entidades.webPageInfo import webPageInfo
class leerFicherosWebPageInfo:


    def readAllFilesInDirectory(route):
        print(route)
        arrayWebPageInfos = []
        ficheros = glob.glob(route + "*.json")
        for webPageInfoFile in ficheros:
            webPageInfoObject = webPageInfo(route=webPageInfoFile)
            arrayWebPageInfos.append(webPageInfoObject)
        return arrayWebPageInfos
