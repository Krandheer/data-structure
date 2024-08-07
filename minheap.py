"""
implementing minheap data-structure
"""

import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push_heap(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def pop_heap(self):
        if not self.heap:
            raise IndexError("heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left_child = 2 * i + 1
            right_child = 2 * i + 2 if 2 * i + 2 < len(self.heap) else None
            min_child = (
                left_child
                if right_child is None or self.heap[left_child] < self.heap[right_child]
                else right_child
            )

            if self.heap[i] <= self.heap[min_child]:
                break
            else:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child

    def peek(self):
        if not self.heap:
            raise IndexError("heap is empty")
        return self.heap[0]

    def is_empty(self):
        return not bool(self.heap)


class MinHeap2:
    def __init__(self):
        self.heap = []

    def push_heap(self, value):
        heapq.heappush(self.heap, value)

    def pop_heap(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return IndexError("heap is empty")

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.heap:
            return self.heap[0]
        return IndexError("heap is empty")


# minheap2 = MinHeap2()
# minheap2.push_heap(5)
# minheap2.push_heap(10)
# minheap2.push_heap(2)
# minheap2.push_heap(8)
# print(minheap2.pop_heap())

minheap = MinHeap()
minheap.push_heap(5)
minheap.push_heap(10)
minheap.push_heap(2)
minheap.push_heap(8)
print(minheap.pop_heap())
