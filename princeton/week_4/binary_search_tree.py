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
    else:
      if node.right:
        self.__insert(val, node.right)
      else:
        node.right = Node(val)

  def find_max(self):
    node = self.root
    while node.right != None:
      node = node.right
    return node.val

  def find_min(self):
    node = self.root
    while node.left != None:
      node = node.left
    return node.val

  def find_floor():
    pass

  def find_ceiling():
    pass

  def get_value(self):
    pass

  def delete(self, val):
    node = self.root
    while node.val:
      if val < node.val:
        node = node.left
      elif val > node:
        node = node.right
      elif node.val == val:
        if node.left:
          node.val = node.left
        elif node.right:
          node.val = node.right
        # else:
          # node.val =

  def print_nodes(self):
    node = self.root
    self.__print_nodes(node)

  def __print_nodes(self, node):
    print(node.val)
    if node.left:
      print("%d Left: " % (node.val)),
      self.__print_nodes(node.left)
    if node.right:
      print("%d Right: " % (node.val)),
      self.__print_nodes(node.right)


class Node(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


bst = Binary_Search_Tree()
bst.insert(5)
bst.insert(6)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.delete(2)
bst.print_nodes()
print(bst.find_min())
print(bst.find_max())


