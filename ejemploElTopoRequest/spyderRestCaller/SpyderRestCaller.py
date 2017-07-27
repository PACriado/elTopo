import requests
import json
import os
from EntidadesRest.SpyderRequest import SpyderRequest
from EntidadesRest.SpyderResponse import SpyderResponse

class SpyderRestCaller:
    def __init__(self,URL=""):
        self.url = URL

    def call(self,DATA=""):
        data = DATA
        r = requests.get(self.url, data=data)
        Response = SpyderResponse(jsonResponse = r.content.decode('UTF-8'))
        return  Response
