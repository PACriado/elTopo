from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest

testRestService = False
testListRestService = False
crawlerOrClassificator = True

if(not testRestService):
    if(crawlerOrClassificator == False):
        theSpyder = spyder()
        theSpyder.launch()

    else:
        trainOrClassify = False
        ##meter parametros
        ejemplo = classificator('/home/usertfm/Escritorio/prueba/training.json', '/home/usertfm/Escritorio/testo/testin.txt', '/home/usertfm/Escritorio/testo/testin.txt', '/home/usertfm/Escritorio/prueba/train.json')
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

