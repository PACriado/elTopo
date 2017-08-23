import threading

import requests

from EntidadesRest.SpyderRequest import SpyderRequest
from EntidadesRest.SpyderResponse import SpyderResponse
from configElTopo.config import config
from spyderRestCaller.lecturaFicheroServidores import lecturaFicheroServidores


class SpyderRestCaller:
    def __init__(self, URL=""):
        self.url = URL

    def call(self, DATA=""):
        data = DATA.toJSON()
        r = requests.post(self.url, json=data)
        Response = SpyderResponse(jsonResponse=r.content.decode('UTF-8'))
        return Response

    def callList(self, rutaConfig="./configElTopo/config.json"):
        self.RutaConfig = rutaConfig
        self.configuracion = config(self.RutaConfig)
        rutaListaServidores = self.configuracion.getRutaServidoresSpyderRest()
        listaServidores = lecturaFicheroServidores.leerDireccionesDiccionario(rutaListaServidores)

        threads = []
        paths = []
        for urlServidor in listaServidores:
            newthread = ThreadSpyderCaller(urlServidor)
            threads.append(newthread)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            paths.append(t.filesPath)
        return paths


class ThreadSpyderCaller(threading.Thread):
    def __init__(self, URL):
        threading.Thread.__init__(self)
        self.url = URL
        self.filesPath = ""

    def run(self):
        print("Llamando a  " + self.url)
        caller = SpyderRestCaller(URL=self.url)
        request = SpyderRequest()
        response = caller.call(request)
        self.filesPath = response.filesPath
        print("FINALIZADO Llamando a  " + self.url)
