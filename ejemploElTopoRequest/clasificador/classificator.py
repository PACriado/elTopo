from textblob.classifiers import NaiveBayesClassifier
from clasificador.dataTrainer import dataTrainer

##cambiar de nombre a clasificator
classifier = NaiveBayesClassifier

class classificator:



    def training(self):
        object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
        object.train()
        object.persistantWrite('/home/usertfm/Escritorio/testo/testin.txt')

    def clasify(self):
        object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
        object.train()
        classifier = object.persistantRead('/home/usertfm/Escritorio/testo/testin.txt')
        return classifier


    def generateJsonData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileParagraphs('/home/usertfm/Escritorio/prueba/train.json')
