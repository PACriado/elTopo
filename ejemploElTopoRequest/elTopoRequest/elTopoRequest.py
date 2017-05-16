import requests
import utils.utils as utils
from fake_useragent import UserAgent
from elTopoRequest.ElTopoRequestException import ElTopoRequestException

class elTopoRequest:
  ua = UserAgent()
  header = { 'User-agent' : ua.firefox }
  pro = { 'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}

  def getRequestTor(self,url):
    try:
      r = requests.get( url, self.header, timeout=(5,15), proxies=self.pro)
      return r
    except:
        #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
      print(url+" error. Cant getRequestTor")
      raise ElTopoRequestException(url+" EXCEPTION. Cant getRequestTor")


  def getRequestNoTor(self,url):
    try:
      r = requests.get( url, self.header, timeout=(5,15))
      return r
    except:
        #AQUI DEBERIAMOS LANZAR UNA EXCEPCION
      print(url+" error. Cant getRequestNoTor")
      raise ElTopoRequestException(url+" EXCEPTION. Cant getRequestNoTor")

  def getRequestAuto(self,url):
      if utils.utils.isOnionURL(url):
          return elTopoRequest.getRequestTor(self,url)
      else:
          return elTopoRequest.getRequestNoTor(self,url)

