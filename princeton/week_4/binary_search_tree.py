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

  def delete(self, val):
    node = self.root
    self.__delete(val, node)

  def __delete(self, val, node):
    if val < node.val:
      if node.left:
        self.__delete(val, node.left)
      return
    elif val > node.val:
      if node.right:
        self.__delete(val, node.right)
      return
    else:
        self.__handle_successors(node)

  def __handle_successors(self, node):
      children = self.count_children(node)
      if children == 0:
        node = None
      elif children == 1:
        if node.left:
          node = node.left
        else:
          node = node.right
      elif children == 2:
        pass
        # TODO: complete deletion if there's two children

  def count_children(self, node):
    total = 0
    if node.left:
      total += 1
    if node.right:
      total += 1
    return total


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


