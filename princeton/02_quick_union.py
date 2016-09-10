'''

- Construct uses a list, with indexes again representing the nodes, and the corresponding elements keeping track of whether a node is part of a component
- This time, the elements represent a pointer to the parent
- Faster unions using this construct, as we only really have to change the element of the new node
- Here, unions will always add on the parent
- Problems arise when the trees are massive -- one must traverse through a large tree to get to root

'''

class QuickFind(object):

  def __init__(self, array_size):
    self.array = range(0, array_size)

  def connected(self, x, y):
    return self.find_root(x) == self.find_root(y)

  def find_root(self, index):
    while self.array[index] != index:
      index = self.array[index]
    return index

  # we want to attach the first number to the component of the second number
  def union(self, x, y):
    root_y = self.find_root(y)
    self.array[x] = root_y


# some test cases
qf = QuickFind(8)
qf.union(1, 2)
qf.union(2, 6)
print qf.connected(1, 6)