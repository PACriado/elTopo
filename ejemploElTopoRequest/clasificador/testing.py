from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.dataTrainer import dataTrainer
from clasificador.dataClasificator import dataClasificator
from textblob.classifiers import NaiveBayesClassifier
from clasificador.classificator import classificator
#ASI SE LEE UN FICHERO JSON Y TE RETORNA EL OBJETO WEBPAGE INFO
webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/1499887306392/offLine/1499888242828-httpsthehiddenwikiorg.json')



#ASI SE LEEN TODOS LOS FICHEROS QUE HAY DENTRO DE UN DIRECTORIO Y TE RETORNA UN ARRAY DE OBJETOS
todosLosObjetos = leerFicherosWebPageInfo.readAllFilesInDirectory("/home/usertfm/SalidaJSON/1500914757772/onLine/")




##cargarmelo, llevarlo al main, booleano entrenar o clasificar, y otro booleano que sea lanzar crawler para clasificador.

ejemplo = classificator()
##ejemplo.training()
classifier = ejemplo.clasify()
##ejemplo.generateJsonData()

for webPageInfoObjectInArray in todosLosObjetos:
    miClass = dataClasificator( webPageInfoObjectInArray, classifier)

    print(miClass.classifyAllParrafos())

    ##print(miClass.getTitle())
    ##print(miClass.classify(webPageInfoObjectInArray.getTitle()))
    ##print("")



