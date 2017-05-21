from lxml import html
from filtroInformacion.HttpCode import HttpCode
from filtroInformacion.HttpCodeException import HttpCodeException
from Entidades.webPageInfo import webPageInfo
import json

class filtroInformacion:

    def __init__(self, conexion, url):
       self.conexion = conexion
       self.url = url
       self.page = self.conexion.getRequestAuto(self.url)
       self.tree = html.fromstring(self.page.content)
       if self.page.status_code != HttpCode.OK.value:
          #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
          print("LA WEB NO RETORNA UN HTTP 200!")
          raise  HttpCodeException("NO HA SALTADO UN 200!")


    def getUrl(self):
        currentUrl = self.url
        return currentUrl

    def getTitle(self):
        title = self.tree.xpath('//title/text()')
        return title[0]

    def getLinksHref(self):
        linksHref = self.tree.xpath('//a/@href')
        #AQUI HAY QUE AÑADIR UNA COMPROBAR SI LOS LINKS SON RELATIVOS O ABSOLUTOS.
        #CASO 1
        #SI EL LINK ES ABSOLUTO, POR EJEMPLO LOS QUE TIENEN UNA URL TIPO HTTP://PATATA.COM/COMOMEGUSTALASPATATAS NO HAY QUE HACER NADA, LO DEJAMOS COMO ESTA
        #CASO 2
        #SI EL LINK ES RELATIVO, POR EJEMPLO /COMOMEGUSTANLASPATATAS HAY QUE AÑADIRLE EL DOMINIO AL INICIO
        #DE FORMA QUE SI EL SELF.URL ES HTTP://PATATA.COM NOSOTROS RETORNEMOS HTTP://PATATA.COM/COMOMEGUSTANLASPATATAS
        #HAY QUE COMPROBAR QUE SELF.URL NO TENGA LA BARRA AL FINAL, Y SI LA TIENE, NO TENEMOS QUE PONERLA 2 VECES
        #EJEMPLO SI VIENE EL SELF.URL HTTP://PATATA.COM/ NO LE PODEMOS CONCATENAR /COMOMEGUSTANLASPATATAS PORQUE TENDRIAMOS HTTP://PATATA.COM//COMOMEGUSTANLASPATATAS
        return linksHref

    def getLinksText(self):
        linksText = self.tree.xpath('//a/text()')
        return linksText

    def getAllDataObject(self):
        return webPageInfo(url=self.getUrl(),title=self.getTitle())

    def getAllDataJson(self):
        return json.dumps(self.getAllDataObject().__dict__,indent=4)

    def getAllDataRecursiveObject(self):
        currentWeb = webPageInfo(url=self.getUrl(),title=self.getTitle(),children=[])
        '''
        #CODIGO QUE FALTA POR PULIR PARA QUE FUNCIONE LA BUSQUEDA RECURSIVA
        allChildren = self.getLinksHref()
        allChildrenList = []
        for currentChildren in allChildren:
            currentURL = currentChildren
            newFilter = filtroInformacion(self.conexion,currentURL)
            currentTitle = newFilter.getTitle()
            newChildren = webPageInfo(url=currentURL, title=currentTitle)
            allChildrenList.append(newChildren)

        #currentWeb.setChildren(allChildrenList)
        '''
        return currentWeb

    def getAllDataRecursiveJson(self):
        #AQUI HAY QUE MIRAR PORQUE NO SERIALIZA A JSON UN OBJETO CON UNA LISTA RELLENA DE OBJETOS
        return json.dumps(self.getAllDataRecursiveObject().__dict__,sort_keys=True,indent=4)
