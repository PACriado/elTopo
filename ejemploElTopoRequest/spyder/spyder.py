import sys

from spyder.filtroInformacion.HttpCodeException import HttpCodeException

from configElTopo.lecturaFicheroConfig import lecturaFicheroConfig
from configElTopo.lecturaFicherosURL import lecturaFicherosURL
from spyder.AlmacenamientoDatos.jsonOutputWebInfoUtils import jsonOutputWebInfoUtils
from spyder.elTopoRequest import elTopoRequest as etr
from spyder.elTopoRequest.elTopoRequest import ElTopoRequestException
from spyder.filtroInformacion import filtroInformacion as fi

#from googleSearch.googleSearch import googleSearch

#searcher = googleSearch();
#searcher.search(".onion")

class spyder:

    def __init__(self, rutaConfig= "./configElTopo/config.json"):
        #PARAMETROS DE CONFIGURACION
        self.RutaConfig = rutaConfig
        self.RutaSalida = lecturaFicheroConfig.leerRutaSalida(self.RutaConfig)
        self.RutaEntradaUrlsDICCIONARIO = lecturaFicheroConfig.leerRutaDiccionario(self.RutaConfig)
        self.maxDepth = lecturaFicheroConfig.leerMaxDepth(self.RutaConfig)
        self.UtilizarDiccionario = lecturaFicheroConfig.leerUsarDiccionario(self.RutaConfig)
        self.UtilizarSiempreTor = lecturaFicheroConfig.leerSiempreTor(self.RutaConfig)
        self.RenovarSiempreCircuitoTor= lecturaFicheroConfig.leerRenovarSiempreCircuitoTor(self.RutaConfig)
        self.DelayIntentoRenovacionCircuitoTor = lecturaFicheroConfig.leerDelayIntentoRenovacionCircuitoTor(self.RutaConfig)
        #FIN PARAMETROS DE CONFIGURACION

        self.utilidadesJson = jsonOutputWebInfoUtils(self.RutaSalida)
        if self.UtilizarDiccionario:
            self.urlsFicheros = lecturaFicherosURL.leerDireccionesDiccionario(self.RutaEntradaUrlsDICCIONARIO)
        else:
            self.urlsFicheros = lecturaFicherosURL.leerDireccionesJSON(self.RutaConfig)

        print("Las URLS son {0}".format(self.urlsFicheros))
        self.conexion = etr.elTopoRequest(self.UtilizarSiempreTor, self.RenovarSiempreCircuitoTor,self.DelayIntentoRenovacionCircuitoTor)

    def launch(self):
        for currentURL in self.urlsFicheros:
            try:
                filtro = fi.filtroInformacion(self.conexion, currentURL, maxDepth=self.maxDepth)
                print("Analizada la URL {0} ".format(filtro.getUrl()))
                datos = filtro.getAllDataRecursiveObject()
                contenido = filtro.getAllDataRecursiveJson(datos)
                self.utilidadesJson.escribirJsonContenidoWeb(contenido, currentURL, ".json",datos.getIsOnline())
                prueba = datos.getAllSpans()
                print("**********")
                print(prueba)
                print("**********")

            except ElTopoRequestException as e:
                print("ElTopoRequestException!!!!!!!!{0}".format(e.valor))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
            except HttpCodeException as e:
                print("HttpCodeException!!!!!!!{0}".format( e.valor))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
            except:
                print("Error no contemplado: {0}".format(sys.exc_info()))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
        print("Los ficheros con los datos de las URLs analizadas estan en {0}".format(self.utilidadesJson.baseDirectory))
