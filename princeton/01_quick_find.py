'''

'''

class QuickFind(object):

  def __init__(self, total_items):
    self.comp_array = range(0, total_items)

  def connected(self, x, y):
    return self.comp_array[x] == self.comp_array[y]

  def union(x, y):

    original = self.comp_array[x]
    union = self.comp_array[y]

    for i in self.comp_array:
      if self.comp_array[i] == original:
        self.comp_array[i] = union


# comp_array = [0, 1, 1, 8, 8, 0, 0, 1, 8]

qf = QuickFind(8)
print qf.connected(1, 2)