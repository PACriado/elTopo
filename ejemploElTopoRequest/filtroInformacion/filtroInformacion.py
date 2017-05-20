from lxml import html
from filtroInformacion.HttpCode import HttpCode
from filtroInformacion.HttpCodeException import HttpCodeException

class filtroInformacion:

    def __init__(self, conexion, url):
       self.conexion = conexion
       self.url = url
       self.page = self.conexion.getRequestAuto(self.url)
       self.tree = html.fromstring(self.page.content)
       if self.page.status_code != HttpCode.OK.value :
          #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
          print("LA WEB NO RETORNA UN HTTP 200!")
          raise  HttpCodeException("NO HA SALTADO UN 200!")


    def getUrl(self):
        currentUrl = self.url
        return currentUrl

    def getTitle(self):
        title = self.tree.xpath('//title/text()')
        return title

    def getLinksHref(self):
        linksHref = self.tree.xpath('//a/@href')
        return linksHref;

    def getLinksText(self):
        linksText = self.tree.xpath('//a/text()')
        return linksText
