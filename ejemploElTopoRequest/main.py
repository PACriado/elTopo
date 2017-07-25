from spyder.spyder import spyder
from clasificador.classificator import classificator

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
        ejemplo.generateJsonData()
