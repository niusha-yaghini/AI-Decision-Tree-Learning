import pandas as pd
import numpy as np
import Attribute


#reading data
data = pd.read_csv('test.csv')

numOfAttributes = len(data.columns) - 1
numOfExamples = len(data.index)

AttributesNames = list(data.columns)

print(numOfAttributes)
print(numOfExamples)
print(AttributesNames)

#dividing data into educational and experimental with 50 and 50

#list of class nodes of attributes


listOfAttributes = []
i = 0
for attrName in AttributesNames:
    # value = {c: (attrName==c).nonzero()[i] for c in np.unique(attrName)}   
    # a = Attributes
    values = []
    for dt in data[f'{attrName}']:
        values.append(dt)
    values = [*set(values)]
    print(values)
    a = Attribute.Attribute(attrName, values)
    listOfAttributes.append(a)
    

print(listOfAttributes)