#This file is to implement the doubly linklist
#Function implemented:
#insertHead, insertTail, insertFromList, traverseLinkList
#delete
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertHead(self, data):
        nodeToInsert = Node(data)
        if self.head:
            nodeToInsert.next = self.head
            self.head.previous = nodeToInsert
            self.head = nodeToInsert
        else:
            self.head = nodeToInsert
            self.tail = nodeToInsert

        self.size += 1


    def insertTail(self, data):
        nodeToInsert = Node(data)
        if self.tail:
            self.tail.next = nodeToInsert
            nodeToInsert.previous = self.tail
            self.tail = nodeToInsert
        else:
            self.head = nodeToInsert
            self.tail = nodeToInsert

        self.size += 1

    def insertFromList(self, listToInsert):
        for x in listToInsert:
            self.insertTail(x)

    def size(self):
        return self.size

    def delete(self, data):
        if self.size == 0:
            return
        else:
            found = 0
            nodeToStart = self.head
            while (not found) and nodeToStart:
                if nodeToStart.data == data:
                    found = 1
                else: nodeToStart = nodeToStart.next

            if found:
                previousNode = nodeToStart.previous
                nextNode = nodeToStart.next

                previousNode.next = nextNode
                nextNode.previous = previousNode

                self.size -= 1

    def traverseLinkList(self):
        if self.size == 0:
            print("Empty List!")
            return

        else:
            count = 0
            nodeToStart = self.head
            while  count < self.size:
                print("Node {} is {}".format(count, nodeToStart.data))
                count += 1
                nodeToStart = nodeToStart.next


##############TESTS##############################################
list1 = [0, 34, 28, 10, 17, -3]
linkList1 = LinkList()
linkList1.insertFromList(list1)
linkList1.traverseLinkList()
linkList1.insertHead(100)
linkList1.delete(28)
linkList1.traverseLinkList()

print("The size of the link list is: {}".format(linkList1.size))
