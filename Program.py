import pandas as pd
import numpy as np
import Attribute
import Example as ex


#reading data
data = pd.read_csv('test.csv')

# var = data.loc[[15]]
# print("this is var")
# print(var.name)
# print(var.values)

numOfAttributes = len(data.columns) - 1
numOfExamples = len(data.index)

AttributesNames = list(data.columns)

# print(numOfAttributes)
# print(numOfExamples)
# print(AttributesNames)

#The ratio of the number of training and testing examples = 50-50
trainRatio = 1/2
testRatio = 1/2

#list of train examples
trainExamples = []
for i in range(0, numOfExamples*trainRatio):
    trainExamples.append(ex.Example(data.loc[[15]]))
    
    
#list of test examples
testExamples = []    
for j in range(numOfExamples*testRatio, numOfExamples):
    testExamples.append(ex.Example(data.loc[[15]]))
    

    
#list of objects of attributes
var = Attribute.AttributesAndValues(data, AttributesNames)

