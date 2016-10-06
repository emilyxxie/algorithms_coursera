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
TODO: This is a pretty ugly BFS. I should redo this soon.

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
    else:
      self.__insert(key, val, self.root)

  def delete(self, node):
    # if val < node.val:
    #   if node.left:
    #     self.delete(val, node.left)
    #   else:
    #     return
    # elif val > node.val:
    #   if node.right:
    #     self.delete(val, node.right)
    #   else:
    #     return
    # else:
    #   self.__hibbard_delete(node)
    pass

  def search(self, val):
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
      node = self.root
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

  def __insert(self, val, node):
    if val < node.val:
        self.__insert(val, node.left)
      else:
        node.left = Node(val)
        node.left.parent = node
    else:
      if node.right:
        self.__insert(val, node.right)
      else:
        node.right = Node(val)
        node.right.parent = node

  def __hibbard_delete(self, node):
    if node.left and node.right:
      val = self.find_max(node.left).val
      node.val = val
    elif node.left or node.right:
      if node.left:
        node.parent.left = node.left
        node.left.parent = node.parent
        node = node.left
        if node == self.root:
          self.root = node
      else:
        node.parent.right = node.right
        node.right.parent = node.parent
        node = node.right
        if node == self.root:
          self.root = node
    else:
      if node.parent.left == node:
        node.parent.left = None
      elif node.parent.right == node:
        node.parent.right = None
      node = None

bst = BinarySearchTree()

bst.insert(6)
bst.insert(8)
bst.insert(7)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.display()

