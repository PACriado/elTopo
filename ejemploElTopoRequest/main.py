import elTopoRequest.elTopoRequest as etr
import filtroInformacion.filtroInformacion as fi


conexion = etr.elTopoRequest()

urlTor="http://3g2upl4pq6kufc4m.onion/"
url="http://www.google.es"

filtroTor = fi.filtroInformacion(conexion,urlTor)
filtro = fi.filtroInformacion(conexion,url)

print(filtroTor.getTitle())
print(filtro.getTitle())

