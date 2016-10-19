'''

A couple of simple graph challenges below, as proposed by Professor Sedgewick.

'''


from graph import Graph, Vertex
import sys

graph = Graph()

# for i in range(1, 17):
#   graph.add_vertex(i, str(i) * 3)

# graph.add_edge(1, 2)
# graph.add_edge(1, 4)
# graph.add_edge(1, 3)
# graph.add_edge(2, 7)
# graph.add_edge(4, 5)
# graph.add_edge(3, 10)
# graph.add_edge(7, 8)
# graph.add_edge(7, 6)
# graph.add_edge(6, 9)
# graph.add_edge(4, 7)
# graph.add_edge(11, 13)
# graph.add_edge(11, 14)
# graph.add_edge(15, 16)
# graph.add_edge(1, 2)
# graph.display()


'''

Determine whether or not a graph is a bipartite.

'''




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

# does_graph_cycle(graph)


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

for i in range(1, 5):
  graph.add_vertex(i, str(i) * 3)


# has path
# graph.add_edge(1, 2)
# graph.add_edge(1, 4)
# graph.add_edge(1, 3)
# graph.add_edge(3, 2)
# graph.add_edge(3, 4)

# has path with no odds
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(4,1)

# graph.display()

def find_euler_tour(graph):
  validation = validate_euler_tour(graph)

  if not validation:
    return False

  start = validation[0]
  end   = validation[1]

  edges_visited = {}

  def dfs(key, prev):
    # first case, don't add anything into array
    # I don't like this.
    if not prev:
      edges_visited[key] = []
    elif edges_visited.has_key(key):
      edges_visited[key].append(prev)
    else:
      edges_visited[key] = [prev]

    vertex = graph.vertices[key]
    connections = vertex.get_connections()
    for c in connections:
      # don't do this check if we're on the final item
      # edges may not always have been visited
      c_connections = graph.vertices[c].get_connections()
      print(c_connections)
      print(edges_visited)
      if c in edges_visited and len(c_connections) - len(edges_visited[c]) > 2:
        dfs(c, key)

  # after the DFS, if there are any unvisited nodes left,
  # this means that there are unvisited vertices
  # this means not all nodes are connectedd
  # this means that this is not a euler tour
  # I want to roll this check into validate_euler_tour() function
  dfs(start, None)
  if len(edges_visited) != len(graph.vertices):
    return


# validates if a graph is a euler tour or not
# if yes, return the start and end nodes
# in the case where there are no odds
# the start and end nodes will be any node
# as long as it is itself
# so, simply choose the graph vertex
def validate_euler_tour(graph):
  odd = []
  for key in graph.vertices:
    vertex = graph.get_vertex(key)
    connections = vertex.get_connections()
    if len(connections) % 2 != 0:
      odd.append(vertex)
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



# TODO:
# learn backtracking
# learn dynamic programming

