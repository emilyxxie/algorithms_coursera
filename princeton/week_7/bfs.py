'''

BFS searches via breadth first, using a queue as an auxillary data structure.
This is in comparison to DFS, which lends itself to recursion.

BFS happens to give us the shortest path, as by using queue, we are
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
      print(queue)
      key = queue.pop(0)
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
graph.add_edge(5, 6)
graph.add_edge(4, 7)

bfs = BFS(graph)
bfs.bfs(1)
bfs.shortest_path(7)
