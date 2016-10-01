'''

Using a binary search tree to implement a symbol table

'''

class Binary_Search_Tree(object):

  def __init__(self, val = None):
    self.root = Node(val)
    self.height = 1 if self.root else 0

  def insert(self, val):
    if self.root.val == None:
      self.root.val = val
    else:
      self.__insert(val, self.root)

  def __insert(self, val, node):
    if val < node.val:
      if node.left:
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

  def delete(self, val):
    node = self.root
    self.__delete(val, node)

  def __delete(self, val, node):
    if val < node.val:
      if node.left:
        self.__delete(val, node.left)
      else:
        node = node.left
    elif val > node.val:
      if node.right:
        self.__delete(val, node.right)
      else:
        node = node.right
    else:
        self.__handle_successors(node)

  def __handle_successors(self, node):
    if node.left or node.right:
      if node.left:
        node.left.parent = node.parent
        node = node.left
      else:
        node.right.parent = node.parent
        node = node.right
    elif node.left and node.right:
      left_c  = node.left
      right_c = node.right
      successor = self.find_max(node.left)
      node.left.parent = successor.parent
      node = successor
      node.left = left_c
      node.right = right_c
    else:
      node = None

  def print_nodes(self, node):
    if node == None:
      return
    print(node.val)
    if node.left:
      print("%d Left: " % (node.val)),
      self.print_nodes(node.left)
    if node.right:
      print("%d Right: " % (node.val)),
      self.print_nodes(node.right)

  def find_max(self, node):
    while node.right != None:
      node = node.right
    return node

  def find_min(self, node):
    while node.left != None:
      node = node.left
    return node

  # def find_floor(self, val):
  #   node = self.head
  #   while node != None:
  #     if val < node.left.val:
  #       node = node.left
  #     elif val > node.right.val:
  #       node = node.right
  #     elif: val > node:

  def get_value(self):
    pass

  def get

class Node(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None

bst = Binary_Search_Tree()

bst.insert(6)
bst.insert(5)
bst.insert(7)
bst.insert(2)
bst.insert(4)
# bst.delete(2)
bst.print_nodes(bst.root)
# bst.find_floor()
# print(bst.find_min())
# print(bst.find_max())


