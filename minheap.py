"""
implementing minheap data-structure
"""
import heapq


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # to balance the inserted new element in the heap we heapify it
    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    # insert the element in the end of the list
    # then use heapify to maintain the heap property
    def push_heap(self, key):
        self.heap.append(key)
        self.size = self.size + 1
        self.heapify_up(self.size - 1)

    # to find the minimum child of the root
    # from both available child
    def min_child(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heap[2 * i] < self.heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    # to del with delete operation we move down
    # the new root to its logical correct position
    def heapify_down(self, i):
        while 2 * i <= self.size:
            min_child = self.min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child

    def heap_pop(self):
        value = self.heap[1]
        self.heap[0] = self.heap[self.size - 1]
        self.size = self.size - 1
        self.heap.pop()
        self.heapify_down(0)
        return value


class MinHeap2:
    def __init__(self):
        self.heap = []

    def push_heap(self, value):
        heapq.heappush(self.heap, value)

    def pop_heap(self):
        if self.heap:
            heapq.heappop(self.heap)
        else:
            return IndexError("heap is empty")

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return IndexError("heap is empty")


minheap = MinHeap()
minheap.push_heap(5)
minheap.push_heap(10)
minheap.push_heap(2)
minheap.push_heap(8)
print(minheap.heap_pop())
