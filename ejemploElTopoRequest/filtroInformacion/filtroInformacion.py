import bs4
from lxml import html


class filtroInformacion:

    def __init__(self, conexion, url):
        self.conexion = conexion
        self.url = url
        self.page = self.conexion.getRequestAuto(self.url)
        self.tree = html.fromstring(self.page.content)
        if self.page.status_code != 200 :
            #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
            print("LA WEB NO RETORNA UN HTTP 200!")


    def getTitle(self):
        title = self.tree.xpath('//title/text()')
        return title
