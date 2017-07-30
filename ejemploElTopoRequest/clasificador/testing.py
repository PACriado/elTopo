from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.dataTrainer import dataTrainer
from clasificador.dataClasificator import dataClasificator
from textblob.classifiers import NaiveBayesClassifier
from clasificador.classificator import classificator
#ASI SE LEE UN FICHERO JSON Y TE RETORNA EL OBJETO WEBPAGE INFO
##webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/1499887306392/offLine/1499888242828-httpsthehiddenwikiorg.json')

##print(webPageInfoObject.getAllUrls())

#ASI SE LEEN TODOS LOS FICHEROS QUE HAY DENTRO DE UN DIRECTORIO Y TE RETORNA UN ARRAY DE OBJETOS
todosLosObjetos = leerFicherosWebPageInfo.readAllFilesInDirectory("/home/usertfm/SalidaJSON/1501436636356/onLine/")




##cargarmelo, llevarlo al main, booleano entrenar o clasificar, y otro booleano que sea lanzar crawler para clasificador.

ejemplo = classificator()
##ejemplo.training()
classifier = ejemplo.getClasifier()


for webPageInfoObjectInArray in todosLosObjetos:
    ##print(webPageInfoObjectInArray.getAllSpans())
    ##print("Inicio")
    ##print("URLS")
    ##print(webPageInfoObjectInArray.getAllUrls())
    ##print("Titles")
    ##print(webPageInfoObjectInArray.getAllTitles())
    ##print("Headers")
    ##print(webPageInfoObjectInArray.getAllHeaders())
    ##print("Meta")
    ##print(webPageInfoObjectInArray.getAllMetadatas())
    ##print("Fin")
    miClass = dataClasificator( webPageInfoObjectInArray, classifier)

    ##print(miClass.classifyAllUrl())
    ##print(miClass.classifyAllParrafos())
    ##print(miClass.classifyAllHeaders())
    print(miClass.classifyAllSpan())
    ##print(miClass.getTitle())
    ##print(miClass.classify(webPageInfoObjectInArray.getTitle()))
    ##print("")



