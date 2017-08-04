from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest
from preProcesador.preProcesator import Preprocesator
from configElTopo.config import config

testRestService = False
testListRestService = False
crawlerOrClassificator = True


configuracion = config("./configElTopo/config.json")

if(not testRestService):
    if(crawlerOrClassificator == False):
        theSpyder = spyder()
        rutaSalidaSpyder = theSpyder.launch()
        procesador = Preprocesator(rutaSalidaSpyder+"onLine/", configuracion.getRutaSalidaPreProcesador())
        procesador.process()
    else:
        trainOrClassify = True
        ##meter parametros
        ficheroParaEntrenamiento = configuracion.getFicheroParaEntrenamiento()
        ficheroParaEntrenamientoGeneradoParaEntrenamiento = configuracion.getFicheroParaEntrenamientoGeneradoParaEntrenamiento()
        casificatorObject = classificator(ficheroParaEntrenamiento, configuracion.getRutaFicheroEntrenamientoPersistente(), configuracion.getRutaSalidaPreProcesador(), ficheroParaEntrenamientoGeneradoParaEntrenamiento)
        if(trainOrClassify == True):
            #aqui se usa el ficheroParaEntrenamiento
            #Aqui abria que añadir unos if para generar "ficheroParaEntrenamientoGeneradoParaEntrenamiento"
            # para las urls, para headers, o para todos (si es que se puede)
            '''ejemplo.generateJsonUrlData()
            ejemplo.generateJsonSpanData()
            ejemplo.generateJsonHeaderData()
            ejemplo.generateJsonParagraphData()'''
            #fin de los ifs

            casificatorObject.training()

        else:
            classifier = casificatorObject.getClasifier()
            #hay que hacer un bucle leyendo los webpage info que salen del preprocesador
            #pasar al classify allUrls, allSpans etc etc
            print(classifier.classify("tumadre"))

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

