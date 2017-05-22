from lxml import html
from filtroInformacion.HttpCode import HttpCode
from filtroInformacion.HttpCodeException import HttpCodeException
from elTopoRequest.elTopoRequest import ElTopoRequestException
from Entidades.webPageInfo import webPageInfo


class filtroInformacion:

    def __init__(self, conexion, url, depth=0, maxDepth=1):
       self.conexion = conexion
       self.url = url
       self.isOnline = True
       self.depth = depth
       self.maxDepth = maxDepth
       print("Filtrando {}".format(self.url))
       try:
         self.page = self.conexion.getRequestAuto(self.url)

         if self.page.status_code != HttpCode.OK.value:
            #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
            print("LA WEB NO RETORNA UN HTTP 200! RETORNA {0}".format(self.page.status_code))
            raise  HttpCodeException("NO HA SALTADO UN 200!")

         self.tree = html.fromstring(self.page.content)
       except ElTopoRequestException:
           #SI NO CONSEGUIMOS CONECTAR, PARA NOSOTROS LA WEB ESTA OFFLINE Y NO PODEMOS HACER MAS
           print("Web OffLine por no poder establecer conexion a {0}".format(self.url))
           self.isOnline=False
       except:
           #SI NO CONSEGUIMOS CONECTAR, PARA NOSOTROS LA WEB ESTA OFFLINE Y NO PODEMOS HACER MAS
           #NOS DA IGUAL LA EXCEPTION, ESTA OFFLINE
           print("Web {0} OffLine por error desconocido".format(self.url))
           self.isOnline=False


    def getUrl(self):
        currentUrl = self.url
        return currentUrl

    def getTitle(self):
        title = self.tree.xpath('//title/text()')
        return title

    def getLinksHref(self):
        listaLinks = []
        linksHref = self.tree.xpath('//a/@href')
        for currentLink in linksHref:
            if not currentLink.startswith("#"):
                listaLinks.append(currentLink)

        #AQUI HAY QUE AÑADIR UNA COMPROBAR SI LOS LINKS SON RELATIVOS O ABSOLUTOS.
        #CASO 1
        #SI EL LINK ES ABSOLUTO, POR EJEMPLO LOS QUE TIENEN UNA URL TIPO HTTP://PATATA.COM/COMOMEGUSTALASPATATAS NO HAY QUE HACER NADA, LO DEJAMOS COMO ESTA
        #CASO 2
        #SI EL LINK ES RELATIVO, POR EJEMPLO /COMOMEGUSTANLASPATATAS HAY QUE AÑADIRLE EL DOMINIO AL INICIO
        #DE FORMA QUE SI EL SELF.URL ES HTTP://PATATA.COM NOSOTROS RETORNEMOS HTTP://PATATA.COM/COMOMEGUSTANLASPATATAS
        #HAY QUE COMPROBAR QUE SELF.URL NO TENGA LA BARRA AL FINAL, Y SI LA TIENE, NO TENEMOS QUE PONERLA 2 VECES
        #EJEMPLO SI VIENE EL SELF.URL HTTP://PATATA.COM/ NO LE PODEMOS CONCATENAR /COMOMEGUSTANLASPATATAS PORQUE TENDRIAMOS HTTP://PATATA.COM//COMOMEGUSTANLASPATATAS
        return listaLinks

    def getLinksText(self):
        linksText = self.tree.xpath('//a/text()')
        return linksText

    def getAllDataRecursiveObject(self):
        currentWeb = webPageInfo(url=self.getUrl(),title=self.getTitle())

        #CODIGO QUE FALTA POR PULIR PARA QUE FUNCIONE LA BUSQUEDA RECURSIVA
        allChildren = self.getLinksHref()
        allChildrenList = []
        depth = self.depth+1
        if depth < self.maxDepth:
          for currentChildren in allChildren:
              currentURL = currentChildren
              try:
                newFilter = filtroInformacion(self.conexion,currentURL,depth=depth,maxDepth=self.maxDepth)
                newChildren = webPageInfo(url=currentURL, isOnline=newFilter.isOnline)
                if newFilter.isOnline:
                  newChildren.setTitle(newFilter.getTitle())

                  newChildren.getChildren().append(newFilter.getAllDataRecursiveObject())
                  allChildrenList.append(newChildren)

              except HttpCodeException:
                newChildren = webPageInfo(url=currentURL, isOnline=False)
              currentWeb.getChildren().append(newChildren)

        return currentWeb

    def getAllDataRecursiveJson(self):
        #AQUI HAY QUE MIRAR PORQUE NO SERIALIZA A JSON UN OBJETO CON UNA LISTA RELLENA DE OBJETOS
        obj_temp= self.getAllDataRecursiveObject()
        temp = obj_temp.toJSON()
        return temp
