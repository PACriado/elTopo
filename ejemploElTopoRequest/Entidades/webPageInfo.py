

class webPageInfo:

    def __init__(self, url='', title=''):
        self.url = url
        self.title = title

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title
