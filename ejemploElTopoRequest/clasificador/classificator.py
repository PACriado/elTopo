from textblob.classifiers import NaiveBayesClassifier
from clasificador.dataTrainer import dataTrainer

##cambiar de nombre a clasificator
classifier = NaiveBayesClassifier

class classificator:



    def training(self):
        object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
        object.train()
        object.persistantWrite('/home/usertfm/Escritorio/testo/testin.txt')

    def getClasifier(self):
        object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
        object.train()
        classifier = object.persistantRead('/home/usertfm/Escritorio/testo/testin.txt')
        return classifier

    ##TODO cambiar los path a las diferentes rutas
    def generateJsonParagraphData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileParagraphs('/home/usertfm/Escritorio/prueba/train.json')

    def generateJsonUrlData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileUrl('/home/usertfm/Escritorio/prueba/train.json')

    def generateJsonTitleData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileTitle('/home/usertfm/Escritorio/prueba/train.json')

    def generateJsonHeaderData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileHeader('/home/usertfm/Escritorio/prueba/train.json')

    def generateJsonMetaData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileMeta('/home/usertfm/Escritorio/prueba/train.json')

    def generateJsonSpanData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileSpan('/home/usertfm/Escritorio/prueba/train.json')
