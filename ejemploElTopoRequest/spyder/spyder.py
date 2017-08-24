import sys

from configElTopo.config import config
from configElTopo.lecturaFicherosURL import lecturaFicherosURL
from spyder.AlmacenamientoDatos.jsonOutputWebInfoUtils import jsonOutputWebInfoUtils
from spyder.elTopoRequest import elTopoRequest as etr
from spyder.elTopoRequest.elTopoRequest import ElTopoRequestException
from spyder.filtroInformacion import filtroInformacion as fi
from spyder.filtroInformacion.HttpCodeException import HttpCodeException


# from googleSearch.googleSearch import googleSearch

# searcher = googleSearch();
# searcher.search(".onion")

class spyder:
    def __init__(self, rutaConfig="./configElTopo/config.json"):
        # PARAMETROS DE CONFIGURACION
        self.RutaConfig = rutaConfig
        self.configuracion = config(self.RutaConfig)
        self.RutaSalida = self.configuracion.getRutaSalida()
        self.RutaEntradaUrlsDICCIONARIO = self.configuracion.getRutaDiccionario()
        self.maxDepth = self.configuracion.getMaxDepth()
        self.UtilizarDiccionario = self.configuracion.getUsarDiccionario()
        self.UtilizarSiempreTor = self.configuracion.getUsarSiempreTor()
        self.RenovarSiempreCircuitoTor = self.configuracion.getRenovarSiempreCircuitoTor()
        self.DelayIntentoRenovacionCircuitoTor = self.configuracion.getDelayIntentoRenovacionCircuitoTor()
        # FIN PARAMETROS DE CONFIGURACION

        self.utilidadesJson = jsonOutputWebInfoUtils(self.RutaSalida)
        if self.UtilizarDiccionario:
            self.urlsFicheros = lecturaFicherosURL.leerDireccionesDiccionario(self.RutaEntradaUrlsDICCIONARIO)
        else:
            self.urlsFicheros = lecturaFicherosURL.leerDireccionesJSON(self.RutaConfig)

        #print("Las URLS son {0}".format(self.urlsFicheros))
        self.conexion = etr.elTopoRequest(self.UtilizarSiempreTor, self.RenovarSiempreCircuitoTor,
                                          self.DelayIntentoRenovacionCircuitoTor)

    def launch(self):
        for currentURL in self.urlsFicheros:
            try:
                filtro = fi.filtroInformacion(self.conexion, currentURL, maxDepth=self.maxDepth)
                print("Analizada la URL {0} ".format(filtro.getUrl()))
                datos = filtro.getAllDataRecursiveObject()
                contenido = filtro.getAllDataRecursiveJson(datos)
                self.utilidadesJson.escribirJsonContenidoWeb(contenido, currentURL, ".json", datos.getIsOnline())
            except ElTopoRequestException as e:
                print("La URL {0} no esta disponible".format(currentURL))
                #print("ElTopoRequestException!!!!!!!!{0}".format(e.valor))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json", False)
            except HttpCodeException as e:
                print("La URL {0} no esta disponible".format(currentURL))
                #print("HttpCodeException!!!!!!!{0}".format(e.valor))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json", False)
            except:
                print("La URL {0} no esta disponible".format(currentURL))
                #print("Error no contemplado: {0}".format(sys.exc_info()))
                self.utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json", False)
        print(
            "Los ficheros con los datos de las URLs analizadas estan en {0}".format(self.utilidadesJson.baseDirectory))
        return self.utilidadesJson.baseDirectory
