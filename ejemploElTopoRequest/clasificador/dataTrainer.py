from textblob.classifiers import NaiveBayesClassifier
import pickle
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.entities.ClassifyEntity import ClassifyEntity
from clasificador.entities.EntitiesArray import EntitiesArray

class dataTrainer:


    def __init__(self, Path):
        self.path = Path

    def train(self):
        with open(self.path, 'r') as fp:
            self.cl = NaiveBayesClassifier(fp, format="json")

    def persistantWrite(self, PathToLoad):
        object = self.cl
        file = open(PathToLoad,'wb')
        pickle.dump(object,file)

    def persistantRead(self, PathRead):
        classifier_f = open(PathRead, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()
        return self.classifier

    def generateFileParagraphs(self, finalPath):
        todosLosObjetos = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        for webPageInfoObjectInArray in todosLosObjetos:
            for cadenaParrafo in webPageInfoObjectInArray.getParrafo():
                classifyEntity = ClassifyEntity(cadenaParrafo, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
                print(entitiesArray.createJsonString())
                outfile = open(finalPath, 'w')
                outfile.write(entitiesArray.createJsonString())
                outfile.close()

