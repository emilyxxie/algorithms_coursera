'''

Graphs comprise of vertices and edges. Vertices represent the values, whereas the
and edges symbolize the connections between nodes.

Below is a simple implementation of a graph as represented by adjaceny lists.
In this structure, each node contains a list of all elements that are connected to it.

Other ways to represent graphs in Sedgewick's discussion include the adjacency matrix.
Imagine a grid of vertices * vertices. At each point in the grid, we determine if two vertices
are connected using a boolean value. But this of course is not scalable nor widely used given that
it grows at N**2 rate. e.g. A graph with 1 million vertices would need space of 1 million ** 2.


'''

class Graph(object):
  def __init__(self):
    self.numVertices = 0
    self.vertices = {}

  def add_edge(self, v1_key, v2_key):
    v1 = self.vertices[v1_key]
    v2 = self.vertices[v2_key]
    v1.add_connection(v2_key, v2)
    v2.add_connection(v1_key, v1)

  def add_vertex(self, key, val):
    self.vertices[key] = Vertex(val)

  def remove_vertex(self, key):
    del self.vertices[key]
    for k, vertex in self.vertices.items():
      if key in vertex.get_connections():
        vertex.remove_connection(key)

  def remove_edge(self, v1_key, v2_key):
    v1 = self.vertices[v1_key]
    v2 = self.vertices[v2_key]
    v1.remove_connection(v2_key)
    v2.remove_connection(v1_key)

  def get_vertex(self, key):
    return self.vertices[key]

  def display(self):
    for key, vertex in self.vertices.items():
      print("%i => %s") % (key, vertex.get_connections())


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


graph = Graph()
graph.add_vertex(1, 10)
graph.add_vertex(2, 20)
graph.add_vertex(3, 30)
graph.add_edge(1, 2)
graph.add_edge(3, 1)
graph.remove_vertex(3)
graph.display()



