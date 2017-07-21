##Un array de entities creado antes. UN metodo put para meter a la lista, happen. Esta clase crear metodo que sea el que nos genere el json como lo acepta txtblob.

class EntitiesArray:

    classifyEntity = ""
    entityArray = []

    def __init__(self, ClassifyEntity):
        self.classifyEntity = ClassifyEntity

    def createJson(self):
        self.entityArray.append(self.classifyEntity.toJSON())
        return self.entityArray

