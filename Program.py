import pandas as pd
import numpy as np


#reading data
data = pd.read_csv('test.csv')

numOfAttributes = len(data.columns) - 1
numOfExamples = len(data.index)

listOfAttributes = list(data.columns)


print(numOfAttributes)
print(numOfExamples)
print(listOfAttributes)

#dividing data into educational and experimental with 50 and 50




