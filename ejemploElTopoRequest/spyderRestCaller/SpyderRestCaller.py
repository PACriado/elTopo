import requests
import json
import os

from EntidadesRest.SpyderResponse import SpyderResponse

class SpyderRestCaller:
    def __init__(self,URL=""):
        self.url = URL

    def call(self,DATA=""):
        data = DATA.toJSON()
        r = requests.post(self.url, json=data)
        Response = SpyderResponse(jsonResponse = r.content.decode('UTF-8'))
        return  Response
