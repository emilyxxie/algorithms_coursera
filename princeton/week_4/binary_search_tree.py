'''

Using a binary search tree to implement a symbol table

'''

class Binary_Search_Tree(object):

  def __init__(self, val = None):
    self.root = Node(val)

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

  '''
  non-recursive insertion:
  '''
  # def __insert(self, val):
  #   current_node = self.root
  #   while current_node:
  #     if val < current_node.val:
  #       if current_node.left:
  #         current_node = current_node.left
  #       else:
  #         current_node.left = Node(val)
  #         return
  #     else:
  #       if current_node.right:
  #         current_node = current_node.right
  #       else:
  #         current_node.right = Node(val)
  #         return

  def get_value(self):
    pass

  def delete(self):
    pass

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
bst.print_nodes()








