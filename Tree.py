import pandas as pd
import numpy as np
import Attribute

f = open("myfile.txt", "x")

#root is a attribute(that has its own values)(it is a node of attribute class)
class Tree:
    def __init__(self, root):
        self.root = root.name
        self.children = root.value
        f.write(f"choosen attribute = {root.name}\n")    
        f.write(f"values = {root.value}\n")    

    # with open ('writeme.txt', 'w') as file:  
    #     file.write('writeme')  