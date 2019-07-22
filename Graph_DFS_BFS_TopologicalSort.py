##This file implemented DFS, BFS and used DFS to find the Topological Sorting of a graph
##graph regresentation
##I'm using adjacency list(dictionary in python) to represent a graph, and the graph is directed but not weighted, no cycles
##vertexes are marked using integers

##Depth First Search
def DFS(graph, startingVertex, visitedList):
    if not visitedList[startingVertex]:
        print("Visiting {}".format(startingVertex))
        visitedList[startingVertex] = True

        ##get neighbors as a list of vertexes(numbers)
        if (startingVertex in graph): ##check if a vertex points to other vertexes
            neighbors = graph[startingVertex]
            for x in neighbors:
                DFS(graph, x, visitedList)
    return

##Breath First Search
##BFS will need to use the QUEUE data structure
##define a queue using linklist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.root = None
        self.tail = None
        self.size = 0

    def addToQueue(self, data): ##add to the end
        ##make a new Node
        nodeToAdd = Node(data)
        self.size += 1
        if not self.root:
            self.root = nodeToAdd
            self.tail = nodeToAdd
        else:
            self.tail.next = nodeToAdd
            self.tail = nodeToAdd

    def removeFromQueue(self): ##remove the first
        if self.root:
            tempData = self.root.data
            self.root = self.root.next
            self.size -= 1
            return tempData
        else:
            return -1


    def size(self):
        return self.size


def BFS(graph, startingVertex, visitedList, vertexQueue):
    vertexQueue.addToQueue(startingVertex) ##add to the queue
    visitedList[startingVertex] = True
    print("Visiting {}".format(startingVertex))

    while vertexQueue.size > 0:
        vertex = vertexQueue.removeFromQueue()
        ##get the neighbors
        if vertex in graph:
            neighbors = graph[vertex]
            for x in neighbors:
                if not visitedList[x]:
                    vertexQueue.addToQueue(x)
                    visitedList[x] = True
                    print("Visiting {}".format(x))



######Find the Topological Order of the graph using DFS
def DFS_for_Topo(graph, startingVertex, visitedList, topoList):
    if not visitedList[startingVertex]:
        visitedList[startingVertex] = True

        ##get neighbors as a list of vertexes(numbers)
        if (startingVertex in graph): ##check if a vertex points to other vertexes
            neighbors = graph[startingVertex]
            for x in neighbors:
                DFS_for_Topo(graph, x, visitedList, topoList)
            topoList.append(startingVertex)
        else:
            topoList.append(startingVertex)
        return topoList

def TopologicalSort(graph, visitedList):
    ##get number of vertexes in the graph
    nVertexes = len(visitedList)
    topoList = []
    for i in range(0, nVertexes):
        if not visitedList[i]:
            topoList = DFS_for_Topo(graph, i, visitedList, topoList)
            #print(*topoList)
    topoList.reverse()
    return topoList


###Test DFS
graph1 = dict([
    (0, [2, 6]),
    (1, [3, 6]),
    (2, [1, 3]),
    (3, [4, 5]),
    (6, [5])
])

visitedList = [False] * 7
print("Traversing graph using DFS")
DFS(graph1, 0, visitedList)

###Test BFS
visitedList = [False] * 7
queue2 = Queue()
print("Traversing graph using BFS")
BFS(graph1, 0, visitedList, queue2)


###Test TopologicalSort
visitedList = [False] * 7
print("TopologicalSort")
TopoSortList = TopologicalSort(graph1, visitedList)
print("The topological sort list for graph1 is: ")
print(TopoSortList)
