import json


class webPageInfo:
    def __init__(self, url='', title='', isOnline=True, route=''):
        if route != '':
            #DE ESTA FORMA CARGAMOS UN JSON A ESTA CLASE
            with open(route) as json_data:
                self.__dict__ = json.load(json_data)
        else:
            #SI NO HAY JSON, CARGAMOS LA CLASE "A MANO"
            self.url = url
            self.title = title
            self.children = []
            self.isOnline = isOnline
            self.headers = []
            self.metadata = []
            self.parrafo = []
            self.span = []
            self.images = 0
            self.videos = 0
            self.label = "" #ESTE ATRIBUTO ES NECESARIO PARA EL CLASIFICADOR

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setIsOnline(self, isOnline):
        self.isOnline = isOnline

    def getIsOnline(self):
        return self.isOnline

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def setHeader(self, headers):
        self.headers = headers

    def getHeader(self):
        return self.headers

    def setMetadata(self, metadata):
        self.metadata = metadata

    def getMetadata(self):
        return self.metadata

    def setParrafo(self, parrafo):
        self.parrafo = parrafo

    def getParrafo(self):
        return self.parrafo

    def setSpan(self, span):
        self.span = span

    def getSpan(self):
        return self.span

    def setImages(self, images):
        self.images = images

    def getImages(self):
        return self.images

    def setVideos(self, videos):
        self.videos = videos

    def getVideos(self):
        return self.videos

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def getAllUrls(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getUrl()
        else:
            for element in self.getChildren():
                all.append(element.getAllUrls())

        return all

    def getAllTitles(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getTitle()
        else:
            for element in self.getChildren():
                all.append(element.getAllTitles())

        return all

    def getAllHeaders(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getHeader()
        else:
            for element in self.getChildren():
                all.append(element.getAllHeaders())

        return all


    def getAllMetadatas(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getMetadata()
        else:
            for element in self.getChildren():
                all.append(element.getAllMetadatas())

        return all

    def getAllParrafos(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getParrafo()
        else:
            for element in self.getChildren():
                all.append(element.getAllParrafos())

        return all

    def getAllSpans(self):
        all = []
        childrenSize = self.getChildren().__len__()
        if childrenSize == 0:
            return self.getSpan()
        else:
            for element in self.getChildren():
                all.append(element.getAllSpans())

        return all
    #AÑADIR METODOS QUE DEVUELVAN TODOS LOS METAS, TODOS LOS SPAN, etc etc es decir los propios y los de los hijos.

