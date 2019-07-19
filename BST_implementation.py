#This file is to implement the Binary Search Tree
#Function implemented:
#Insertion, Get Min, Get Max, In Order Traversal, deletion
#Initialization from Array, To Array

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.insertNode(self.root, data)
        else:
            self.root = Node(data)

    def insertNode(self, nodeToInsert, data):
        if data < nodeToInsert.value:
            if nodeToInsert.left:
                self.insertNode(nodeToInsert.left, data)
            else: nodeToInsert.left = Node(data)
        else:
            if nodeToInsert.right:
                self.insertNode(nodeToInsert.right, data)
            else: nodeToInsert.right = Node(data)

    def fromArray(self, arrayForInsertion):
        for x in arrayForInsertion:
            self.insert(x)

    def getMin(self):
        if self.root:
            return self.getMinNode(self.root)

    def getMinNode(self, nodeToGetMin):
        if nodeToGetMin.left:
            return self.getMinNode(nodeToGetMin.left)
        else:
            return nodeToGetMin.value

    def getMax(self):
        if self.root:
            return self.getMaxNode(self.root)

    def getMaxNode(self, nodeToGetMax):
        if nodeToGetMax.right:
            return self.getMaxNode(nodeToGetMax.right)
        else:
            return nodeToGetMax.value

    def traverse(self):
        if self.root:
            self.inOrderTraverse(self.root)

    def inOrderTraverse(self, nodeToTraverse):
        if nodeToTraverse.left:
            self.inOrderTraverse(nodeToTraverse.left)

        print(nodeToTraverse.value, " ")

        if nodeToTraverse.right:
            self.inOrderTraverse(nodeToTraverse.right)


    def toArray(self, arrayFromTree):
        if self.root:
            self.inOrderTraverseToArray(self.root, arrayFromTree)
            return arrayFromTree

    def inOrderTraverseToArray(self, nodeToTraverse, arrayFromTree):
        if nodeToTraverse.left:
            self.inOrderTraverseToArray(nodeToTraverse.left, arrayFromTree)

        arrayFromTree.append(nodeToTraverse.value)

        if nodeToTraverse.right:
            self.inOrderTraverseToArray(nodeToTraverse.right, arrayFromTree)


    def serializeNode(nodeToStartSerialize, serializeString):
        stringToAppend = str(nodeToStartSerialize.value, " ")
        serializeString = serializeString + stringToAppend
        if nodeToStartSerialize.left:
            self.serializeNode(nodeToStartSerialize.left, serializeString)
        else:
            stringToAppend = str("# ")
            serializeString = serializeString + stringToAppend

        if nodeToStartSerialize.right:
            self.serializeNode(nodeToStartSerialize.right, serializeString)
        else:
            stringToAppend = str("# ")
            serializeString = serializeString + stringToAppend


    def delete(self, value):
        if self.root:
            self.deleteNode(None, "lr", self.root, value)


    def deleteNode(self, parentNode, left_or_right ,nodeToStartDelete, value):
        ##first need to find the value to delete
        if nodeToStartDelete.value == value:
            if nodeToStartDelete.left and nodeToStartDelete.right:

                maxValue = self.getMaxNode(nodeToStartDelete.left)
                self.deleteNode(nodeToStartDelete,"l",nodeToStartDelete.left, maxValue)
                nodeToStartDelete.value = maxValue

            elif nodeToStartDelete.left:
                if (left_or_right == "l"):
                    if parentNode:
                        parentNode.left = nodeToStartDelete.left
                    else: nodeToStartDelete = nodeToStartDelete.left
                elif (left_or_right == "r"):
                    if parentNode:
                        parentNode.right = nodeToStartDelete.left
                    else: nodeToStartDelete = nodeToStartDelete.left
                else : nodeToStartDelete = nodeToStartDelete.left


            elif nodeToStartDelete.right:
                if (left_or_right == "l"):
                    if parentNode:
                        parentNode.left = nodeToStartDelete.right
                    else: nodeToStartDelete = nodeToStartDelete.right
                elif (left_or_right == "r"):
                    if parentNode:
                        parentNode.right = nodeToStartDelete.right
                    else:
                        nodeToStartDelete = nodeToStartDelete.right
                else: nodeToStartDelete = nodeToStartDelete.right

            else:
                if (left_or_right == "l"):
                    if parentNode:
                        parentNode.left = None
                    else:
                        nodeToStartDelete = None
                elif(left_or_right == "r"):
                    if parentNode:
                        parentNode.right = None
                    else: nodeToStartDelete = None
                else: nodeToStartDelete = None


        elif nodeToStartDelete.value < value:
            self.deleteNode(nodeToStartDelete,"r",nodeToStartDelete.right, value)
        else: self.deleteNode(nodeToStartDelete, "l", nodeToStartDelete.left, value)


##test BST
####construct BST by inserting with 9, 100, 6, -3, 5, 2
bst1 = BST()
bst1.insert(9)
bst1.insert(100)
bst1.insert(6)
bst1.insert(-3)
bst1.insert(5)
bst1.insert(2)

###Min/Max
print("Min of the BST with (9, 100, 6, -3, 5, 2) is: {}".format(bst1.getMin()))
print("Max of the BST with (9, 100, 6, -3, 5, 2) is: {}".format(bst1.getMax()))

###traverse
bst1.traverse()

###construct BST from array [4,0, 12, 7, 9, 23]
bst2 = BST()
bst2.fromArray([4,0, 12, 7, 9, 23])
print(*bst2.toArray([]))

##delet 12 from bst2
print("original bst1: ", *bst1.toArray([]))
bst1.delete(100)
print("delete node 100: ", *bst1.toArray([]))

print("original bst2: ", *bst2.toArray([]))
bst2.delete(4)
print("delete root 4: ", *bst2.toArray([]))
