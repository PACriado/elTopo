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

    def training(self):
        print("Iniciando entrenamiento")
        object = dataTrainer(self.trainingJsonPath)
        object.train()
        object.persistantWrite(self.persistantWriteFile)
        print("El entrenamiento es persistente")

    def getClasifier(self):
        objecto = dataTrainer(self.trainingJsonPath)
        # objecto.train()
        classifier = objecto.persistantRead(self.persistantReadFile)
        return classifier

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

    def generateJsonWithAllData(self):
        trainer = dataTrainer(self.readJsonDataFile)
        trainer.generateFileAllTypes(self.result)
