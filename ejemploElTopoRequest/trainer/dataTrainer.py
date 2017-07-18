from textblob.classifiers import NaiveBayesClassifier
import pickle

class dataTrainer:

    path = ""
    cl = ""

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
