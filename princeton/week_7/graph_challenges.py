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

for i in range(1, 7):
  graph.add_vertex(i, str(i) * 3)

# has path, complicated:
# graph.add_edge(1, 2)
# graph.add_edge(2, 3)
# graph.add_edge(2, 4)
# graph.add_edge(3, 5)
# graph.add_edge(4, 5)
# graph.add_edge(5, 2)
# graph.add_edge(5, 6)

# # has path
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


graph.display()



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
  if len(edges_visited) != len(graph.vertices):
    return False
  return tour


'''

  # don't do this check if we're on the final item
  # edges may not always have been visited

  # after the DFS, if there are any unvisited nodes left,
  # this means that there are unvisited vertices
  # this means not all nodes are connectedd
  # this means that this is not a euler tour
  # I want to roll this check into validate_euler_tour() function

'''


# validates if a graph is a euler tour or not
# checks the criteria that there are only either 0 or 2 vertices
# with odd connections
# if so, return the start and end nodes
# in the case where there are no odds
# the start and end nodes will be any same node
# to indicate that the graph will start and end at the same place
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



  # stores node, and the connections that it already has visited
  # first find if it is a euler problem
  # find the starting and end vertex
  # cycle through the graph, get each vertex
  # check the connections.
  # use DFS -> only go to the next connection if you look it up
  # in the hash, and see that it has avialable connections to leave
  # unless it is the final one

  # for key in graph.vertices(graph):
    # while cycling through,
    # if there's
    # if there's an additional odd,
    # we need to make sure that the odd is the final one
    # if there's an odd node that we find
    # we wipe edges visited
    # and start the cycle anew with the odd vertex
    #





