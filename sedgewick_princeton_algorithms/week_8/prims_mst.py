'''

Prim's is a special case of the greedy MST algorithm which continually
picks the smallest edge connected to the current tree until the
MST is size V - 1.

The priority queue is a heap that holds all edges reachable from the
current MST, and keeps them ordered from smallest to largest.
The algorithm pops the first edge off the priority queue,
and adds the corresponding unvisited node to an array of "already-marked" nodes.

To prevent cycles, we can simply avoid edges whose two nodes have already
been marked as visited. This works because in Prim's, you are working off an MST
that is one singular component (as opposed to Kruskal's).

We are considered done once we have V - 1 number of edges in our MST.

Prim's computes the MST in time proportional to O(NlogN), with N standing for number
of edges. Extra space is proportional to E.

Prim's also has an eager implementation, which saves some space complexity. (#TODO)

'''

import heapq
import string
import sys
from edge_weighted_graph import EdgeWeightedGraph, Edge, Node


class PrimsMST(object):

  def __init__(self, graph):
    self.graph = graph
    self.priority_queue = []
    self.MST = []
    self.visited_nodes = {}

  def find_MST(self):

    node = 0
    while len(self.MST) < len(self.graph.nodes) - 1:
      self.visited_nodes[node] = node
      for edge in self.graph.nodes[node].edges:
        if edge.other(node) not in self.visited_nodes:
          heapq.heappush(self.priority_queue, (edge.weight, edge))

      while node in self.visited_nodes and self.priority_queue:
        min_edge = heapq.heappop(self.priority_queue)[1]
        node = min_edge.either()
        if node in self.visited_nodes:
          node = min_edge.other(node)

      self.MST.append(min_edge)

  def display_MST(self):
    if not self.MST:
      self.find_MST()
    for edge in self.MST:
      node = edge.either()
      node2 = edge.other(node)
      print(node, node2)
