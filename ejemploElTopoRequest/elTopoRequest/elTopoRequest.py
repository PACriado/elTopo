import requests
from fake_useragent import UserAgent

import utils.utils as utils
from elTopoRequest.ElTopoRequestException import ElTopoRequestException

import time


from stem import Signal
from stem.control import Controller


class elTopoRequest:
    ua = UserAgent()
    header = {'User-agent': ua.firefox}
    pro = {'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}
    utilizarSiempreTor=False
    renovarSiempreCircuitoTor=False
    delayIntentoRenovacionCircuitoTor=5

    def __init__(self,UtilizarSiempreTor,RenovarSiempreCircuitoTor,DelayIntentoRenovacionCircuitoTor):
        self.utilizarSiempreTor = UtilizarSiempreTor
        self.renovarSiempreCircuitoTor = RenovarSiempreCircuitoTor
        self.delayIntentoRenovacionCircuitoTor = DelayIntentoRenovacionCircuitoTor


    def getRequestTor(self, url):
        try:
            r = requests.get(url, self.header, timeout=(25, 85), proxies=self.pro)
            return r
        except:
            # AQUI LANZAMOS UNA EXCEPCION PORQUE NO HEMOS PODIDO CONECTAR A ESA WEB
            raise ElTopoRequestException(url + " EXCEPTION. Cant getRequestTor")

    def getRequestNoTor(self, url):
        try:
            if self.utilizarSiempreTor:
                r = requests.get(url, self.header, timeout=(25, 85), proxies=self.pro)
            else:
                r = requests.get(url, self.header, timeout=(25, 85))
            return r
        except:
            # AQUI LANZAMOS UNA EXCEPCION PORQUE NO HEMOS PODIDO CONECTAR A ESA WEB
            raise ElTopoRequestException(url + " EXCEPTION. Cant getRequestNoTor")

    def renew_connection(self):
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password = 'my_password')
            controller.signal(Signal.NEWNYM)

            var = controller.is_newnym_available()
            while var == False:
                    time.sleep(self.delayIntentoRenovacionCircuitoTor)
                    var = controller.is_newnym_available()
            controller.close()

    def getRequestAuto(self, url):
        if self.renovarSiempreCircuitoTor:
            self.renew_connection()

        if utils.utils.isOnionURL(url):
            return elTopoRequest.getRequestTor(self, url)
        else:
            return elTopoRequest.getRequestNoTor(self, url)
