from textblob.classifiers import NaiveBayesClassifier
from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
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
        all = []
        urlList  = self.webPageInfo.getAllUrls()
        for url in urlList:
            ##pprint("************" + self.classifier.classify(url))
            all.append(self.classifier.classify(url))
        return all

    def classifyAllHeaders(self):
        all = []
        headerList  = self.webPageInfo.getAllHeaders()
        for header in headerList:
            for e in header:
                add = self.classifier.classify(e)
        return all

    def classifyAllTitles(self):
        all = []
        titleList  = self.webPageInfo.getAllTitles()
        for titles in titleList:
            for e in titles:
                all.append(self.classifier.classify(e))
        return all

    def classifyAllParrafos(self):
        all = []
        parrafosList  = self.webPageInfo.getAllParrafos()
        for parrafo in parrafosList:
            ##print(parrafo)
            for e in parrafo:
                all.append(self.classifier.classify(e))
        return all

    def classifyAllSpan(self):
        all = []
        spanList  = self.webPageInfo.getAllSpans()
        print(spanList)
        for span in spanList:
            for e in span:
            ##return self.classifier.classify(span)
                all.append(self.classifier.classify(e))
        return all
