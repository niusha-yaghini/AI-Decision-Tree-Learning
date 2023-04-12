import pandas as pd
import numpy as np
import csv
import Attribute

#reading data
data = pd.read_csv('test.csv')

rows = list(data)
print(rows[1])
# pd.set_option('display.max_rows', None)
# for r in data:
#     print(r)
# print(data.index)

# print(data.index)
# for i in data.index:
#     print()
# print(data[0].tolist)
# print(data[1].tolist)
# for row in data:
#     # print(''.join(row))
#     print(row)


numOfAttributes = len(data.columns) - 1
numOfExamples = len(data.index)

AttributesNames = list(data.columns)

print(numOfAttributes)
print(numOfExamples)
print(AttributesNames)

#dividing data into educational and experimental with 50 and 50
trainExamples = originalList[:]
testExamples = originalList[:]

#list of class nodes of attributes

var = Attribute.AttributesAndValues(data, AttributesNames)
# print(var)