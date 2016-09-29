'''

Implement the heap-sort algorithm for efficient sorting.
Two phases:
  1) Construction phase
    First, implement bottom-up heap order
  2) Swap max item with smallest, then, continually sink until array has been sorted

'''

class HeapSort(object):

  def __init__(self, array):
    self.heap = [ None ] + array
    self.sorted = []

  def __sink(self, i):
    c = i * 2
    size = len(self.heap)
    while c < size:
      larger_c = c
      # checks to see if second child exists and is larger
      if c + 1 < size and self.heap[c + 1] > self.heap[c]: larger_c += 1
      if self.heap[i] < self.heap[larger_c]:
        self.heap[i], self.heap[larger_c] = self.heap[larger_c], self.heap[i]
      i = c
      c *= 2

  def order_heap(self):
    size = len(self.heap)
    for i in range(1, size // 2):
      self.__sink(i)

  def sort(self):
    self.order_heap()
    for i in range(1, len(self.heap)):
      self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
      self.sorted.append(self.heap.pop())
      self.__sink(1)

array = [9, 1, 4, 5, 2, 7, 3, 8, 6]
heap_sort = HeapSort(array)
heap_sort.sort()
print(heap_sort.sorted)
