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

# from IPython import embed

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
      self.root.color = self.BLACK
      return self.root
    else:
      # the insertion returns always bubble back to the top node
      # so we can simply set the last value returned equal to root
      self.root = self.__insert(key, val, self.root)

  def display(self, node):
    if node == None:
      return
    color = 'red' if node.color else 'black'
    print(node.key, color)
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

  def delete(self, node):
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
    else: # same key, different value. So, overwrite
      node.val = val
    return self.__balance(node)

  def __balance(self, node):
    # return node
    if not self.__is_red(node.left) and self.__is_red(node.right):
      node = self.__rotate_left(node)
    if self.__is_red(node.left) and node.left and self.__is_red(node.left.left):
      node = self.__rotate_right(node)
    if self.__is_red(node.left) and self.__is_red(node.right):
      self.__flip_color(node)
    return node

  def __is_red(self, node):
    if node: return node.color

  def __rotate_left(self, node):
    rotated = node.right
    node.right = rotated.left
    rotated.left = node
    rotated.color = node.color
    rotated.left.color = self.RED
    return rotated

  def __rotate_right(self, node):
    rotated = node.left
    node.left = rotated.left
    rotated.right = node
    rotated.color = node.color
    rotated.right.color = self.RED
    return rotated

  def __flip_color(self, node):
    node.color = not node.color
    if node.left:
      node.left.color = not node.left.color
    if node.right:
      node.right.color = not node.right.color


rbt = RedBlackTree()
rbt.insert(3, "three")
rbt.insert(2, "two")
rbt.insert(1, "one")
rbt.insert(5, "five")
rbt.insert(6, "six")
rbt.insert(7, "seven")
rbt.insert(8, "eight")
rbt.display(rbt.root)


