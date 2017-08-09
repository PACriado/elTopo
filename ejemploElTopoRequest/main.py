from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config

testRestService = False
testListRestService = False
crawlerOrClassificator = True

##clasificator booleans poner a true el que se quiera lanzar
header = False
url = True
paragraph = False
metadata = False
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
        ##meter parametros
        ficheroParaEntrenamiento = configuracion.getFicheroParaEntrenamiento()

        ##cambiar el nombre de esto... TODO
        ficheroParaEntrenamientoGeneradoParaEntrenamiento = configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()

        print("hola")
        print(configuracion.getRutaSalidaPreProcesador())

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
            classifier = classificatorObject.getClasifier()
            #hay que hacer un bucle leyendo los webpage info que salen del preprocesador
            #pasar al classify allUrls, allSpans etc etc
            print(classifier.classify("clasificameESTO"))

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

