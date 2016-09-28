'''

Notes:

- In this structure, the list indexes represent the nodes
- List elements provide a number that keeps track of whether the nodes reside in the same component
- That is, all the nodes within a component will have the same element
- Quick-find using this structure is pretty fast, though at the expense of a slower union.
- Union requires that we change every element in the list to match the element of the newly added component
- Worst-case scenario: we'd have to change n-1, n being list size
  (that is, every other element is in the component except for the item we're adding


'''

class QuickFind(object):

  def __init__(self, total_items):
    self.comp_array = range(0, total_items)

  def connected(self, x, y):
    return self.comp_array[x] == self.comp_array[y]

  def union(self, x, y):

    original = self.comp_array[x]
    union = self.comp_array[y]

    for i in self.comp_array:
      if self.comp_array[i] == original:
        self.comp_array[i] = union



# some testing
qf = QuickFind(8)
print qf.connected(1, 2)
qf.union(1, 2)
qf.union(1, 3)
print qf.connected(2, 3)


