from textblob.classifiers import NaiveBayesClassifier
from Entidades.webPageInfo import webPageInfo
from accesoDatos.leerFicherosWebPageInfo import leerFicherosWebPageInfo
import pickle
from pprint import pprint
#Class that classifies all the data depending of the tag selected.
class dataClasificator:

    path = ""
    classifier = NaiveBayesClassifier
    webPageInfo = ""
    def __init__(self, WPI, Classifier):

        self.webPageInfo = WPI
        ##self.path = Path
        ##classifier_f = open(self.path, "rb")
        self.classifier = Classifier
        ##classifier_f.close()


    #Classification methods
    def printer(self):
        return self.webPageInfo.getUrl()

    def classifyUrl(self):
        url = self.webPageInfo.getUrl()
        var = self.classifier.classify(url)
        return var

    def classifyTitle(self):
        return self.classifier.classify(self.webPageInfo.getTitle())

    def classifyHeader(self):
        return self.classifier.classify(self.webPageInfo.getHeader())

    def classifyMetaData(self):
        return self.classifier.classify(self.webPageInfo.getMetadata())

    def classifyParraf(self):
        return self.classifier.classify(self.webPageInfo.getParrafo())

    def classifyAllUrl(self):
        urlList  = self.webPageInfo.getAllUrls()
        for url in urlList:
            pprint(self.classifier.classify(url))


