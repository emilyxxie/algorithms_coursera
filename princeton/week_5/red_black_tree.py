'''

Red black tree is a type of binary search tree that is self-balancing.
This implementation will be the "Left-Leaning Red-Black Tree, which is
essentially the same as a 2-3 Tree, with 2-node representations illustrated w/ red edge.
So, if a node has a red connection, in the 2-3 Tree, it would be the left side of the parent in a two-node.

LLRBT shares much of the same functionality as BST, but benefits from the fact that
it keeps itself relatively balanced. (Hibbard Deletion in BSTs over time result in a
fairly unbalanced tree, resulting in average case O(sqrtN) for operations.


'''

class RedBlackTree(object):

  RED = True
  BLACK = False

  def __init__(self, val = None):
    self.root = Node(val)

    # process:
    # insert according to BST rules
    # all nodes inserted must be red, except root
    # am I the right child?
        # if I'm the only child or is my sibling black, rotate left through parent
        # if I have a red sibling, turn yourself and your sibling into black
          # Then, your parent needs to turn red.
    # two left red children in a row:
      # rotate self right
    # continually apply the rules until you're in a valid state


  def __is_red(self, node):
    return node.color



  def rotate_left(self, node):
    pass


  def rotate_right(self, node):
    pass

  def flip_colors(self, node):
    pass


class Node(object):

  def __init__(self, val):
    self.key = key
    self.val = val
    self.left = None
    self.right = None
    self.color = BLACK




