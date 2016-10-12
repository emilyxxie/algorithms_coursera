'''

As an alternative way to implement collision detection.

'''



class SeparateChainingHashTable(object):

  class Node(object):
    def __init__(self, val):
      self.val = val
      self.next = None

  def __init__(self, table_size):
    self.table_size = table_size
    self.hash_table = [None] * table_size

  #---------------------------------
  # public api
  #---------------------------------

  # inserts items into table
  def put(self, val):
    pos = self.__hash(val)
    if self.hash_table[pos] != None:
      self.__chain(val, pos)
    else:
      self.hash_table[pos] = self.Node(val)
    return pos

  # finds slot for a given value
  def search(self, val):
    key = self.__hash(val)
    node = self.hash_table[key]
    if node.val != val and node != None:
      while node and node.val != val:
        node = node.next
    return key if node and node.val == val \
           else "Value not in table"

  # returns node using key
  def get(self, key):
    return self.hash_table[key]

  # print out table
  def show_table(self):
    for node in self.hash_table:
      if node:
        print(node.val),
        while node.next:
          node = node.next
          print("->"),
          print(node.val)
      else:
        print(None)
      print("\n")


  #---------------------------------
  # private helpers
  #---------------------------------

  def __hash(self, val, attempts = 0):
    return val % self.table_size

  def __chain(self, val, pos):
    node = self.hash_table[pos]
    while node.next:
      node = node.next
    node.next = self.Node(val)

ht = SeparateChainingHashTable(11)

for num in range(11, 22):
  if num != 13:
    ht.put(num)

ht.put(35)
ht.put(36)
print(ht.search(21))


ht.show_table()