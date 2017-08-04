from textblob.classifiers import NaiveBayesClassifier
from clasificador.dataTrainer import dataTrainer

##cambiar de nombre a clasificator
classifier = NaiveBayesClassifier

class classificator:


    def __init__(self, trainingJSONPath, persistantWritepath, JsonGenericData, results):
        self.trainingJsonPath = trainingJSONPath
        self.persistantWriteFile = persistantWritepath
        self.persistantReadFile = persistantWritepath
        self.readJsonDataFile = JsonGenericData
        self.result = results
   ##pasarlos pos parametros
    def training(self):
        object = dataTrainer(self.trainingJsonPath)
        object.train()
        object.persistantWrite(self.persistantWriteFile)

    def getClasifier(self):
        object = dataTrainer(self.trainingJsonPath)
        object.train()
        classifier = object.persistantRead(self.persistantReadFile)
        return classifier

    ##TODO cambiar los path a las diferentes rutas
    def generateJsonParagraphData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileParagraphs(self.result)

    def generateJsonUrlData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileUrl(self.result)

    def generateJsonTitleData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileTitle(self.result)

    def generateJsonHeaderData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileHeader(self.result)

    def generateJsonMetaData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileMeta(self.result)

    def generateJsonSpanData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileSpan(self.result)
