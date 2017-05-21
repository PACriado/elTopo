

class webPageInfo:

    def __init__(self, url='', title='' , isOnline=True, children=[]):
        self.url = url
        self.title = title
        self.children = children
        self.isOnline = isOnline

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
        return self.title
