import sys
'''

Sweep-line algorithm.

Given a random set of horizontal and vertical lines
occuring on a x-y coordinate grid, calculate the number of intersections

You can easily do this using O(n**2), but the sweep-line algorithm completes it in O(NLogN) + R.

When you hit the left coordinate of a line, insert the Y coordinate into a binary search tree.
Keep track of y-coordinates in a binary search tree.
Keep track of where the coordinate ends. Once it ends, remove the start from your BST
Because it means it has already been processed.

Once you hit a vertical line segment, you need to do a range search of the Y-interval end-points.
Any point that is within that range will intersect.

Using a binary search tree to implement a symbol table
BFS tends to take log N time. However, worst case scenario takes linear time.

TODO: maybe implement this visually in p5.js (!!! so fun)

'''

class BinarySearchTree(object):

  #---------------------------------

  class Node(object):

    def __init__(self, key, val):
      self.key   = key
      self.val   = val
      self.left  = None
      self.right = None

  #---------------------------------

  def __init__(self, key = None, val = None):
    self.root = self.Node(key, val)

  #---------------------------------
  # public api
  #---------------------------------

  def insert(self, key, val):
    if not self.root.key:
      self.root = self.Node(key, val)
      return self.root
    else:
      self.root = self.__insert(key, val, self.root)

  def delete(self, key):
    node = self.root
    self.root = self.__hibbard_delete(key, self.root)

  def select(self, val):
    node = self.head
    while node:
      if val < node.val:
        node = node.left
      elif val > node.val:
        node = node.right
      else:
        return node

  def display(self, node):
    if node == None:
      return
    print(node.key)
    if node.left:
      print("%d Left: " % (node.key)),
      self.display(node.left)
    if node.right:
      print("%d Right: " % (node.key)),
      self.display(node.right)

  def find_max(self, node):
    while node.right:
      node = node.right
    return node

  def find_min(self, node):
    while node.left:
      node = node.left
    return node

  def bfs(self):
    queue = [self.root]
    while queue:
      node = queue.pop(0)
      print(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  def dfs(self, node):
    print(node.val)
    if node.left:
      self.dfs(node.left)
    if node.right:
      self.dfs(node.right)

  #---------------------------------
  # private helpers
  #---------------------------------

  def __insert(self, key, val, node):
    if node == None: return self.Node(key, val)
    if key < node.key:
      node.left = self.__insert(key, val, node.left)
    elif key > node.key:
      node.right = self.__insert(key, val, node.right)
    else: # key == node.key
      node.val = val
    return node

  def __hibbard_delete(self, key, node):
    # if the delete reaches a node with a value of None, it means the node was never found
    # we return None nevertheless since we are recursing
    # and want to keep this child as is for the parent who will receive this on return
    if node == None:
      return None
    if key < node.key:
      node.left = self.__hibbard_delete(key, node.left)
    elif key > node.key:
      node.right = self.__hibbard_delete(key, node.right)
    else: # key == node.key
      if not node.left and not node.right:
        return None
      if node.left == None: return node.right
      if node.right == None: return node.left
      # by now, if the node has passed the above checks
      # it will have both a left and right child.
      # if so, replace the node with the minumum
      # of the right child, a.k.a the next largest
      next_largest = self.__hibbard_delete_min(node.right)
      left = node.left
      if next_largest == node.right:
        right = next_largest.right
      else:
        right = node.right
      node = next_largest
      node.left = left
      node.right = right
    return node

  def __hibbard_delete_min(self, node):
    while node.left:
      parent = node
      node = node.left
    if 'parent' in locals():
      parent.left = node.right
    return node

# horizontal_lines = [
#   [(1,1), (3,1)],
#   [(2,3), (6,3)],
#   [(4,5), (8,5)],
#   [(8,10), (10,10)],
# ]

# vertical_lines = [
#   [(7,2), (7,6)],
#   [(5,2), (5,6)],
# ]

lines = [
  [(1,1), (3,1)],
  [(2,3), (6,3)],
  [(4,5), (8,5)],
  [(8,10), (10,10)],
]

# INCOMPLETE: TODO -> I SHOULD FIND FORMAT OF THE INPUT

# given a de-duped set of lines, where every x and y coordinate are distinct
# def find_intersections(horizontal, vertical):
#   bst = BinarySearchTree()
#   horizontal = [coordinate for line in horizontal for coordinate in line]
#   horizontal.sort(key = lambda x: x[0])
#   print(horizontal)
#   # line.sort(key = lambda x: x[0])

#   for i, point in enumerate(horizontal):
#     x = point[0]
#     v = vertical[0][0]
#     # todo -> edge case of when it hits the end
#     if len(vertical > 0) and# we reach the end, and there's still something in vertical, immediately comapre

#     v >= x and v <= horizontal[i - 1][0]:
#       bst.range(vertical[0][1], vertical[1][1])
#     # if the item is already in the BST, then delete it if the y is the same
#     if bst.select(y):
#       bst.delete(y)
#     else:
#       bst.insert(y)
#     prevX = x

#find_intersections(horizontal_lines, vertical_lines)



