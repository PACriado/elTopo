from pprint import pprint
import clasificador.entities.ClassifyEntity
from clasificador.entities.ClassifyEntity import ClassifyEntity
from clasificador.entities.EntitiesArray import EntitiesArray
import clasificador
from Entidades.webPageInfo import webPageInfo
from accesoDatos.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.dataTrainer import dataTrainer
from clasificador.dataClasificator import dataClasificator
from textblob.classifiers import NaiveBayesClassifier
#ASI SE LEE UN FICHERO JSON Y TE RETORNA EL OBJETO WEBPAGE INFO
webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/1499887306392/offLine/1499888242828-httpsthehiddenwikiorg.json')

##print("***************")
#COMO PUEDES VER, LOS GETTER FUNCIONAN, YA QUE LO QUE HAS LEIDO ES UN OBJETO
##print(webPageInfoObject.getUrl())
##print(webPageInfoObject.getTitle())
##print("---------------")

#ASI SE LEEN TODOS LOS FICHEROS QUE HAY DENTRO DE UN DIRECTORIO Y TE RETORNA UN ARRAY DE OBJETOS
todosLosObjetos = leerFicherosWebPageInfo.readAllFilesInDirectory("/home/usertfm/SalidaJSON/1500546733904/onLine/")

##print(todosLosObjetos)

##classifier_f = open("/home/usertfm/Escritorio/testo/testin.txt", "rb")
##classifier = pickle.load(classifier_f)
##classifier_f.close()

##with open('/home/usertfm/Escritorio/prueba/test.json', 'r') as fp:
  ##  cl = NaiveBayesClassifier(fp, format="json")

##object = cl
##file = open('/home/usertfm/Escritorio/testo/testin.txt','wb')
##pickle.dump(object,file)

##resultado = classifier.classify(data["span"])
##prob_dist = classifier.prob_classify("I babys")
##prob_dist.max()




classifier = NaiveBayesClassifier
##False escribimos, true leemos
readWrite = True

if(readWrite == False):
    object = dataTrainer('/home/usertfm/Escritorio/prueba/test.json')
    object.train()
    object.persistantWrite('/home/usertfm/Escritorio/testo/testin.txt')
else:
    object = dataTrainer('/home/usertfm/Escritorio/prueba/test.json')
    object.train()
    classifier = object.persistantRead('/home/usertfm/Escritorio/testo/testin.txt')
    trainer = dataTrainer("/home/usertfm/SalidaJSON/1500546733904/onLine/")
    trainer.generateFileParagraphs("")
       #miClass = dataClasificator( webPageInfoObjectInArray, classifier)
    #ASI SE RECORRE EL ARRAY Y COMO VES, LOS GETTER FUNCIONAN PORQUE HAS LEIDO OBJETOS :)
       ##print(miClass.getUrl())
    ##pprint(miClass.printer())
       #pprint(miClass.classifyAllSpan())

    ##print(miClass.getTitle())
    ##print(miClass.classify(webPageInfoObjectInArray.getTitle()))
    ##print("")












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


