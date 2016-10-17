'''

A couple of simple graph challenges below, as proposed by Professor Sedgewick.

'''


from graph import Graph, Vertex
import sys

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
graph.add_edge(1, 2)
graph.display()


'''

Determine whether or not a graph is a bipartite.

'''

# TODO


'''

Detect whether or not a simple graph contains a cycle.

'''

def does_graph_cycle(graph):
  visited = {}

  def dfs(v_key, prev):
    vertex = graph.get_vertex(v_key)
    if v_key not in visited:
      visited[v_key] = prev
      for connection in vertex.get_connections():
        if connection in visited and connection != prev:
          return sys.exit("Cycle Found")
        else:
          dfs(connection, v_key)

  for v_key in graph.vertices:
    dfs(v_key, None)
  return "No cycle"

does_graph_cycle(graph)


'''

Seven bridges of Konisberg:

Is there a cycle that uses every edge exactly once?
Algorithm uses theory as discovered by Euler: if
all vertices have an even degree and is connected, then it is possible.

'''

# TODO


'''

Other algorithms to note:

1)  Find a cycle that vists every vertex exactly once: "Traveling salesperson"
    This algorithm can be done, but it is intractable and is considered NP-Complete.
    "Hamiltonian cycle" problem.
    NP-Complete problems will be considered later on.

2)  Possible to lay out a graph on a plane without crossing edges?
    Linear time algorithm based on DFS was discovered by B. Tarjan in 1970s.
    This is a really complex algorithm, and would never be expected of a student.

'''




