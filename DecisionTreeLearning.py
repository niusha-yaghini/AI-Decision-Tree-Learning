import Tree

def Plurality_Value(exs):
    return 0

def Importance(arg, examples):
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
        entropy = list
        for arg in attributes:
            entropy.append(Importance(arg, examples))
        #A is a attribute that has the biggest entropy of all
        #each attribute has values (such as "yes, No" or "Some, Full, None")
        A = max(entropy)
        #making a new decision tree with root A(choosen attribute)
        tree = Tree.Making_Tree(A)
        for value in A:
            exs = list
            for e in examples:
                if(e.A == value):
                    exs.append(e)
            subtree = Decision_Tree_Learning(exs, attributes.remove(A), examples)
            #adding a branch to "tree" with label (A=value) and subtree "subtree"
        return tree