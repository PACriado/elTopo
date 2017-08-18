import json


class config:

    def __init__(self, route=''):

        if route != '':
            #DE ESTA FORMA CARGAMOS UN JSON A ESTA CLASE
            with open(route) as json_data:
                self.__dict__ = json.load(json_data)
        else:
            self.RutaSalida =""
            self.RutaDiccionario=""
            self.MaxDepth=1
            self.UsarDiccionario= False
            self.UsarSiempreTor=False
            self.RenovarSiempreCircuitoTor=False
            self.DelayIntentoRenovacionCircuitoTor=2
            self.RutaServidoresSpyderRest=""
            self.RutaSalidaPreProcesador=""
            self.RutaFicheroEntrenamientoPersistente=""
            self.RutaFicheroEntrenamientoPersistenteHeaderData=""
            self.RutaFicheroEntrenamientoPersistenteUrlData=""
            self.RutaFicheroEntrenamientoPersistenteParagraphData=""
            self.RutaFicheroEntrenamientoPersistenteMetaData=""
            self.RutaFicheroEntrenamientoPersistenteSpanData=""
            self.RutaFicheroEntrenamientoPersistenteTitle=""
            self.FicheroParaEntrenamiento=""
            self.RutaFicheroCategorias=""
            self.FicheroParaEntrenamientoGeneradoParaEntrenamiento=""
            self.RutaJSONTraining=""
            self.WebPageInfoToClassify = ""
            self.url=[]
        self.Route = route

    def setRutaFicheroCategorias(self, rutaFicheroCategorias):
        self.RutaFicheroCategorias = rutaFicheroCategorias

    def getRutaFicheroCategorias(self):
        return self.RutaFicheroCategorias

    def setRutaFicheroEntrenamientoPersistenteHeaderData(self, rutaFicheroEntrenamientoPersistenteHeaderData):
        self.RutaFicheroEntrenamientoPersistenteHeaderData = rutaFicheroEntrenamientoPersistenteHeaderData

    def getRutaFicheroEntrenamientoPersistenteHeaderData(self):
        return self.RutaFicheroEntrenamientoPersistenteHeaderData

    def setRutaFicheroEntrenamientoPersistenteUrlData(self, rutaFicheroEntrenamientoPersistenteUrlData):
        self.RutaFicheroEntrenamientoPersistenteUrlData = rutaFicheroEntrenamientoPersistenteUrlData

    def getRutaFicheroEntrenamientoPersistenteUrlData(self):
        return self.RutaFicheroEntrenamientoPersistenteUrlData

    def setRutaFicheroEntrenamientoPersistenteParagraphData(self, rutaFicheroEntrenamientoPersistenteParagraphData):
        self.RutaFicheroEntrenamientoPersistenteParagraphData = rutaFicheroEntrenamientoPersistenteParagraphData

    def getRutaFicheroEntrenamientoPersistenteParagraphData(self):
        return self.RutaFicheroEntrenamientoPersistenteParagraphData

    def setRutaFicheroEntrenamientoPersistenteMetaData(self, rutaFicheroEntrenamientoPersistenteMetaData):
        self.RutaFicheroEntrenamientoPersistenteMetaData = rutaFicheroEntrenamientoPersistenteMetaData

    def getRutaFicheroEntrenamientoPersistenteMetaData(self):
        return self.RutaFicheroEntrenamientoPersistenteMetaData

    def setRutaFicheroEntrenamientoPersistenteSpanData(self, rutaFicheroEntrenamientoPersistenteSpanData):
        self.RutaFicheroEntrenamientoPersistenteSpanData = rutaFicheroEntrenamientoPersistenteSpanData

    def getRutaFicheroEntrenamientoPersistenteSpanData(self):
        return self.RutaFicheroEntrenamientoPersistenteSpanData

    def setRutaFicheroEntrenamientoPersistenteTitle(self, rutaFicheroEntrenamientoPersistenteTitle):
        self.RutaFicheroEntrenamientoPersistenteTitle = rutaFicheroEntrenamientoPersistenteTitle

    def getRutaFicheroEntrenamientoPersistenteTitle(self):
        return self.RutaFicheroEntrenamientoPersistenteTitle

    def setWebPageInfoToClassify(self, rutaWpInfo):
        self.WebPageInfoToClassify = rutaWpInfo

    def getWebPageInfoToClassify(self):
        return self.WebPageInfoToClassify

    def setRutaJSONTraining(self, rutaJSONTraining):
        self.RutaJSONTraining = rutaJSONTraining

    def getRutaJSONTraining(self):
        return self.RutaJSONTraining

    def setRutaSalida(self, rutaSalida):
        self.RutaSalida = rutaSalida

    def getRutaSalida(self):
        return self.RutaSalida

    def setFicheroParaEntrenamiento(self, ficheroParaEntrenamiento):
        self.FicheroParaEntrenamiento = ficheroParaEntrenamiento

    def getFicheroParaEntrenamiento(self):
        return self.FicheroParaEntrenamiento

    def setFicheroParaEntrenamientoGeneradoParaEntrenamiento(self, ficheroParaEntrenamientoGeneradoParaEntrenamiento):
        self.FicheroParaEntrenamientoGeneradoParaEntrenamiento = ficheroParaEntrenamientoGeneradoParaEntrenamiento

    def getFicheroParaEntrenamientoGeneradoParaEntrenamiento(self):
        return self.FicheroParaEntrenamientoGeneradoParaEntrenamiento

    def setRutaFicheroEntrenamientoPersistente(self, rutaFicheroEntrenamientoPersistente):
        self.RutaFicheroEntrenamientoPersistente = rutaFicheroEntrenamientoPersistente

    def getRutaFicheroEntrenamientoPersistente(self):
        return self.RutaFicheroEntrenamientoPersistente

    def setRutaSalidaPreProcesador(self, rutaSalidaPreProcesador):
        self.RutaSalidaPreProcesador = rutaSalidaPreProcesador

    def getRutaSalidaPreProcesador(self):
        return self.RutaSalidaPreProcesador

    def setRutaServidoresSpyderRest(self, rutaServidoresSpyderRest):
        self.RutaServidoresSpyderRest = rutaServidoresSpyderRest

    def getRutaServidoresSpyderRest(self):
        return self.RutaServidoresSpyderRest

    def setRutaDiccionario(self, rutaDiccionario):
        self.RutaDiccionario = rutaDiccionario

    def getRutaDiccionario(self):
        return self.RutaDiccionario

    def setMaxDepth(self, maxDepth):
        self.MaxDepth = maxDepth

    def getMaxDepth(self):
        return self.MaxDepth

    def setUsarDiccionario(self, usarDiccionario):
        self.UsarDiccionario = usarDiccionario

    def getUsarDiccionario(self):
        return self.UsarDiccionario

    def setUsarSiempreTor(self, usarSiempreTor):
        self.UsarSiempreTor = usarSiempreTor

    def getUsarSiempreTor(self):
        return self.UsarSiempreTor

    def setRenovarSiempreCircuitoTor(self, renovarSiempreCircuitoTor):
        self.RenovarSiempreCircuitoTor = renovarSiempreCircuitoTor

    def getRenovarSiempreCircuitoTor(self):
        return self.RenovarSiempreCircuitoTor

    def setDelayIntentoRenovacionCircuitoTor(self, delayIntentoRenovacionCircuitoTor):
        self.DelayIntentoRenovacionCircuitoTor = delayIntentoRenovacionCircuitoTor

    def getDelayIntentoRenovacionCircuitoTor(self):
        return self.DelayIntentoRenovacionCircuitoTor

    def seturl(self, Url):
        self.url = Url

    def geturl(self):
        return self.url

    def setRoute(self, route):
        self.Route = route

    def getRoute(self):
        return self.Route

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def writeFileJSON(self,file):
        outfile = open(file, 'w')
        outfile.write(self.toJSON())
        outfile.close()

