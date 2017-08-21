from textblob.classifiers import NaiveBayesClassifier
from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
import pickle
from pprint import pprint
from clasificador.entities.categoryStatistic import categoryStatistic

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
            print(header)
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
            print(parrafo)
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

    def classifyAllData(self):
        allData = []
        metaDataArray = self.classifyAllMeta()
        spanDataArray = self.classifyAllSpan()
        paragraphDataArray = self.classifyAllParrafos()
        titleDataArray = self.classifyAllTitles()
        headerDataArray = self.classifyAllHeaders()
        urlDatayArray = self.classifyAllUrl()

        allData.append(metaDataArray)
        allData.append(spanDataArray)
        allData.append(paragraphDataArray)
        allData.append(titleDataArray)
        allData.append(headerDataArray)
        allData.append(urlDatayArray)
        return allData

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
                #print(title)
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

        if (classifierType == "ALLDATA"):
            lists = self.webPageInfo.getAllMetadatas()
            lists.append(self.webPageInfo.getAllUrls())
            lists.append(self.webPageInfo.getAllParrafos())
            lists.append(self.webPageInfo.getAllTitles())
            lists.append(self.webPageInfo.getAllHeaders())
            lists.append(self.webPageInfo.getAllSpans())
            lists.append(self.webPageInfo.getAllTitles())
            print(lists)
            for data in lists:
                prob_dist = self.classifier.prob_classify(data)
                all.append((prob_dist.prob(probType)))
        return all


    def leerCategorias(self,ruta):
        categorias = []
        infile = open(ruta, 'r')
        for line in infile:
            line = line.replace("\n", "")
            categorias.append(line)
        infile.close()
        return categorias

    def accuracyAllByCategory(self, classifierType, categoriesPath,URL=""):
        estadisticaDeCategorias = []
        categorias = self.leerCategorias(categoriesPath)
        sumatorioEstadisticaCategoria=0
        for categoria in categorias:
            Statistics = self.accuracyAll(classifierType, categoria)
            for stadistica in Statistics:
                sumatorioEstadisticaCategoria+=stadistica
            numeroElementos = len(Statistics)
            if numeroElementos==0:
                numeroElementos=1
            estadisticaCategoria = sumatorioEstadisticaCategoria/numeroElementos
            estadisticaDeCategorias.append(categoryStatistic(categoria,estadisticaCategoria,URL=URL))
            sumatorioEstadisticaCategoria=0
        return estadisticaDeCategorias


