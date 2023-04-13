import Tree as T

#when we run out of examples or attributes we use this function
def Plurality_Value(exs):
    survived = 0
    unsurvived = 0
    for i in exs.survived:
        if(i==0): unsurvived+=1
        if(i==1): survived+=1
    if survived > unsurvived: return survived
    else: return unsurvived


def Importance(attributes, examples):
    
    return 0


#return a tree
def Decision_Tree_Learning(examples, attributes, parent_examples):
    if (len(examples)==0):
        return Plurality_Value(parent_examples)
    #checking if all examples have the same classification or not
    elif all(ex.survived == examples[0].survived for ex in examples):
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