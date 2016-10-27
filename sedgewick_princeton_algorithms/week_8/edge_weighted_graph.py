import string
import sys

class EdgeWeightedGraph(object):

  def __init__(self):
    '''
    An edge weighted graph maintains a node-indexed dictionary
    of adjacency lists of corresponding edges (each stored as a ref to the object).
    Since this is an undirected graph, each edge is listed twice.
    '''
    self.nodes = {}
    self.total_edges = 0

  def add_edge(self, edge):
    v = edge.either()
    w = edge.other(v)
    self.nodes[v].connect(edge)
    self.nodes[w].connect(edge)
    self.total_edges += 1

  def add_node(self, key, data):
    self.nodes[key] = Node(data)

  def count_nodes(self):
    return len(self.nodes.keys())

  def display(self):
    for n in self.nodes:
      node = self.nodes[n]
      if node.edges:
        sys.stdout.write(
          "%d: %s ==>  " % (n, node.data)
        )
      else:
        print("%d: %s" % (n, node.data))
      if node.edges:
        print(" , ".join(str(vars(edge)) for edge in node.edges))


######################################

class Node(object):

  def __init__(self, data):
    self.data = data
    self.edges = []

  def connect(self, edge):
    self.edges.append(edge)

######################################

class Edge(object):

  def __init__(self, v, w, weight):
    self.v = v
    self.w = w
    self.weight = weight

  def either(self):
    '''
    Picks one of either node endpoints connected to edge.
    When processing an edge, it's fairly idiomatic to first
    pick out "either," and then pick out the "other."
    '''
    return self.v

  def other(self, node):
    '''
    Picks the other endpoint.
    '''
    return self.w if node == self.v else self.v

  def compare(edge2):
    '''
    Compares the weight of this edge to that of another.
    '''
    if self.weight < edge2.weight:
      return -1
    elif self.weight > edge2.weight:
      return 1
    else:
      return 0


ewg = EdgeWeightedGraph()
alpha = string.ascii_lowercase[:11]

for i, char in enumerate(alpha):
  ewg.add_node(i, char)

ewg.add_edge(Edge(1, 2, 1.25))
ewg.add_edge(Edge(1,4, 3))
ewg.display()



