from textblob.classifiers import NaiveBayesClassifier
from Entidades.webPageInfo import webPageInfo
from accesoDatos.leerFicherosWebPageInfo import leerFicherosWebPageInfo
import pickle
from pprint import pprint
#Class that classifies all the data depending of the tag selected.
class clasificador:

    path = ""
    classifier = NaiveBayesClassifier
    webPageInfo = ""
    def __init__(self, WPI, Path):

        self.webPageInfo = WPI
        self.path = Path
        classifier_f = open(self.path, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()


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

   ## def navigateChilds(self, webPageInfo):
     ##   json = webPageInfo.toJSON()
      ##  for key, value in json.items():
        ##    if key == "children":

