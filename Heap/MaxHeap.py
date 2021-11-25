#Implementing Max Heap

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap.pop()
            return max
        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            temp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = temp
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for x in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(x)


heap = MaxHeap()
heap.buildHeap([1, 12, 54, 62, 88, 91])
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.removeMax())
print(heap.removeMax())
print(heap.removeMax())
print(heap.getMax())