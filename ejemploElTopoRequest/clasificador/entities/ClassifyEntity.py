##DOs atributos, uno que sea text y otro label, constructor, y hacer un json
import json

class ClassifyEntity:

    def __init__(self, Text, Label):
        self.text = Text
        self.label = Label


    def toJSON(self):

        newStrText = self.text.replace("\\", "")
        self.text.strip()
        self.text.replace('\\','')
       ##MODIFICAR, ESTÁ FALLANDO TODO
        obj = {"text": self.text, "label": self.label}
        ##print("objeto")
        ##print(obj)
        ##print(newStrText)
        ##print("objeto2")
        ##print(json.dumps(obj))
        return obj



