import socks
import socket
import requests
import bs4
from fake_useragent import UserAgent
ua = UserAgent()

url = "http://3g2upl4pq6kufc4m.onion/"
header = { 'User-agent' : ua.firefox }
pro = { 'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}

try:
    r = requests.get( url, header, timeout=(5,15), proxies=pro)
    soup = bs4.BeautifulSoup ( r.text, 'html.parser' )
    print(soup)
except:
    print(url+" error")
    print("Unexpected error:", sys.exc_info()[0])
