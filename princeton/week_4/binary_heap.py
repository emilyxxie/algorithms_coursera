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

Children's order with respect to each other does not matter--> all works out in the end since popping out of queue takes the top node.
Top node is always floated based on two children, which are continually floated to the top.

Traversing through the priority queue via insertion or removal should take O(log N).


'''

class PriorityQueue(object):

  def __init__(self):
    self.heap = []

  def insert(self, val):
    pass

  def remove_max(self):
    pass

  def sink(self):
    pass

  def float(self):
    pass