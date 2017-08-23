from lxml import html

from Entidades.webPageInfo import webPageInfo
from spyder.elTopoRequest.elTopoRequest import ElTopoRequestException
from spyder.filtroInformacion.HttpCode import HttpCode
from spyder.filtroInformacion.HttpCodeException import HttpCodeException
from spyder.utils.utils import utils


class filtroInformacion:
    def __init__(self, conexion, url, depth=1, maxDepth=1):
        self.conexion = conexion
        self.url = url
        self.isOnline = True
        self.depth = depth
        self.maxDepth = maxDepth
        # print("Filtrando {}".format(self.url))
        try:
            self.page = self.conexion.getRequestAuto(self.url)

            if self.page.status_code != HttpCode.OK.value:
                # AQUI DEBERIAMOS LANZAR UNA EXCEPCION
                # print("LA WEB NO RETORNA UN HTTP 200! RETORNA {0}".format(self.page.status_code))
                raise HttpCodeException("NO HA SALTADO UN 200!")

            self.tree = html.fromstring(self.page.content.decode('utf-8', 'ignore'))
        except ElTopoRequestException:
            # SI NO CONSEGUIMOS CONECTAR, PARA NOSOTROS LA WEB ESTA OFFLINE Y NO PODEMOS HACER MAS
            print("Web OffLine por no poder establecer conexion a {0}".format(self.url))
            self.isOnline = False
        except:
            # SI NO CONSEGUIMOS CONECTAR, PARA NOSOTROS LA WEB ESTA OFFLINE Y NO PODEMOS HACER MAS
            # NOS DA IGUAL LA EXCEPTION, ESTA OFFLINE
            print("Web {0} OffLine por error desconocido".format(self.url))
            self.isOnline = False

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
            # Las anclas no nos interesan
            if not currentLink.startswith("#"):
                if utils.is_absolute(currentLink):
                    listaLinks.append(currentLink)
                else:
                    absoluteCurrentLink = utils.get_absolute_url(self.url, currentLink)
                    listaLinks.append(absoluteCurrentLink)

        # AQUI HAY QUE AÑADIR UNA COMPROBAR SI LOS LINKS SON RELATIVOS O ABSOLUTOS.
        # CASO 1
        # SI EL LINK ES ABSOLUTO, POR EJEMPLO LOS QUE TIENEN UNA URL TIPO HTTP://PATATA.COM/COMOMEGUSTALASPATATAS NO HAY QUE HACER NADA, LO DEJAMOS COMO ESTA
        # CASO 2
        # SI EL LINK ES RELATIVO, POR EJEMPLO /COMOMEGUSTANLASPATATAS HAY QUE AÑADIRLE EL DOMINIO AL INICIO
        # DE FORMA QUE SI EL SELF.URL ES HTTP://PATATA.COM NOSOTROS RETORNEMOS HTTP://PATATA.COM/COMOMEGUSTANLASPATATAS
        # HAY QUE COMPROBAR QUE SELF.URL NO TENGA LA BARRA AL FINAL, Y SI LA TIENE, NO TENEMOS QUE PONERLA 2 VECES
        # EJEMPLO SI VIENE EL SELF.URL HTTP://PATATA.COM/ NO LE PODEMOS CONCATENAR /COMOMEGUSTANLASPATATAS PORQUE TENDRIAMOS HTTP://PATATA.COM//COMOMEGUSTANLASPATATAS
        return listaLinks

    def getHeader(self):
        headers = self.tree.xpath('/html/body/*[self::h1 or self::h2 or self::h3]/text()')
        return headers

    def getMetadata(self):
        metadata = self.tree.xpath('//meta[@name="description"]/@content')
        return metadata

    def getLinksText(self):
        linksText = self.tree.xpath('//a/text()')
        return linksText

    def getParrafo(self):
        parrafo = self.tree.xpath('//p/text()')
        return parrafo

    def getSpan(self):
        span = self.tree.xpath('//span//text()')
        return span

    def getImages(self):
        images = self.tree.xpath('count(//*[(substring(@src, string-length(@src) - string-length("png") +1) = "png") '
                                 'or (substring(@src, string-length(@src) - string-length("jpeg") +1) = "jpeg" )])')
        return images

    def getVideos(self):
        videos = self.tree.xpath('count(//*[(substring(@src, string-length(@src) - string-length("mp4") +1) = "mp4") '
                                 'or (substring(@src, string-length(@src) - string-length("mpeg") +1) = "mpeg" )])')
        return videos

    def getAllDataRecursiveObject(self):
        currentWeb = ''
        if self.depth == self.maxDepth:
            title = self.getTitle()
            if (title == None) or (not title):
                title = [""]

            currentWeb = webPageInfo(url=self.getUrl(), title=title)
            # aqui meter todos los filtros
            currentWeb.setHeader(self.getHeader())
            currentWeb.setMetadata(self.getMetadata())
            currentWeb.setParrafo(self.getParrafo())
            currentWeb.setSpan(self.getSpan())
            currentWeb.setImages(self.getImages())
            currentWeb.setVideos(self.getVideos())
        else:
            allChildren = self.getLinksHref()
            title = self.getTitle()
            if (title == None) or (not title):
                title = [""]
            currentWeb = webPageInfo(url=self.getUrl(), title=title)
            for currentChildren in allChildren:
                try:
                    newFilter = filtroInformacion(self.conexion, currentChildren, depth=(self.depth + 1),
                                                  maxDepth=self.maxDepth)
                    children = newFilter.getAllDataRecursiveObject()
                    currentWeb.getChildren().append(children)
                except:
                    currentWeb.setIsOnline(False)

        return currentWeb

    def getAllDataRecursiveJson(self, data):
        # AQUI HAY QUE MIRAR PORQUE NO SERIALIZA A JSON UN OBJETO CON UNA LISTA RELLENA DE OBJETOS
        temp = data.toJSON()
        return temp
