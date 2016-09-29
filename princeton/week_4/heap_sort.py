'''

Implement the heap-sort algorithm for efficient sorting.
Two phases:
  1) Construction phase
    First, implement bottom-up heap order
  2) Swap max item with smallest, then, continually sink until array has been sorted

Heapsort time complexity is O(N log N). Construction takes 2N compares and exchanges up front.
It's an nLogn in-place sorting algorithm.

'''

import random

class HeapSort(object):

  def __init__(self, array):
    self.heap = [ None ] + array

  def __sink(self, i, limit):
    c = i * 2
    size = limit
    while c < size:
      larger_c = c
      # checks to see if second child exists and is larger
      if c + 1 < size and self.heap[c + 1] > self.heap[c]: larger_c += 1
      if self.heap[i] < self.heap[larger_c]:
        self.heap[i], self.heap[larger_c] = self.heap[larger_c], self.heap[i]
      i = larger_c
      c = i * 2

  def order_heap(self):
    size = len(self.heap)
    for i in range(size // 2, 0, -1):
      print("Index: %d" % (i))
      self.__sink(i, size)

  def sort(self):
    self.order_heap()
    ordered = 1
    while ordered < len(self.heap):
      self.heap[1], self.heap[-ordered] = self.heap[-ordered], self.heap[1]
      self.__sink(1, ordered)
      ordered += 1

# reliable broken case -> order heap does not work
array = [1, 7, 5, 11, 12, 93, 21]

# array = random.sample(range(0, 10), 10)
heap_sort = HeapSort(array)
heap_sort.sort()
print(heap_sort.heap)
