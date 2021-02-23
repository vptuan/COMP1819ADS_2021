def BinaryTree(r):
	return [r, [], []]

def insertLeft(root,newBranch):
    temp = root.pop(1) # remove left branch of root and assign to temp
    print(temp, len(temp))
    if len(temp) > 1: #  already a subtree temp at left of root, add a new left with temp being the left branch of newBranch
        root.insert(1,[newBranch,temp,[]])
    else: # if t is null, len = 0, no left yet
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

tree = BinaryTree('a')
print(tree)
insertLeft(tree,'b')
# print("insertLeft ", tree)
# insertLeft(getLeftChild(tree),'d')
print(tree)
insertLeft(tree,'c')
print(tree)

# insertRight(tree,'c')
# insertLeft(getRightChild(tree),'e')
# insertRight(getRightChild(tree),'f')

# print(tree)