import json

class webPageInfo:

    def __init__(self, url='', title='' , isOnline=True):
        self.url = url
        self.title = title
        self.children = []
        self.isOnline = isOnline
        self.headers = []
        self.metadata = []

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setIsOnline(self,isOnline):
        self.isOnline = isOnline

    def getIsOnline(self):
        return self.isOnline

    def setChildren(self,children):
        self.children = children

    def getChildren(self):
        return self.children

    def setHeader(self,headers):
        self.headers = headers

    def getHeader(self):
        return self.headers

    def setMetadata(self, metadata):
        self.metadata = metadata

    def getMetadata(self):
        return self.metadata

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

