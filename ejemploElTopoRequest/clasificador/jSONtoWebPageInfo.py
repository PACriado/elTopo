import json
import Entidades.webPageInfo as webPgInfo



class jSONtoWebPageInfo:
    def __init__(self, url=''):
        self.url = url


    def convertToJson(self):
        with open(self.url) as data_file:
            data = json.load(data_file)

            webPgInfo.setUrl(self.url)
            webPgInfo.setTitle(data["title"])
            webPgInfo.setIsOnline(True)
            webPgInfo.setChildren(data["children"])
            webPgInfo.setHeader(data["headers"])
            webPgInfo.setMetaData(data["metadata"])
            webPgInfo.setParrafo(data["parrafo"])
            webPgInfo.setSpan(data["span"])
            webPgInfo.setImages(data["images"])
            webPgInfo.setVideos(data["videos"])
