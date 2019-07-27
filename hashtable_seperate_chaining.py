##This class implemented HashTable
##used seperate chaining to handle collision
##used linklist to store key, value pairs

##function implemented for HashTable
##insertion, deletion, search, get array index of the key

import hashlib
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkListForSeperateChaining:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertTail(self, key, value):
        nodeToInsert = Node(key, value)
        if not self.head:
            self.head = nodeToInsert
        else: ##traverse the linkList
            nodeToStart = self.head
            while nodeToStart:
                if nodeToStart.key == key: ##check whether key is already in the linklist
                    break
                elif not nodeToStart.next: ##check if nodeToStart is the tail
                    nodeToStart.next = nodeToInsert ## insert
                    break
                else: ##keep looping
                    nodeToStart = nodeToStart.next
        self.size += 1

    def searchKey(self, key):
        if self.size == 0:
            print("Nothing in the list")
            return None
        else:
            nodeToSearch = self.head
            while nodeToSearch:
                if nodeToSearch.key == key:
                    return nodeToSearch
                else:
                    nodeToSearch = nodeToSearch.next
            return None


    def size(self):
        return self.size

    def delete(self, key):
        if self.size == 0:
            print("Nothing to delete!")
            return
        else:
            found = 0
            parentNode = None ##keep track of the parent node
            nodeToSearch = self.head
            while not found and nodeToSearch:
                if nodeToSearch.key == key:
                    found = 1
                else:
                    parentNode = nodeToSearch
                    nodeToSearch = nodeToSearch.next

            if not found:
                print("Nothing found to delete!")
            else:
                if not parentNode:
                    self.head = nodeToSearch.next
                else:
                    parentNode.next = nodeToSearch.next

                del nodeToSearch
                self.size -= 1
                return

class HashTable:
    def __init__(self, size):
        self.size = size
        self.ht = [None] * self.size

    def getIndex(self, key):
        ##hash the key
        keyHash = int(hashlib.md5(key.encode()).hexdigest(), 16) ##hexdigest gives out base 16
        ##get the hashed key into the range of 0 through size -1
        keyIndex = keyHash % self.size
        print("KeyIndex: {}".format(keyIndex))
        return keyIndex

    def insertHashTable(self, key, value):
        ##get Index
        keyIndex = self.getIndex(key)

        ##insert
        linkListToInsert = self.ht[keyIndex]
        if not linkListToInsert:
            linkListForIndex = LinkListForSeperateChaining()
            linkListForIndex.insertTail(key, value)
            self.ht[keyIndex] = linkListForIndex
        else:
            linkListToInsert.insertTail(key,value)

    def findKey(self, key):
        ##get Index
        keyIndex = self.getIndex(key)

        ##search
        linkListToSearch = self.ht[keyIndex]
        if not linkListToSearch:
            print("Key {} is not in the hash table".format(key))
            return None
        else:
            keyValue = linkListToSearch.searchKey(key)
            if not keyValue:
                print("Key {} is not in the hash table".format(key))
            else:
                print("Key: {}, Value: {}".format(keyValue.key, keyValue.value))
            return keyValue

    def deleteKey(self, key):
        ##get Index
        keyIndex = self.getIndex(key)

        ##delete
        linkListForDeletion = self.ht[keyIndex]
        if not linkListForDeletion:
            print("Key {} is not in the hash table".format(key))
            return
        else:
            linkListForDeletion.delete(key)
            return

################TEST HASHTABLE###########
ht1 = HashTable(200)
ht1.insertHashTable("Andrew", 21)
ht1.insertHashTable("Mary", 100)
ht1.insertHashTable("Brenton", 28)
ht1.insertHashTable("April", 10)
ht1.insertHashTable("Anderson", 210)
ht1.insertHashTable("Paul", 180)
ht1.insertHashTable("Steven", 2)
ht1.insertHashTable("Nicole", 100)

ht1.findKey("Steven")
ht1.deleteKey("Steven")
ht1.findKey("Steven")
ht1.findKey("Nicole")
