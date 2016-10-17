'''

Connectivity queries: Exercise to determine of vertices are connected as a component.
Vertices are considered part of the same component if there is a path between them.
Pre-process graph using DFS; any connectivity queries from there on out will be executed in
constant time.

Algorithm is based on the notion that connection is an equivalence relation; if
v is connected to w, then w is connected to v. If v is connected to w, which is connected to x,
then v is connected to x.

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






