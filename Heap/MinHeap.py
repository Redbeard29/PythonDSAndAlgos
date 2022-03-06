#Implementing Min Heap

class MinHeap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMin(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.__minHeapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap.pop()
            return min
        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateUp(parent)

    def __minHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = temp
            self.__minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for x in range(len(self.heap) - 1, -1, -1):
            self.__minHeapify(x)


myHeap = MinHeap()
myHeap.buildHeap([300, 23, 17, 5, 7, 8, 9, 12])
myHeap.insert(1)
myHeap.insert(3)
print(myHeap.removeMin())
print(myHeap.removeMin())
print(myHeap.removeMin())
print(myHeap.removeMin())
print(myHeap.getMin())
