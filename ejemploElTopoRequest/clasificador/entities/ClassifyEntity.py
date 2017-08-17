##DOs atributos, uno que sea text y otro label, constructor, y hacer un json
import json
import string
import re
import codecs
import unicodedata, re

class ClassifyEntity:

    def __init__(self, Text, Label):
        self.text = Text
        self.label = Label


    def toJSON(self):

        text = self.text
        text = ''.join(filter(lambda x: x in string.printable, text))
        dirty = text
        #.decode('utf8','ignore')
        newDirty = dirty.replace("'", '')
        newDirty2 = newDirty.replace("\\", "")
        newDirty3 = newDirty2.replace('"',"")
        newDirty4 = newDirty3.replace("\\x", "")
       ##MODIFICAR, ESTÁ FALLANDO TODO
        print(self.label)
        print(self.text)
        obj = {"text": newDirty4, "label": self.label}
        ##print("objeto")
        ##print(obj)
        ##print(newStrText)
        ##print("objeto2")
        ##print(json.dumps(obj))
        return obj



