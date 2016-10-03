'''

Red black tree is a subset of binary tree
Rules:

1) Node is either red or black
2) Root is always black
3) All leaves are black, never have values, always contain None
4) If node is red, both of its children are black
5) Every path from a node to any of its descendant NIL nodes contains the same number of black nodes

^^ if you maintain these properties, you will be balanced


'''

import sys

class RedBlackTree(object):

  def __init__(self, val = None):
    self.root = Node(val)

  def insert(self, val):
    if self.root.val == None:
      self.root.val = val
    else:
      self.__insert(val, self.root)


  def search(self, val):
  node = self.head
  while node:
    if val < node.val:
      node = node.left
    elif val > node.val:
      node = node.right
    else:
      return node


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




    # insert according to BST rules
    # all nodes inserted must be red, except root
    # am I the right child?
        # if I'm the only child or is my sibling black, rotate left through parent
        # if I have a red sibling, turn yourself and your sibling into black
          # Then, your parent needs to turn red.
    # two left red children in a row:
      # rotate self right




    # continually apply the rules until you're in a valid state






  def delete(self, val, node):
    if val < node.val:
      if node.left:
        self.delete(val, node.left)
      else:
        return
    elif val > node.val:
      if node.right:
        self.delete(val, node.right)
      else:
        return
    else:
      self.__delete_and_handle_successors(node)

  def __delete_and_handle_successors(self, node):
    if node.left and node.right:
      # not worrying about balancing
      # so, just find max of left node and replace it
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
    while node.right:
      node = node.right
    return node

  def find_min(self, node):
    while node.left:
      node = node.left
    return node

  def get_value(self):
    pass

class Node(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    self.color = None
    # RBT root is always black

bst = BinarySearchTree()

bst.insert(6)
bst.insert(8)
bst.insert(7)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.delete(6, bst.root)
bst.print_nodes(bst.root)
# bst.find_floor()
# print(bst.find_min())
# print(bst.find_max())


