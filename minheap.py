"""
implementing minheap data-structure
"""


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # to balance the inserted new element in the heap
    # we heapify it
    def heapifyUp(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    # insert the element in the end of the list
    # then use heapify to maintain the heap property
    def insert(self, key):
        self.heap.append(key)
        self.size = self.size + 1
        self.heapifyUp(self.size)

    # to del with delete operation we move down
    # the new root to its logical correct position
    def heapifyDown(self, i):
        while 2 * i <= self.size:
            min_child = self.minChild(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child

    # to find the minimum child of the root
    # from both available child
    def minChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heap[2 * i] < self.heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def delMin(self):
        value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.heapifyDown(1)
        return value
