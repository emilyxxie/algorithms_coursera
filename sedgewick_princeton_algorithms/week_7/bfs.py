'''

BFS searches via breadth first, using a queue as an auxillary data structure.
This is in comparison to DFS, which lends itself to recursion.

BFS happens to give us the shortest path, as by using a queue, we are
processing items in first-in-first out order. The first time we get to the vertex
is always the shortest path to the vertex.

'''

from graph import Graph, Vertex

class BFS(object):

  def __init__(self, graph):
    self.graph = graph
    self.visited = {}

  def bfs(self, key):
    queue = [key]
    self.visited[key] = None
    while queue:
      key = queue.pop(0)
      print(key)
      vertex = self.graph.get_vertex(key)
      for connection in vertex.get_connections():
        if connection not in self.visited:
          queue.append(connection)
          self.visited[connection] = key

  def shortest_path(self, target):
    if target in self.visited:
      # follow the path backwards until we reach a None node
      next = target
      while next:
        print(next)
        next = self.visited[next]
    else:
      return

