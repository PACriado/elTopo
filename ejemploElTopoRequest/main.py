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
        trainOrClassify = False
        ##meter parametros
        ejemplo = classificator('./clasificatorData/training.json', './clasificatorData/entrenamiento.txt', configuracion.getRutaSalidaPreProcesador(), './clasificatorData/train.json')
        if(trainOrClassify == True):
            ejemplo.training()
        else:
            classifier = ejemplo.getClasifier()
            print(classifier.classify("tumadre"))
            ejemplo.generateJsonUrlData()
            ejemplo.generateJsonSpanData()
            ejemplo.generateJsonHeaderData()
            ejemplo.generateJsonParagraphData()
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

