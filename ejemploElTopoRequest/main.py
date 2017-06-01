import sys

import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi
from AlmacenamientoDatos.jsonOutputWebInfoUtils import jsonOutputWebInfoUtils
from AlmacenamientoDatos.lecturaFicheroConfig import lecturaFicheroConfig
from elTopoRequest.elTopoRequest import ElTopoRequestException
from filtroInformacion.HttpCodeException import HttpCodeException
from AlmacenamientoDatos.lecturaFicherosURL import lecturaFicherosURL

#from googleSearch.googleSearch import googleSearch

#searcher = googleSearch();
#searcher.search(".onion")


RutaConfig = "./configElTopo/config.json"

RutaSalida = lecturaFicheroConfig.leerRutaSalida(RutaConfig)
RutaEntradaUrlsDICCIONARIO = lecturaFicheroConfig.leerRutaDiccionario(RutaConfig)
maxDepth = lecturaFicheroConfig.leerMaxDepth(RutaConfig)
UtilizarDiccionario = lecturaFicheroConfig.leerUsarDiccionario(RutaConfig)

utilidadesJson = jsonOutputWebInfoUtils(RutaSalida)
if UtilizarDiccionario:
    urlsFicheros = lecturaFicherosURL.leerDireccionesDiccionario(RutaEntradaUrlsDICCIONARIO)
else:
    urlsFicheros = lecturaFicherosURL.leerDireccionesJSON(RutaConfig)

print("Las URLS son {0}".format(urlsFicheros))
conexion = etr.elTopoRequest()

for currentURL in urlsFicheros:
    try:
        filtro = fi.filtroInformacion(conexion, currentURL, maxDepth=maxDepth)
        print("Analizada la URL {0} ".format(filtro.getUrl()))
        datos = filtro.getAllDataRecursiveObject()
        contenido = filtro.getAllDataRecursiveJson(datos)
        utilidadesJson.escribirJsonContenidoWeb(contenido, currentURL, ".json",datos.getIsOnline())

    except ElTopoRequestException as e:
        print("ElTopoRequestException!!!!!!!!{0}".format(e.valor))
        utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
    except HttpCodeException as e:
        print("HttpCodeException!!!!!!!{0}".format( e.valor))
        utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
    except:
        print("Error no contemplado: {0}".format(sys.exc_info()))
        utilidadesJson.escribirJsonContenidoWeb(currentURL, currentURL, ".json",False)
print("Los ficheros con los datos de las URLs analizadas estan en {0}".format(utilidadesJson.baseDirectory))
