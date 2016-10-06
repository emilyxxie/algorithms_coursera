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



1) implement size
2) no parents
3) Ceiling
4) floor
5) rank
6) height


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
      return self.root
    else:
      self.root = self.__insert(key, val, self.root)

  def delete(self, key):
    node = self.root
    # hibbard deletion recursion returns the deleted node itself
    # maybe do a check --- if it returns None, then don't set it to root.
    # if it returns a node via hibbard, then set it to root
    self.root = self.__hibbard_delete(key, self.root)

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
      # so, perform the hibbard delete, which is to replace the node
      # with the minumum of the right child -> the next largest
      next_largest = self.__delete_min(node.right)
      left = node.left
      node = next_largest
      node.left = left
    return node

  def __delete_min(self, node):
    while node.left:
      parent = node
      node = node.left
    if 'parent' in locals():
      parent.left = node.right
    return node

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

bst = BinarySearchTree()

bst.insert(5, "five")
bst.insert(8, "eight")
bst.insert(9, "nine")
bst.insert(6, "six")
bst.insert(7, "seven")
bst.insert(10, "ten")
bst.delete(8)
# bst.delete(8)
# bst.insert(3, "three")
# bst.insert(2, "two")
# bst.insert(4, "four")
# bst.insert(5, "five")

bst.display(bst.root)
# print(bst.delete(150))

