import Tree as T
import numpy as np

#when we run out of examples or attributes we use this function
def Plurality_Value(exs):
    survived = 0
    unsurvived = 0
    for i in exs.survived:
        if(i==0): unsurvived+=1
        if(i==1): survived+=1
    if survived > unsurvived: return survived
    else: return unsurvived

def _entropy(examples):
    hist = np.bincount(examples)
    ps = hist / len(y)
    return -np.sum([p * np.log(p) for p in ps if p>0])
    

def gain(att, examples):
    p = 0
    for e in examples:
        if(e.survived == 0):
            p+=1
    for a in att.values:
        

def Importance(attributes, examples):
    entropy = []
    for att in attributes:
        x = gain(att, examples)
        entropy.append(x)
        
    return max(entropy)


def same_value(examples):
    a = examples[0].survived
    for e in examples:
        if(e.survived!=a):
            return False
    return True
        

#return a tree
def Decision_Tree_Learning(examples, attributes, parent_examples=None):
    if (len(examples)==0):
        return Plurality_Value(parent_examples)
    #checking if all examples have the same classification or not
    # elif all(ex.survived == examples[0].survived for ex in examples):
    #     return examples[0].survived
    elif(same_value(examples)):
        return examples[0].survived
    elif (len(attributes)==0):
        return Plurality_Value(examples)
    else:
        # entropy = []
        # for arg in attributes:
        #     entropy.append(Importance(arg, examples))
        #A is a attribute that has the biggest entropy of all
        #each attribute has values (such as "yes, No" or "Some, Full, None")
        # A = max(entropy)
        
        #importance gets the list of attributes and list of examples and return the attribute with biggest entropy on examples
        A = Importance(attributes, examples)
        #making a new decision tree with root A(choosen attribute)
        tree = T.Tree(A)
        for value in A:
            exs = list
            for e in examples:
                if(e.A == value):
                    exs.append(e)
            subtree = Decision_Tree_Learning(exs, attributes.remove(A), examples)
            #adding a branch to "tree" with label (A=value) and subtree "subtree"
        return tree