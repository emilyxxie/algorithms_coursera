'''
Connectivity queries:

  Goal is to determineefinition -> vertices are connected if there is a path between them.

  Goal: pre-process graph to answer queries in the form of is v connected to w?
  In constant-time.

  We'll use a DFS approach to implement.

  The algorithm is based on teh notion that connection is an equivalence relation.
  Every node is connected to itself.
  If v is connected to w, then w is connected to v.

  If v is connected to w and w is connected to x, then v is connected to x

  This computation should be able  to be done in linear time.

'''

from graph import Graph, Vertex

class ConnectedComponents(object):

  def __init__(self, graph):
    self.graph = graph
    self.visited = {}

  def find_connected_components(self):
    cc = 0
    for vertex in self.graph.vertices:
      if vertex not in self.visited:
        cc += 1
        self.__dfs(vertex, cc)

  def __dfs(self, key, cc):
    self.visited[key] = cc
    vertex = self.graph.get_vertex(key)
    for connection in vertex.get_connections():
      if connection not in self.visited:
        self.__dfs(connection, cc)

  def is_connected(self, key1, key2):
    return self.visited[key1] == self.visited[key2]

  def get_components(self, key):
    cc_val = self.visited[key]
    return [x for x, y in self.visited.items() if y == cc_val]


graph = Graph()

for i in range(1, 17):
  graph.add_vertex(i, str(i) * 3)

graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(1, 3)
graph.add_edge(2, 7)
graph.add_edge(4, 5)
graph.add_edge(3, 10)
graph.add_edge(7, 8)
graph.add_edge(7, 6)
graph.add_edge(6, 9)
graph.add_edge(4, 7)
graph.add_edge(11, 13)
graph.add_edge(11, 14)
graph.add_edge(15, 16)
graph.display()

cc = ConnectedComponents(graph)
cc.find_connected_components()
cc.get_components(2)
cc.is_connected(2, 11)






