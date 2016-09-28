'''

Python Priority Queue using a binary heap implementation via array.
Unlike stacks--first in, first out--or queues--which are first in, last out--
priority queues serve items with highest priority first.

A heap is a binary tree with a few special properties:
  1) Shape Property
     - Binary heap is a complete binary tree.
     - This means all nodes of a level must be filled out before moving on to the next
  2) Heap property
     - Conforms to an ordering: all parent nodes will have the same size property in relation to all of its children
     - So, min heap -> all parents will be smaller than children, max heap -> all parents larger than children

Array structure: represent nodes of children using arithmetic -> all children's nodes are 2k and 2k + 1

Children's order with respect to each other does not matter--> all works out in the end since popping out of queue takes the top node.
Top node is always floated based on two children, which are continually floated to the top.

Traversing through the priority queue via insertion or removal should take O(log N).


'''

class MaxPriorityQueue(object):

  def __init__(self):
    # using the array structure, we'll need to set aside position 0
    # to simplify the arithmetic for traversal
    self.heap = [ None ]

  def insert(self, val):
    self.heap.append(val)
    self.rise()

  def remove_max(self):
    self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
    self.heap.pop()
    self.sink()

  def rise(self):
    i = len(self.heap) - 1
    while (i > 1 and self.heap[i] > self.heap[i // 2]):
      self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
      i //= 2

  def sink(self):
    i = 1
    c1 = i * 2
    while c1 < len(self.heap):
      larger_child = c1 if self.heap[c1] > self.heap[c2] else c2
      if self.heap[i] < self.heap[larger_child]:
        self.heap[i], self.heap[larger_child] = self.heap[larger_child], self.heap[i]
        if larger_child % 2 == 0:
          i = c1
        else:
          i = c2
        c1 *= 2
        c2 *= 2
      else:
        return


queue = MaxPriorityQueue()
queue.insert(15)
queue.insert(12)
queue.insert(10)
queue.insert(5)
queue.insert(3)
queue.remove_max()
print(queue.heap)