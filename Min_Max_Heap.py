##This file implemented minHeap
##function included: insert, delete the min, heapify top down, heapify bottom up, get min
class minHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)

        if len(self.heap) == 1:
            return
        else:
            self.heapifyUp(len(self.heap) - 1)
            return

    def deleteMin(self):
        if len(self.heap) == 0:
            return
        elif len(self.heap) == 1:
            self.heap.pop(len(self.heap) -1)
            return
        else:
            ##move last item to first
            self.heap[0]  = self.heap[len(self.heap) - 1]
            ##pop the last item
            self.heap.pop(len(self.heap) -1)
            ##move item around to keep minHeap property
            self.heapifyDown(0)

    def getMin(self):
        return self.heap[0]

    def leftChildIndex(self, selfIndex):
        return selfIndex*2 + 1

    def rightChildIndex(self, selfIndex):
        return selfIndex*2 + 2

    def parentIndex(self, selfIndex):
        return int((selfIndex -1)/2)

    def heapifyUp(self, IndexToMoveUp):
        while IndexToMoveUp > 0:
            parent = self.parentIndex(IndexToMoveUp)
            if self.heap[parent] <= self.heap[IndexToMoveUp]:
                break
            else:
                tempParent = self.heap[parent]
                self.heap[parent] = self.heap[IndexToMoveUp]
                self.heap[IndexToMoveUp] = tempParent
                IndexToMoveUp = parent

    def heapifyDown(self, IndexToMoveDown):
        while self.leftChildIndex(IndexToMoveDown) < len(self.heap):
            ##find the smallest of the child
            leftIndex = self.leftChildIndex(IndexToMoveDown)
            rightIndex = self.rightChildIndex(IndexToMoveDown)

            if rightIndex >= len(self.heap):
                smallestIndex = leftIndex
            elif self.heap[leftIndex] <= self.heap[rightIndex]:
                smallestIndex = leftIndex
            else:
                smallestIndex = rightIndex

            ##compare the smallest child to the parent
            if (self.heap[smallestIndex] >= self.heap[IndexToMoveDown]):
                break
            else:
                tempParent = self.heap[IndexToMoveDown]
                ##swap
                self.heap[IndexToMoveDown] = self.heap[smallestIndex]
                self.heap[smallestIndex] = tempParent
                IndexToMoveDown = smallestIndex


##test
##construct minHeap: 3, 8, 0, 2, 1, 11, 19, 35
minHeap1 = minHeap()
minHeap1.insert(3)
minHeap1.insert(8)
minHeap1.insert(0)
minHeap1.insert(2)
minHeap1.insert(1)
minHeap1.insert(11)
minHeap1.insert(19)
minHeap1.insert(35)

print(*minHeap1.heap)

minHeap1.deleteMin()
print(*minHeap1.heap)
print(minHeap1.getMin())

minHeap1.insert(17)
print(*minHeap1.heap)
