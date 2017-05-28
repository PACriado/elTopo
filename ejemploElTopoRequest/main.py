import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi
import sys
from elTopoRequest.elTopoRequest import ElTopoRequestException
from filtroInformacion.HttpCodeException import HttpCodeException
from AlmacenamientoDatos.jsonUtils import jsonUtil



conexion = etr.elTopoRequest()
utilidadesJson = jsonUtil('/home/usertfm/SalidaJSON/')

urlTor="http://3g2upl4pq6kufc4m.onion/"
#url="http://www.google.es"
#url="https://thehiddenwiki.org/"
url="http://info.cern.ch/"
'''
try:
  filtroTor = fi.filtroInformacion(conexion,urlTor,maxDepth=1)
  print(filtroTor.getUrl())
  print(filtroTor.getTitle())
  print(filtroTor.getLinksHref())
  print(filtroTor.getLinksText())
  print(filtroTor.getAllDataRecursiveJson())
except ElTopoRequestException as e:
  print(e.valor)
except HttpCodeException as e:
  print(e.valor)
except:
  print("Error no contemplado:", sys.exc_traceback)
'''

try:
  filtro = fi.filtroInformacion(conexion,url,maxDepth=1)
  print(filtro.getUrl())
  print(filtro.getTitle())
  print(filtro.getLinksHref())
  print(filtro.getLinksText())
  contenido= filtro.getAllDataRecursiveJson()
  print(contenido)
  utilidadesJson.escribirJson(contenido,"salida",".json")
except ElTopoRequestException as e:
  print(e.valor)
except HttpCodeException as e:
  print(e.valor)
except:
  print("Error no contemplado:", sys.exc_traceback)




