

class webPageInfo:

    def __init__(self, url='', title='' , children=[]):
        self.url = url
        self.title = title
        self.children = children

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setChildren(self,children):
        self.children = children

    def getChildren(self):
        return self.title
