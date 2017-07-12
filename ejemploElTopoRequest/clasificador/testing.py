from textblob.classifiers import NaiveBayesClassifier
import pickle
import json
import sys
import json
from pprint import pprint
import jSONtoWebPageInfo as jsonConverter


webPageInformation = jsonConverter(url='/home/usertfm/SalidaJSON/1499718909639/onLine/1499718910438-httpwwwgooglees.json')

webPageInformation.get





##with open('/home/usertfm/SalidaJSON/1499718909639/onLine/1499718910438-httpwwwgooglees.json') as data_file:
  ##  data = json.load(data_file)
##pprint(data)

##print(data["span"])a


##with open('/home/usertfm/Escritorio/prueba/test.json', 'r') as fp:
  ##  cl = NaiveBayesClassifier(fp, format="json")

##object = cl
##file = open('/home/usertfm/Escritorio/testo/testin.txt','wb')
##pickle.dump(object,file)

##classifier_f = open("/home/usertfm/Escritorio/testo/testin.txt", "rb")
##classifier = pickle.load(classifier_f)
##classifier_f.close()
#!/usr/bin/python







##resultado = classifier.classify(data["span"])
##prob_dist = classifier.prob_classify("I babys")
##prob_dist.max()
##new_data = [('She is my best friend.', 'pos'),
 ##            ("I'm happy to have a new friend.", 'pos'),
 ##            ("Stay thirsty, my friend.", 'pos'),
 ##            ("He ain't from around here.", 'neg')]
##cl.update(new_data)
##True

##cl.show_informative_features(3)
##print("Resultado: {0}".format(resultado))


