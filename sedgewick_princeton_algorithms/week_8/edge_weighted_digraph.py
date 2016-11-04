'''

In edge-weighted digraphs, the edges are directed, with weighted edges.
Shortest-path applications are the most relevant; map directions, texture-mapping,
urban traffic planning, network routing protocols.

Relevant vocabulary:
  - Source-sink: From one vertex to another
  - Single source: From one vertex to every other
  - All pairs: Between all pairs of vertices

Restrictions on edge weights to consider:
  - Non-negative weights
  - Arbitrary weights
  - Euclidean weights

Cycle considerations:
  - No directed Cycles
  - No "negative cycles"

Simplfying assumptions:
  We'll assume shortest paths froms to each vertex v will exist.
  We won't worry abotu the concept of "driving to an island"
  Single source shortest paths.
  Compute all paths shortest paths.

'''

class EdgeWeightedDigraph:

  '''

  An edge weighted graph maintains a node-indexed dictionary
  of adjacency lists of corresponding edges (each stored as a ref to the object).
  Since this is a directed graph, an edge will be filed under its starting node.

  In previous graphs, I created a separate object for my nodes / vertices.
  To simplify for this one, I'll store the value of my node
  directly as an index, and use a set to store all of the edges.

  '''

  def __init__(self):
    self.nodes = {}
    self.total_edges = 0

  def add_edge(self, edge):
    start = edge.start
    end = edge.end
    if start not in self.nodes:
      self.nodes[start] = set()
    else:
      print(self.nodes[start])
      self.nodes[start].add(edge)
      print(self.nodes[start])

    # if end does not exist, add it to the graph
    if end not in self.nodes:
      self.nodes[end] = set()
    self.total_edges += 1

  def count_nodes(self):
    return len(self.nodes.keys())

  def display(self):
    for node, edges in self.nodes.items():
      print(
        "%i => %s" % (node, [vars(edge) for edge in edges])
      )

class DirectedEdge:

  '''

  Directed edges are a bit simplier than non-directed edges
  since you only need to store start and end nodes.

  '''

  def __init__(self, start, end, weight):
    self.start = start
    self.end = end
    self.weight = weight


ewdg = EdgeWeightedDigraph()

ewdg.add_edge(DirectedEdge(1, 4, 0.5))
ewdg.add_edge(DirectedEdge(1, 7, 0.28))
ewdg.add_edge(DirectedEdge(2, 8, 0.1))
ewdg.add_edge(DirectedEdge(8, 1, 0.2))

ewdg.display()

