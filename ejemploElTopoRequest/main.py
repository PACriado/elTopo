from spyder.spyder import spyder
from clasificador.classificator import classificator
from spyderRestCaller.SpyderRestCaller import SpyderRestCaller
from EntidadesRest.SpyderRequest import SpyderRequest

'''
crawlerOrClassificator = True

if (crawlerOrClassificator == True):
    theSpyder = spyder()
    theSpyder.launch()

else:
    trainOrClassify = True
    ejemplo = classificator()
    if(trainOrClassify == True):
        ejemplo.training()
    else:
        classifier = ejemplo.clasify()
        ejemplo.generateJsonData()'''


caller = SpyderRestCaller(URL="http://localhost:5000/lanzar")
#request= SpyderRequest(Url="www.google.es")
request= SpyderRequest()
response = caller.call(request)
print(response.filesPath)
