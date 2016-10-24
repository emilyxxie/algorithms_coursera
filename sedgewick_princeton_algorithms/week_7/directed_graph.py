'''

In a digraph, aka directed graph, an edge has a direction.
Vertices in digraphs have in-degrees and out-degrees.
Outdegrees -> number of arrows coming out out the digraph.
Indegree is vice versa.

Examples of digraphs -> an electrical circuit

For digraphs, DFS and BFS are exactly the same as in undirected graphs. BFS still
computes shortest graph in linear time.

Examples: Website crawler is a directed graph using BFS.
(We don't use DFS to crawl - imagine a website like amazon.com...
it will have many links to itself. We should thus take way too long
to get to another domain. More practically speaking, we could accidentally
DDOS a website doing this.)

'''


class DirectedGraph(object):
  def __init__(self):
    self.numVertices = 0
    self.vertices = {}

  # adds directed edge, going from v1 -> v2
  def add_edge(self, v1, v2):
    vertex = self.get_vertex(v1)
    vertex_2 = self.get_vertex(v2)
    vertex.add_connection(v2, vertex_2.val)

  # remove edge. v1 = origin vertex
  # v2 = vertex that v1 points to
  def remove_edge(self, v1, v2):
    vertex = self.vertices[v1]
    vertex.remove_connection(v2)

  def add_vertex(self, key, val):
    self.vertices[key] = Vertex(val)

  def remove_vertex(self, key):
    del self.vertices[key]
    for k, vertex in self.vertices.items():
      if key in vertex.get_connections():
        vertex.remove_connection(key)

  def get_vertex(self, key):
    return self.vertices[key]

  def display(self):
    for key, vertex in self.vertices.items():
      print("%i => %s") % (key, vertex.get_connections())

  def reverse(self):
    pass

class Vertex(object):

  def __init__(self, val):
    self.val = val
    self.connections = {}

  def get_connections(self):
    return self.connections.keys()

  def add_connection(self, key, val):
    self.connections[key] = val
    return self.connections

  def remove_connection(self, key):
    del self.connections[key]


# z



