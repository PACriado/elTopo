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
        pprint("----" + urlList)
        for url in urlList:
            ##pprint("************" + self.classifier.classify(url))
            return self.classifier.classify(url)

    def classifyAllHeaders(self):
        headerList  = self.webPageInfo.getAllHeaders()
        for header in headerList:
            pprint(self.classifier.classify(header))
            return self.classifier.classify(header)

    def classifyAllTitles(self):
        titleList  = self.webPageInfo.getAllTitles()
        for titles in titleList:
            pprint(self.classifier.classify(titles))
            return self.classifier.classify(titles)

    def classifyAllParrafos(self):
        parrafosList  = self.webPageInfo.getAllParrafos()
        for parrafo in parrafosList:
            pprint(self.classifier.classify(parrafo))
            return self.classifier.classify(parrafo)

    def classifyAllSpan(self):
        spanList  = self.webPageInfo.getAllSpans()
        print(spanList)
        for span in spanList:
            newStr = str(span)
            print(newStr)
            pprint(self.classifier.classify(newStr))
            ##return self.classifier.classify(span)
