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
        ##for url in urlList:
            ##pprint("************" + url + self.classifier.classify(url))
        all.append(self.classifier.classify(urlList))
        return all

    def classifyAllHeaders(self):
        all = []
        headerList  = self.webPageInfo.getAllHeaders()
        for header in headerList:
            ##for e in header:
                ##add = self.classifier.classify(e)
            all.append(self.classifier.classify(header))
        return all

    def classifyAllTitles(self):
        all = []
        titleList  = self.webPageInfo.getAllTitles()
        for titles in titleList:
            print(titles)
            ##for e in titles:

            all.append(self.classifier.classify(titles))
        return all

    def classifyAllParrafos(self):
        all = []
        parrafosList  = self.webPageInfo.getAllParrafos()
        for parrafo in parrafosList:
            ##print(parrafo)
            ##for e in parrafo:
            all.append(self.classifier.classify(parrafo))
        return all

    def classifyAllSpan(self):
        all = []
        spanList  = self.webPageInfo.getAllSpans()
        ##print(spanList)
        for span in spanList:
            ##for e in span:
            ##return self.classifier.classify(span)
            all.append(self.classifier.classify(span))
        return all

    def classifyAllMeta(self):
        all = []
        metaList  = self.webPageInfo.getAllMetadatas()
        ##print(metaList)
        for meta in metaList:
            ##for e in meta:

            ##return self.classifier.classify(span)
            all.append(self.classifier.classify(meta))
        return all

    ##Metodos
    def accuracyAll(self, classifierType, probType):
        all = []
        lists = []
        if (classifierType == "URL"):
            lists = self.webPageInfo.getAllUrls()
            prob_dist = self.classifier.prob_classify(lists)
            all.append((prob_dist.prob(probType)))
        if (classifierType == "TITLE"):
            lists = self.webPageInfo.getAllTitles()
            for title in lists:
                print(title)
                prob_dist = self.classifier.prob_classify(title)
                all.append((prob_dist.prob(probType)))
        if (classifierType == "SPAN"):
            lists = self.webPageInfo.getAllSpans()
            for span in lists:
                prob_dist = self.classifier.prob_classify(span)
                all.append((prob_dist.prob(probType)))
        if (classifierType == "HEADER"):
            lists = self.webPageInfo.getAllHeaders()
            for header in lists:
                prob_dist = self.classifier.prob_classify(header)
                all.append((prob_dist.prob(probType)))
        if (classifierType == "PARRAFO"):
            lists = self.webPageInfo.getAllParrafos()
            for parrafo in lists:
                prob_dist = self.classifier.prob_classify(parrafo)
                all.append((prob_dist.prob(probType)))
        if (classifierType == "META"):
            lists = self.webPageInfo.getAllMetadatas()
            for meta in lists:

                prob_dist = self.classifier.prob_classify(meta)
                all.append((prob_dist.prob(probType)))
        return all
