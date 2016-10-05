'''

Red black tree is a type of binary search tree that is self-balancing.
This implementation will be the "Left-Leaning Red-Black Tree, which is
essentially the same as a 2-3 Tree, with 2-node representations illustrated w/ red edge.
So, if a node has a red connection, in the 2-3 Tree, it corresponds to the left side of the parent in a two-node.

LLRBT shares much of the same functionality as BST, but benefits from the fact that
it keeps itself relatively balanced. (Hibbard Deletion in BSTs over time result in a
fairly unbalanced tree, resulting in average case O(sqrtN) for operations.

Rules:
1) If a right child has a red link, and a left child has a black link: rotate left
2) If left child, or left-left grandchild red: rotate right
3) Both children red: flip colors

'''

class RedBlackTree(object):

  RED = True
  BLACK = False

  #---------------------------------

  class Node(object):

    def __init__(self, key, val):
      self.key   = key
      self.val   = val
      self.left  = None
      self.right = None
      self.color = RedBlackTree.RED

  #---------------------------------

  def __init__(self, key = None, val = None):
    self.root = self.Node(key, val)
    self.root.color = self.BLACK

  #---------------------------------
  # public api
  #---------------------------------

  def insert(self, key, val):
    if not self.root.val:
      self.root = self.Node(key, val)
      return self.root
    else:
      return self.__insert(key, val, self.root)

  def display(self, node):
    if node == None:
      return
    print(node.key, node.color)
    if node.left:
      print("%d Left: " % (node.key)),
      self.display(node.left)
    if node.right:
      print("%d Right: " % (node.key)),
      self.display(node.right)

  def get(self, node):
    pass

  def find(self, node):
    pass

  #---------------------------------
  # private helpers
  #---------------------------------

  def __insert(self, key, val, node = None):
    if node == None: return self.Node(key, val)
    if key < node.key:
      node.left  = self.__insert(key, val, node.left)
    elif key > node.key:
      node.right = self.__insert(key, val, node.right)
    else:
      # same key, different value. So, overwrite
      node.val = val
    if key == 6:
      print(node.val)
    # return self.__balance(node)
    return node

  def __balance(self, node):
    # if self.__is_red(node.right) and not self.__is_red(node.left):
    #   node = self.__rotate_left(node)
    # if self.__is_red(node.left) and node.right and self.__is_red(node.right.right):
    #   node = rotate_right(node)
    # if self.__is_red(node.left) and self.__is_red(node.right):
    #   # self.__flip_color(node)
    #   pass
    return node

  def __is_red(self, node):
    # to do, need to check what would happen if I return nothing instead of color
    if node:
      return node.color

  def __rotate_left(self, node):
    pass

  def __rotate_right(self, node):
    pass

  def __flip_color(self, node):
    self.color = BLACK
    self.left.color = RED
    self.right.color = RED


rbt = RedBlackTree()
rbt.insert(3, "three")
rbt.insert(1, "one")
rbt.insert(4, "four")
rbt.insert(5, "five")
rbt.insert(2, "two")
rbt.insert(6, "six")
# rbt.root.right.right.val
# rbt.root.right.val

rbt.display(rbt.root)


