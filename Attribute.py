import pandas as pd
import numpy as np

class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value


#this function will return a list of objects, that they are objects of attribute class(we will have each attribute with its value)
def AttributesAndValues(data, AttributesNames):
    listOfAttributes = []
    for attrName in AttributesNames:
        # value = {c: (a==c).nonzero()[i] for c in np.unique(a)}   
        # values = []
        # res = N.array(list_inp) 
        # unique_res = N.unique(res) 
        # for dt in data[f'{attrName}']:
        #     values.append(dt)
        # values = np.unique(np.array(data[f'{attrName}']))
        values = [*set(data[f'{attrName}'])]
        print(values)

        # values = [*set(values)]
        a = Attribute(attrName, values)
        listOfAttributes.append(a)
    return listOfAttributes
        
        
    
