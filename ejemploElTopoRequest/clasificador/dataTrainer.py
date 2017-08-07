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

    def accuracy(self, jsonFile):
        return self.cl.accuracy(jsonFile)

    def persistantWrite(self, PathToLoad):
        object = self.cl
        file = open(PathToLoad,'wb')
        pickle.dump(object,file)

    def persistantRead(self, PathRead):
        classifier_f = open(PathRead, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()
        return self.classifier

    ##METODOS QUE GENERAN FICHEROS DE CONFIGURACIÓN CON DIFERENTES TIPOS DE DATOS.
    def generateFileParagraphs(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaParrafo in webPageInfoObjectInArray.getParrafo():
                classifyEntity = ClassifyEntity(cadenaParrafo, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)

        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()

    def generateFileUrl(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            classifyEntity = ClassifyEntity(webPageInfoObjectInArray.getUrl(), webPageInfoObjectInArray.getLabel())
            entitiesArray.add(classifyEntity)
        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()

    def generateFileTitle(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaTitle in webPageInfoObjectInArray.getTitle():
                classifyEntity = ClassifyEntity(cadenaTitle, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)


        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()

    def generateFileHeader(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaHeader in webPageInfoObjectInArray.getHeader():
                classifyEntity = ClassifyEntity(cadenaHeader, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)


        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()

    def generateFileMeta(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaMeta in webPageInfoObjectInArray.getMetadata():
                classifyEntity = ClassifyEntity(cadenaMeta, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)


        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()


    def generateFileSpan(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaSpan in webPageInfoObjectInArray.getSpan():
                classifyEntity = ClassifyEntity(cadenaSpan, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)


        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()

    def generateFileAllTypes(self, finalPath):
        allObjects = leerFicherosWebPageInfo.readAllFilesInDirectory(self.path)
        entitiesArray = EntitiesArray()
        outfile = open(finalPath, 'w')
        outfile.write("[")

        for webPageInfoObjectInArray in allObjects:
            for cadenaSpan in webPageInfoObjectInArray.getSpan():
                classifyEntity = ClassifyEntity(cadenaSpan, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
            for cadenaParrafo in webPageInfoObjectInArray.getParrafo():
                classifyEntity = ClassifyEntity(cadenaParrafo, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
            for cadenaMeta in webPageInfoObjectInArray.getMetadata():
                classifyEntity = ClassifyEntity(cadenaMeta, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
            for cadenaHeader in webPageInfoObjectInArray.getHeader():
                classifyEntity = ClassifyEntity(cadenaHeader, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
            for cadenaTitle in webPageInfoObjectInArray.getTitle():
                classifyEntity = ClassifyEntity(cadenaTitle, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)
            for cadenaUrl in webPageInfoObjectInArray.getUrl():
                classifyEntity = ClassifyEntity(cadenaUrl, webPageInfoObjectInArray.getLabel())
                entitiesArray.add(classifyEntity)


        outfile.write(entitiesArray.createJsonString().replace("'", '"'))
        outfile.write("]")
        outfile.close()
