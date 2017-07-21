##DOs atributos, uno que sea text y otro label, constructor, y hacer un json
import json

class ClassifyEntity:

    text = ""
    label = ""

    def __init__(self, Text, Label):
        self.text = Text
        self.label = Label


    def toJSON(self):

        obj = {u"text": self.text, u"label": self.label}
        print(json.dumps(obj))
        return obj



