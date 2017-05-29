import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi
import sys
from elTopoRequest.elTopoRequest import ElTopoRequestException
from filtroInformacion.HttpCodeException import HttpCodeException
from AlmacenamientoDatos.jsonOutputWebInfoUtils import jsonOutputWebInfoUtils
from AlmacenamientoDatos.lecturaFicheroUrlOnion import lecturaFicheroUrlOnion


RutaSalida="/home/usertfm/SalidaJSON/"
RutaEntradaUrls="./configElTopo/config.json"

utilidadesJson = jsonOutputWebInfoUtils(RutaSalida)
urlsFicheros = lecturaFicheroUrlOnion.leerDireccionesOnion(RutaEntradaUrls)
print("Las URLS son {0}".format(urlsFicheros))
conexion = etr.elTopoRequest()

for currentURL in urlsFicheros:
    try:
      filtro = fi.filtroInformacion(conexion,currentURL,maxDepth=1)
      print("Analizada la URL {0} ".format(filtro.getUrl()))
      contenido= filtro.getAllDataRecursiveJson()
      utilidadesJson.escribirJsonContenidoWeb(contenido,currentURL,".json")
    except ElTopoRequestException as e:
      print(e.valor)
    except HttpCodeException as e:
      print(e.valor)
    except:
      print("Error no contemplado: {0}".format(sys.exc_traceback))
print("Los ficheros con los datos de las URLs analizadas estan en {0}".format(utilidadesJson.baseDirectory))



