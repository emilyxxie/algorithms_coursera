'''

DFS should allow keep track of visited vertices,
which should be decoupled from the actual vertices themselves. This calls
for creating a separate class.

DFS runs in O(N) time

Applications of DFS:
Find a path between two vertices. Find all vertices connected to a
given source index.

Using this DFS, one can find vertices connected to s in constant time, and can
find a path to s (if one exists) in time proportional to its length.

DFS is not the optimal graph-searching method for all applications.

'''

from graph import Graph, Vertex

class DFS(object):
  def __init__(self, graph):
    # keeps track of which nodes visited, and from where
    self.visited = {}
    self.graph = graph

  def dfs(self, key, prev = None):
    self.visited[key] = prev
    vertex = self.graph.get_vertex(key)
    print(vertex.val)
    for k in vertex.get_connections():
      if k in self.visited:
        continue
      else:
        self.dfs(k, key)

  def get_path(self, target):
    if target in self.visited:
      # follow the path backwards until we reach a None node
      next = target
      while next:
        print(next)
        next = self.visited[next]
    else:
      return


graph = Graph()

for i in range(0, 11):
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
graph.display()

dfs = DFS(graph)
dfs.dfs(1)
dfs.get_path(8)