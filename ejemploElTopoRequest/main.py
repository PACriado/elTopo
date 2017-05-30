import sys

import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi
from AlmacenamientoDatos.jsonOutputWebInfoUtils import jsonOutputWebInfoUtils
from AlmacenamientoDatos.lecturaFicheroConfig import lecturaFicheroConfig
from elTopoRequest.elTopoRequest import ElTopoRequestException
from filtroInformacion.HttpCodeException import HttpCodeException
from AlmacenamientoDatos.lecturaFicherosURL import lecturaFicherosURL

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
        contenido = filtro.getAllDataRecursiveJson()
        utilidadesJson.escribirJsonContenidoWeb(contenido, currentURL, ".json")
    except ElTopoRequestException as e:
        print(e.valor)
    except HttpCodeException as e:
        print(e.valor)
    except:
        print("Error no contemplado: {0}".format(sys.exc_traceback))
print("Los ficheros con los datos de las URLs analizadas estan en {0}".format(utilidadesJson.baseDirectory))
