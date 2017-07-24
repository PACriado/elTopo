from textblob.classifiers import NaiveBayesClassifier
from clasificador.dataTrainer import dataTrainer


classifier = NaiveBayesClassifier
##False escribimos, true leemos

class reader:

    readWrite = False

    def __init__(self, conditionRW,):
        self.readWrite = conditionRW

    def readOrWrite(self):
        if(self.readWrite == False):
            print("ENtra false")
            object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
            object.train()
            object.persistantWrite('/home/usertfm/Escritorio/testo/testin.txt')
        else:
            print("Entra true")
            object = dataTrainer('/home/usertfm/Escritorio/prueba/training.json')
            object.train()
            classifier = object.persistantRead('/home/usertfm/Escritorio/testo/testin.txt')
            return classifier

    def generateJsonData(self):
        trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
        trainer.generateFileParagraphs('/home/usertfm/Escritorio/prueba/train.json')
