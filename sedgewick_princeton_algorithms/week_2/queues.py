# Queue -> FIFO, first in first out

class Queue(object):

  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def is_empty(self, item):
    return len(self.items)

  def show_all(self):
    return self.items

# However, this queue runs pretty slowly as it grows larger, as
# the "enqueue" uses insert(), which requires that each item
# in array shifts over by one

# TODO: implement a faster solution to enqueue

# TODO: implement node queue using linked list