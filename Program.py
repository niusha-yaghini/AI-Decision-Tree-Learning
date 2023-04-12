import pandas as pd
import numpy as np
import csv
import Attribute

#reading data
data = pd.read_csv('test.csv')

print(list(data.loc[[15]]))

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