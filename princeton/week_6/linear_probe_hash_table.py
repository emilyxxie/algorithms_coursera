'''

Unlike the BST data structure, hash tables allow for constant time operations

Here is a hash table implemented using linear probing as its collision resolution method.

Linear probing really just means going to the next available slot. One downfall of this,
however, is the tendency to cluster, resulting in chains of adjacent data.
Clustering is pretty bad since as the table increases in size, so too do the clusters.
In turn, new values likely hash into a big cluster, resulting in increasingly longer probes.
This of course affects performance time for search and insert over the long run.

To help with this, we can increment the amount that a linear probe moves per rehash.

'''


class LinearProbeHashTable(object):
  probe_step = 3
  error_map = {
    0: "Hash table table full",
    1: "Item does not exist in table",
  }

  def __init__(self, table_size):
    self.table_size = table_size
    self.hash_table = [None] * table_size

  #---------------------------------
  # public api
  #---------------------------------

  # inserts items into table
  def put(self, val):
    pos = self.__hash(val)
    # use linear probing if necessary
    if self.hash_table[pos] != None:
      pos = self.__rehash(pos)
    self.hash_table[pos] = val
    return pos

  # finds key for a given value
  def search(self, val):
    original = self.__hash(val)
    pos = original
    start = pos
    attempts = 0
    while self.hash_table[pos] != val and self.hash_table[pos] != None:
      attempts += 1
      pos = self.__hash(pos, attempts)
      if start == pos:
        pos = None
        break
    return pos if self.hash_table[pos] == val else self.error_map[1]

  # returns item using key
  def get(self, key):
    return self.hash_table[key]

  # print out table
  def show_table(self):
    print(self.hash_table)


  #---------------------------------
  # private helpers
  #---------------------------------

  def __hash(self, val, attempts = 0):
    return (val + (self.probe_step * attempts)) % self.table_size

  def __rehash(self, start):
    attempts = 0
    pos = start
    while self.hash_table[pos] != None:
      attempts += 1
      pos = self.__hash(pos, attempts)
      if pos == start:
        raise StandardError(self.error_map[0])
    return pos


ht = LinearProbeHashTable(11)

for num in range(11, 22):
  if num != 13:
    ht.put(num)

ht.put(32)
print(ht.search(32))
ht.show_table()
