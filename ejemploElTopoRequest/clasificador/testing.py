from Entidades.webPageInfo import webPageInfo
from Entidades.leerFicherosWebPageInfo import leerFicherosWebPageInfo
from clasificador.dataTrainer import dataTrainer
from clasificador.dataClasificator import dataClasificator
from textblob.classifiers import NaiveBayesClassifier
from clasificador.classificator import classificator
from preProcesador.preProcesator import Preprocesator
from urllib.parse import urlparse
#ASI SE LEE UN FICHERO JSON Y TE RETORNA EL OBJETO WEBPAGE INFO
##webPageInfoObject = webPageInfo(route='/home/usertfm/SalidaJSON/1499887306392/offLine/1499888242828-httpsthehiddenwikiorg.json')

##print(webPageInfoObject.getAllUrls())

#ASI SE LEEN TODOS LOS FICHEROS QUE HAY DENTRO DE UN DIRECTORIO Y TE RETORNA UN ARRAY DE OBJETOS
##todosLosObjetos = leerFicherosWebPageInfo.readAllFilesInDirectory("/home/usertfm/SalidaJSON/1501436636356/onLine/")

procesador = Preprocesator("/home/usertfm/SalidaJSON/1501436636356/onLine/", "/home/usertfm/SalidaJSON/Preproc/")
procesador.process()
##cargarmelo, llevarlo al main, booleano entrenar o clasificar, y otro booleano que sea lanzar crawler para clasificador.

##ejemplo = classificator()

##ejemplo.training()
##classifier = ejemplo.getClasifier()




'''
mList1 = webPageInfoObjectInArray.getAllUrls()
mList2 = webPageInfoObjectInArray.getAllUrls()
mList1 = mList1[0]
mList2 = mList2[0]
urlList = []


for link1 in mList1:

    found = False

    for link in mList2:
        if link1 in link:
            found = True
            break

    print (found)

mList3 = webPageInfoObjectInArray.getAllUrls()
mList3 = mList3[0]
for url in mList1:
    hostname = urlparse(url).hostname.split(".")

    hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
    print(hostname)
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    urlList.append(domain)
    print(domain)
    list(set(urlList))
print(urlList)
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
##miClass = dataClasificator( webPageInfoObjectInArray, classifier)

##print(miClass.classifyAllUrl())
##print(miClass.classifyAllParrafos())
##print(miClass.classifyAllHeaders())
##print(miClass.classifyAllSpan())
##print(miClass.getTitle())
##print(miClass.classify(webPageInfoObjectInArray.getTitle()))
##print("")

'''

