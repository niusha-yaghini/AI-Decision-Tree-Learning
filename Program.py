import pandas as pd
import numpy as np
import csv
import Attribute

#reading data
data = pd.read_csv('test.csv')

print(data.loc[[15]])
print(list(data.loc[[15]]))
print(len(list(data.loc[[15]])))
# print(list(data.loc[[15]])[0])
# print(list(data.loc[[15]])[1])

var = data.loc[[15]].pclass
print("this is var")
print(var)



numOfAttributes = len(data.columns) - 1
numOfExamples = len(data.index)

AttributesNames = list(data.columns)

print(numOfAttributes)
print(numOfExamples)
print(AttributesNames)

#dividing data into educational and experimental with 50 and 50
# trainExamples = originalList[:]
# testExamples = originalList[:]

#list of class nodes of attributes
var = Attribute.AttributesAndValues(data, AttributesNames)
# print(var)