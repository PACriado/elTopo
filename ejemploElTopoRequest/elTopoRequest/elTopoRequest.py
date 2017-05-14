import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = { 'User-agent' : ua.firefox }
pro = { 'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}

def getRequestTor(url):
  try:
    r = requests.get( url, header, timeout=(5,15), proxies=pro)
    return r
  except:
    print(url+" error. Cant GetRequest")


def getRequest(url):
  try:
    r = requests.get( url, header, timeout=(5,15))
    return r
  except:
    print(url+" error. Cant GetRequest")
