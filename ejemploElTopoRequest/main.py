from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo
from clasificador.entities.categoryStatistic import categoryStatistic

testRestService = False
testListRestService = False
crawlerOrClassificator = True

##clasificator booleans poner a true el que se quiera lanzar
allData = False
paragraph = False

configuracion = config("./configElTopo/config.json")

if(not testRestService):
    if(crawlerOrClassificator == False):
        theSpyder = spyder()
        rutaSalidaSpyder = theSpyder.launch()
        procesador = Preprocesator(rutaSalidaSpyder+"onLine/", configuracion.getRutaSalidaPreProcesador())
        procesador.process()
    else:
        trainOrClassify = False
        ficheroParaEntrenamiento = configuracion.getFicheroParaEntrenamiento()

        ##cambiar el nombre de esto... TODO
        ficheroParaEntrenamientoGeneradoParaEntrenamiento = configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()

        if(trainOrClassify == True):
            #Entrenamos con todas las posibilidades y generamos los ficheros correspondientes de entrenamiento persistente
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonHeaderData()
            classificatorObject.training()
            '''
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonUrlData()
            classificatorObject.training()
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonMetaData()
            classificatorObject.training()
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonSpanData()
            classificatorObject.training()
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteTitle(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonTitleData()
            classificatorObject.training()
            #El entrenamiento de allData le activamos a mano, porque todabia no funciona fino

            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonParagraphData()
            classificatorObject.training()

            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistente(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonWithAllData()
            classificatorObject.training() '''
            ##if de todos   TODO
            #fin de los ifs



        else:
            classifyMeta = False
            classifyParrafo = False
            classifyHeader = False #Hay que revisar porque este no funciona correctamente. hay que mirar el entrenamiento
            classifySpan = True
            classifyUrl = False
            classifyTitle = False

            #hay que hacer un bucle leyendo los webpage info que salen del preprocesador
            #pasar al classify allUrls, allSpans etc etc
            webPageInfoObject = webPageInfo(route= '/home/usertfm/SalidaJSON/Preproc/google.es.json')

            if classifyMeta == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier Meta...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                print(clasificator.classifyAllMeta())
                print(clasificator.accuracyAll("META", "Armas"))
            if classifyParrafo == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier Parragraph...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                print(clasificator.classifyAllParrafos())
                print(clasificator.accuracyAll("PARRAFO", "Armas"))
            if classifyHeader == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier Headers...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                print(clasificator.classifyAllHeaders())
                print(clasificator.accuracyAll("HEADER", "Armas"))
            if classifySpan == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier Spans...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                #allClasifyElements = clasificator.classifyAllSpan()
                #allClasifyElementsUnique = list(set(allClasifyElements)) #ESTO ELIMINA LOS ELEMENTOS DUPLICADOS EN EL ARRAY
                #print(allClasifyElements)
                #print(allClasifyElementsUnique)
                #print(clasificator.accuracyAll("SPAN", "Armas"))
                estadisticas = clasificator.accuracyAllByCategory("SPAN",configuracion.getRutaFicheroCategorias())
                for estadistica in estadisticas:
                    print(estadistica.getcategory())
                    print(estadistica.getstatistic())

            if classifyUrl == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier URL...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                print(clasificator.classifyAllUrl())
                print(clasificator.accuracyAll("URL", "Armas"))
            if classifyTitle == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteTitle(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                print("Cargado Classifier Title...")
                classifier = classificatorObject.getClasifier()
                print("Classifier Cargado")
                clasificator = dataClasificator( webPageInfoObject, classifier)
                print(clasificator.classifyAllTitles())
                print(clasificator.accuracyAll("TITLE", "Armas"))

else:
    if(testListRestService):
        caller = SpyderRestCaller()
        paths = caller.callList()
        print(paths)

    else:
        caller = SpyderRestCaller(URL="http://localhost:5005/lanzar")
        request= SpyderRequest()
        #request= SpyderRequest(Url="www.google.es")
        response = caller.call(request)
        print(response.filesPath)

