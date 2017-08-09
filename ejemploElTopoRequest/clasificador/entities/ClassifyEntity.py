##DOs atributos, uno que sea text y otro label, constructor, y hacer un json
import json
import string
import re
import codecs
class ClassifyEntity:

    def __init__(self, Text, Label):
        self.text = Text
        self.label = Label


    def toJSON(self):

        text = self.text
        dirty = self._removeNonAscii(text)
        newDirty = dirty.replace("'", '')
        newDirty2 = newDirty.replace("\\", "")
        newDirty3 = newDirty2.replace('"',"")


       ##MODIFICAR, ESTÁ FALLANDO TODO
        print(self.label)
        print(self.text)
        obj = {"text": newDirty3, "label": self.label}
        ##print("objeto")
        ##print(obj)
        ##print(newStrText)
        ##print("objeto2")
        ##print(json.dumps(obj))
        return obj


    def _removeNonAscii(self, s):
        return "".join(i for i in s if ord(i)<128)


