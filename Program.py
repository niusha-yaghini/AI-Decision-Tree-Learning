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


# listOfAttributes = []
# i = 0
# for attrName in AttributesNames:
#     # value = {c: (attrName==c).nonzero()[i] for c in np.unique(attrName)}   
#     # a = Attributes
#     values = []
#     for dt in data[f'{attrName}']:
#         values.append(dt)
#     values = [*set(values)]
#     print(values)
#     a = Attribute.Attribute(attrName, values)
#     listOfAttributes.append(a)
    

# print(listOfAttributes)

# values = np.array(data['ticket'])
# print(values)

# values = np.unique(values)
# # values = [*set(values)]
# print(values)


# listOfAttributes = []
# for attrName in AttributesNames:
#     # value = {c: (a==c).nonzero()[i] for c in np.unique(a)}   
#     # values = []
#     # res = N.array(list_inp) 
#     # unique_res = N.unique(res) 
#     # for dt in data[f'{attrName}']:
#     #     values.append(dt)
#     # values = np.array(data[f'{attrName}'])
#     # values = np.unique(values)
#     values = [*set(data[f'{attrName}'])]
#     # print(values)
#     a = Attribute.Attribute(attrName, values)
#     # print(a)
#     listOfAttributes.append(a)

# print(listOfAttributes)

var = Attribute.AttributesAndValues(data, AttributesNames)
print(var)