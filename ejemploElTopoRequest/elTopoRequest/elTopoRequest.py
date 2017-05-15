import requests
import ejemploElTopoRequest.utils.utils as utils
from fake_useragent import UserAgent

class elTopoRequest:
  ua = UserAgent()
  header = { 'User-agent' : ua.firefox }
  pro = { 'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}

  def getRequestTor(self,url):
    try:
      r = requests.get( url, self.header, timeout=(5,15), proxies=self.pro)
      return r
    except:
      print(url+" error. Cant getRequestTor")


  def getRequestNoTor(self,url):
    try:
      r = requests.get( url, self.header, timeout=(5,15))
      return r
    except:
      print(url+" error. Cant getRequestNoTor")

  def getRequestAuto(self,url):
      if utils.utils.isOnionURL(url):
          return elTopoRequest.getRequestTor(self,url)
      else:
          return elTopoRequest.getRequestNoTor(self,url)

