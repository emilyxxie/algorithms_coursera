'''

- How to get around the problem of potentially massive trees?
- we can keep track of how tall the trees are, and when doing unions,
  and always link the root of the smaller tree to the root of the larger tree.
- Before, we did not pay any mind to which one we linked to which


- By doing this, we only have to traverse the shorter tree
- This is called the "weighted algorithm"

'''
# TO DO: skipped this, have not actually completed
# class QuickFind(object):

#   def __init__(self, array_size):
#     self.array = range(0, array_size)

#   def connected(self, x, y):
#     return self.find_root(x) == self.find_root(y)

#   def find_root(self, index):
#     while self.array[index] != index:
#       index = self.array[index]
#     return index

#   # we want to attach the first number to the component of the second number
#   def union(self, x, y):
#     root_y = self.find_root(y)
#     self.array[x] = root_y


# some test cases
# qf = QuickFind(8)
# qf.union(1, 2)
# qf.union(2, 6)
# print qf.connected(1, 6)