##Un array de entities creado antes. UN metodo put para meter a la lista, happen. Esta clase crear metodo que sea el que nos genere el json como lo acepta txtblob.
##crear metodo para pasar a string
class EntitiesArray:

    def __init__(self):
        self.entityArray = []

    def add(self, newObject):
        self.entityArray.append(newObject.toJSON())

    def createJson(self):
        return self.entityArray

    def createJsonString(self):
        print(self.entityArray)
        values = ','.join(str(v) for v in self.entityArray)
        return values
