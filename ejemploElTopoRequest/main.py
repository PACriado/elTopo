from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config
from clasificador.dataClasificator import dataClasificator
from Entidades.webPageInfo import webPageInfo

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
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonUrlData()
            classificatorObject.training()
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonMetaData()
            classificatorObject.training()
            '''classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonSpanData()
            classificatorObject.training()'''
            classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteTitle(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
            classificatorObject.generateJsonTitleData()
            classificatorObject.training()
            #El entrenamiento de allData le activamos a mano, porque todabia no funciona fino

            if paragraph == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classificatorObject.generateJsonParagraphData()
                classificatorObject.training()

            if allData == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistente(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classificatorObject.generateJsonWithAllData()
                classificatorObject.training()
            ##if de todos   TODO
            #fin de los ifs



        else:
            classifyMeta = False
            classifyParrafo = False
            classifyHeader = False
            classifySpan = False
            classifyUrl = False
            classifyTitle = True

            #hay que hacer un bucle leyendo los webpage info que salen del preprocesador
            #pasar al classify allUrls, allSpans etc etc
            webPageInfoObject = webPageInfo(route= '/home/usertfm/SalidaJSON/Preproc/google.es.json')

            if classifyMeta == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteMetaData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllMeta())
                print(miClass.accuracyAll("META", "Armas"))
            if classifyParrafo == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteParagraphData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllParrafos())
                print(miClass.accuracyAll("PARRAFO", "Armas"))
            if classifyHeader == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteHeaderData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllHeaders())
                print(miClass.accuracyAll("HEADER", "Armas"))
            if classifySpan == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteSpanData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllSpan())
                print(miClass.accuracyAll("SPAN", "Armas"))
            if classifyUrl == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteUrlData(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllUrl())
                print(miClass.accuracyAll("URL", "Armas"))
            if classifyTitle == True:
                classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistenteTitle(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
                classifier = classificatorObject.getClasifier()
                miClass = dataClasificator( webPageInfoObject, classifier)
                print(miClass.classifyAllTitles())
                print(miClass.accuracyAll("TITLE", "Armas"))

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

