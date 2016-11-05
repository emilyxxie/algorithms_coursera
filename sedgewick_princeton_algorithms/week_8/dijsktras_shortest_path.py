'''

Challenge: Find the shortest path from point v to every other vertex in a graph with
non-negative weights, assuming that a shortest-paths tree (SPT) solution exists.

Djikstra's algorithm solves for this efficiently, using an
edge relaxation technique combined with certain optimality conditions.

"Edge relaxation" simply means taking an edge into consideration as part
of your final solution. In the context of Prim's algorithm, it would simply mean
taking the shortest edge from the frontier, and adding it to your MST. Each successful
relaxation of a node gets an increasingly shorter distance to V.

Rules:
1) Consider vertices in increasing order of distance from a source
2) Add vertex to tree and relax all edges pointing from that vertex.

Relaxation ensures that the tree so far to V always carries the
current shortest distance.

Analysis of run time of Dijstrak's algorithm:
Using a binary heap, Dijkstra's algorithm, runs at
O(ElogV).


'''

import math
import heapq
import sys
import collections
from edge_weighted_digraph import EdgeWeightedDigraph, DirectedEdge

class DijkstrasSP:

  def __init__(self, graph):
    self.graph = graph
    # heap contains nodes, min-prioritized by distance
    self.node_queue = []
    # node => tuple (total distance, source + prev node)
    self.shortest_paths = {}

  def get_shortest_paths(self, source):
    # seed the first value
    source_distance = 0
    self.shortest_paths[source] = collections.namedtuple(
      'shortest_path', 'distance prev_node'
    )
    self.shortest_paths[source].distance = source_distance
    self.shortest_paths[source].prev_node = None
    heapq.heappush(
      self.node_queue,
      (source_distance, source)
    )

    while self.node_queue:
      node = heapq.heappop(self.node_queue)[1]
      source_distance = self.shortest_paths[node].distance

      for edge in self.graph.nodes[node]:
        frontier_i = edge.end
        edge_distance = edge.weight
        # if the node isn't already in shortest paths
        # then instantiate the node, giving it a distance of infinity
        if frontier_i not in self.shortest_paths:
          self.shortest_paths[frontier_i] = collections.namedtuple(
            'shortest_path',
            'distance prev_node'
          )
          self.shortest_paths[frontier_i].distance = math.inf

        frontier = self.shortest_paths[frontier_i]
        if source_distance + edge_distance < frontier.distance:
          frontier.distance = source_distance + edge_distance
          frontier.prev_node = node
        heapq.heappush(
          self.node_queue,
          (frontier.distance,
            frontier_i)
        )



  def display_shortest_path(self, start_node):
    for node, vals in self.shortest_paths.items():
      print("Node %d: " % (node), end = '')
      while node != None:
        print("%d, " % (node), end = '')
        node = self.shortest_paths[node].prev_node
      print("Total distance: %d" % (vals.distance))


ewdg = EdgeWeightedDigraph()

ewdg.add_edge(DirectedEdge(0, 1, 5))
ewdg.add_edge(DirectedEdge(0, 7, 8))
ewdg.add_edge(DirectedEdge(0, 4, 9))

ewdg.add_edge(DirectedEdge(1, 3, 15))
ewdg.add_edge(DirectedEdge(1, 2, 12))
ewdg.add_edge(DirectedEdge(1, 7, 4))

ewdg.add_edge(DirectedEdge(7, 2, 7))
ewdg.add_edge(DirectedEdge(7, 5, 6))

ewdg.add_edge(DirectedEdge(4, 7, 5))
ewdg.add_edge(DirectedEdge(4, 5, 4))
ewdg.add_edge(DirectedEdge(4, 6, 20))

ewdg.add_edge(DirectedEdge(3, 6, 9))

ewdg.add_edge(DirectedEdge(2, 3, 3))
ewdg.add_edge(DirectedEdge(2, 6, 11))

ewdg.add_edge(DirectedEdge(5, 2, 1))
ewdg.add_edge(DirectedEdge(5, 6, 13))

# ewdg.display()
dsp = DijkstrasSP(ewdg)
dsp.get_shortest_paths(0)
dsp.display_shortest_path(0)



