from textblob.classifiers import NaiveBayesClassifier
from clasificador.dataTrainer import dataTrainer

##cambiar de nombre a clasificator
classifier = NaiveBayesClassifier

class classificator:


    def __init__(self, trainingJSONPath, persistantWritepath, persistantReadpath, results):
        self.trainingJsonPath = trainingJSONPath
        self.persistantWriteFile = persistantWritepath
        self.persistantReadFile = persistantReadpath
        self.result = results
        print("hey")
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
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileParagraphs(self.result)

    def generateJsonUrlData(self):
        print("hola")
        print(self.trainingJsonPath)
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileUrl(self.result)

    def generateJsonTitleData(self):
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileTitle(self.result)

    def generateJsonHeaderData(self):
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileHeader(self.result)

    def generateJsonMetaData(self):
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileMeta(self.result)

    def generateJsonSpanData(self):
        trainer = dataTrainer(self.trainingJsonPath)
        trainer.generateFileSpan(self.result)
