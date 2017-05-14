import elTopoRequest.elTopoRequest as etr
import bs4

#myRequest = etr.getRequestTor("http://3g2upl4pq6kufc4m.onion/")
myRequest = etr.getRequest("http://www.google.es")


soup = bs4.BeautifulSoup ( myRequest.text, 'html.parser' )
print(soup)
