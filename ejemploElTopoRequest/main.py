import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi
import sys
from elTopoRequest.elTopoRequest import ElTopoRequestException
from filtroInformacion.HttpCodeException import HttpCodeException



conexion = etr.elTopoRequest()

urlTor="http://3g2upl4pq6kufc4m.onion/"
#url="http://www.google.es"
url="https://thehiddenwiki.org/"
try:
  filtroTor = fi.filtroInformacion(conexion,urlTor)
  print(filtroTor.getUrl())
  print(filtroTor.getTitle())
  print(filtroTor.getLinksHref())
  print(filtroTor.getLinksText())
except ElTopoRequestException as e:
  print(e.valor)
except HttpCodeException as e:
  print(e.valor)
except:
  print("Error no contemplado:", sys.exc_info())


try:
  filtro = fi.filtroInformacion(conexion,url)
  print(filtro.getUrl())
  print(filtro.getTitle())
  print(filtro.getLinksHref())
  print(filtro.getLinksText())
except ElTopoRequestException as e:
  print(e.valor)
except HttpCodeException as e:
  print(e.valor)
except:
  print("Error no contemplado:", sys.exc_info())




