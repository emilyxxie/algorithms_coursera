# introduction to stacks:

# client reads strings from standard input
# if string is equal to a character, push on to stack
# if we see a hyphen, take the first item in the stack, and pop it, and print it

def string_stack(string):
  stack = []
  popped_strings = []

  for word in string.split():
    if word == "-":
      popped = stack.pop()
      popped_strings.append(popped)
    else:
      stack.append(word)

  return " ".join(popped_strings)


# test case
test_string = "To be or not to - be - - that - - - is"

# should result in: to be or not that or be
print string_stack(test_string)

##### Below is a linked-list implementation of the same thing ######


'''
- Linked list is a string of nodes
- The node contains data on itself and a reference to the next node on the list (singly linked)
- The main advantage of using linked list as opposed to an array, is the linked list's dyanimic memory allocation. If you don't know the amount of data you want to store before hand, linked list can adjust
- Pro comes with con: dynamic memory allocation requires more space + slower look up times

'''

class Node(object):

  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_next(self, next):
    self.next = next


class LinkedList(object):

  def __init__(self, head = None):
    self.head = head

  def get_head(self):
    return self.head.get_data()

  # not used here in the context of this lesson, but wanted to implement regardless
  def count_list(self):
    current = self.head
    size = 0
    while (current.get_data != None):
      size += 1
      current = self.head.get_next()
    return size

  def add_node(self, data):
    self.head = Node(data, self.head)

  def is_empty(self):
    return self.head == None

  def pop(self):
    popped = self.head
    if popped == None:
      return "There are no items in the stack"
    self.head = self.head.get_next()
    return popped.get_data()

  def push(self, node_data):
    next = self.head
    self.head = Node(node_data, next)


def string_stack_ll(string):
  string = string.split()
  string_stack = LinkedList()

  for word in string:
    if word == "-":
      print string_stack.pop(),
    else:
      string_stack.push(word)


test_string = "To be or not to - be - - that - - - is"

string_stack_ll(test_string)
