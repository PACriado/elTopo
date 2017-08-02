from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest

testRestService = True
crawlerOrClassificator = False

if(not testRestService):
    if(crawlerOrClassificator == False):
        theSpyder = spyder()
        theSpyder.launch()

    else:
        trainOrClassify = True
        ejemplo = classificator()
        if(trainOrClassify == True):
            ejemplo.training()
        else:
            classifier = ejemplo.getClasifier()
            ejemplo.generateJsonSpanData()
else:
    caller = SpyderRestCaller(URL="http://localhost:5005/lanzar")

    request= SpyderRequest()
    #request= SpyderRequest(Url="www.google.es")
    response = caller.call(request)
    print(response.filesPath)

