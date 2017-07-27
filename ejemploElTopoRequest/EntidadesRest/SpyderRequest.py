import json


class SpyderRequest:
    def __init__(self, Url="", jsonRequest=""):
        if jsonRequest != '':
            self.__dict__ = json.loads(json.loads(jsonRequest))
        else:
            self.url = Url

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
