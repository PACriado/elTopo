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
header = False
url = False
paragraph = False
metadata = True
span = False
title = False
allData = False

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
        classificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistente(), configuracion.getRutaJSONTraining(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        if(trainOrClassify == True):
            if header == True:
                classificatorObject.generateJsonHeaderData()
            if url == True:
                classificatorObject.generateJsonUrlData()
            if paragraph == True:
                classificatorObject.generateJsonParagraphData()
            if metadata == True:
                classificatorObject.generateJsonMetaData()
            if span == True:
                classificatorObject.generateJsonSpanData()
            if title == True:
                classificatorObject.generateJsonTitleData()
            if allData == True:
                classificatorObject.generateJsonWithAllData()
            ##if de todos   TODO
            #fin de los ifs

            classificatorObject.training()

        else:
            classifyMeta = True
            classifyParrafo = False
            classifyHeader = False
            classifySpan = False
            classifyUrl = False
            classifyTitle = False
            classifier = classificatorObject.getClasifier()
            #hay que hacer un bucle leyendo los webpage info que salen del preprocesador
            #pasar al classify allUrls, allSpans etc etc
            webPageInfoObject = webPageInfo(route= configuracion.getWebPageInfoToClassify())
            miClass = dataClasificator( webPageInfoObject, classifier)
            if classifyMeta == True:
                print(miClass.classifyAllMeta())
            if classifyParrafo == True:
                print(miClass.classifyAllParrafos())
            if classifyHeader == True:
                print(miClass.classifyAllHeaders())
            if classifySpan == True:
                print(miClass.classifyAllSpan())
            if classifyUrl == True:
                print(miClass.classifyAllUrl())
            if classifyTitle == True:
                print(miClass.classifyAllTitles())
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

