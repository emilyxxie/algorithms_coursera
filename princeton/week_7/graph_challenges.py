'''

A couple of simple graph challenges below, as proposed by Professor Sedgewick.

'''


from graph import Graph, Vertex
import sys


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

'''

Seven bridges of Konisberg:

Is there a cycle that uses every edge exactly once?
Algorithm uses theory as discovered by Euler. This was the first thereom
in graph theory.

All vertices must have an odd degree of either 0 or two, and all vertices
must be reachable / connected.

Algorithm -> Always leave one edge to go to a starting vertex, or to the other odd vertex.
unless there is another edge
available to leave that vertex

Do not use an edge to go to a vertex unless anpther edge is available.

'''


def find_euler_tour(graph):
  validation = validate_euler_tour(graph)

  if not validation:
    return False

  start = validation[0]
  end   = validation[1]
  tour  = []

  edges_visited = {
    key: [] for key in graph.vertices.keys()
  }

  def dfs(key, prev):
    tour.append(key)
    if prev:
      edges_visited[prev].append(key)
      edges_visited[key].append(prev)

    vertex = graph.vertices[key]
    connections = vertex.get_connections()
    for c in connections:
      c_connections = graph.vertices[c].get_connections()
      if len(c_connections) - len(edges_visited[c]) >= 1 and key not in edges_visited[c]:
        dfs(c, key)

  dfs(start, None)

  # Final validation check:
  # If after the DFS, items remained untraveled, this means there are unconnected vertices
  edges_visited = dict((key, val) for key, val in edges_visited.iteritems() if val)
  if len(edges_visited) != len(graph.vertices): return False
  return tour


# Validates if a graph is a euler tour or not
# by ensuring there are only 0 or 2 odd vertices.
# If valid, return the start and end vertices.
# If no odds, the start and end vertices will be the same vertex
def validate_euler_tour(graph):
  odd = []
  for key in graph.vertices:
    vertex = graph.get_vertex(key)
    connections = vertex.get_connections()
    if len(connections) % 2 != 0:
      odd.append(key)
      if len(odd) > 2:
        return False
  if len(odd) == 1: return False
  start_end = []
  start_end.append(graph.vertices.keys()[0] if not odd else odd[0])
  start_end.append(graph.vertices.keys()[0] if not odd else odd[1])
  return start_end


print(find_euler_tour(graph))


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





