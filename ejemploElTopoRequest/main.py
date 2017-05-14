import elTopoRequest.elTopoRequest as etr
import bs4

myRequest = etr.getRequest("http://3g2upl4pq6kufc4m.onion/")


soup = bs4.BeautifulSoup ( myRequest.text, 'html.parser' )
print(soup)
