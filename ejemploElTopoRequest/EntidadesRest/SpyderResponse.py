import json


class SpyderResponse:
    def __init__(self,FilesPath="",jsonResponse=""):
        if jsonResponse != '':
            print(jsonResponse)
            self.__dict__ = json.loads(jsonResponse)
        else:
            self.filesPath = FilesPath


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
