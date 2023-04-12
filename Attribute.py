import pandas as pd
import numpy as np

#attributes class
class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value


#making a list of objects of attribute class(we will have each attribute with its value)
def AttributesAndValues(data, AttributesNames):
    listOfAttributes = []
    for attrName in AttributesNames:
        values = [*set(data[f'{attrName}'])]
        print(values)
        a = Attribute(attrName, values)
        listOfAttributes.append(a)
    return listOfAttributes