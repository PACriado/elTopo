import ejemploElTopoRequest.elTopoRequest.elTopoRequest as etr
import bs4


conexion = etr.elTopoRequest()
urlTor="http://3g2upl4pq6kufc4m.onion/"
url="http://www.google.es"


myRequestOnion = conexion.getRequestAuto(urlTor)
myRequest = conexion.getRequestAuto(url)
soupOnion = bs4.BeautifulSoup(myRequestOnion.text, 'html.parser')
print(soupOnion)
soup = bs4.BeautifulSoup ( myRequest.text, 'html.parser' )
print(soup)


