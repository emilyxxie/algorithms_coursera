'''

Two vertices, v & w, are considered "strongly connected" if there is
a directed path from v to w and a directed path from w to v.

An example of a strong component application would be the food web, with
animals that mutually eat each other.

A brute force way to find strongly connected components would be to find all
cycles using recursion, keeping track of every time a vertex
is encountered twice in a recursive stack. However, this is a rather
inefficient method.

This implementation uses Kosaraju's algorithm, which computes strong components
in linear time using two sweeps of DFS:

1) Find the reverse post-order traversal of a graph.
2) Process a transposed graph with DFS using the reverse post-order from step 1

Time complexity: linear -> O(e+v). We visit each vertice and edge.
Space complexity: linear -> O(v). (Though this requires creation of a reversed graph.)

Intuition behind why this works:

##########

hard to understanding in writing.
Revisit video for diagram / awesome explanation:
https://www.youtube.com/watch?v=RpgcYiky7uw

##########

Think of it like this: each of the connected components can be thought of as a
set. If we abstract these sets, they create a DAG.
There is a guarantee that at least one of the vertices in a set (let's call it Vertex Y)
will be processed after the items from the set it points to.

Reversing the graph still preserves the connected components, aka cycles.
At the same time, because of this reversal, we prohibit Vertex Y from exploring the
vertex that it's connected to (let's call it Vertex W) outside of its set / component.

Vertex Y and Vertex W will have swapped directions, but the reverse
post-order travseral will ensure that Vertex W will not explore the
already-considered component that Vertex Y is part of.

'''

from directed_graph import DirectedGraph
import string


class KosarajuStrongComponents(object):

  def __init__(self, digraph):
    self.post_order = []
    self.visited    = []
    self.components = {}
    self.digraph    = digraph
    self.reversed_graph = DirectedGraph()

  #---------------------------------
  # public api
  #---------------------------------

  def find_strong_components(self):
    '''
    Pre-process the graph to find strongly
    connected components using Kosaraju's algorithm.
    '''
    for key in self.digraph.vertices:
      if key not in self.visited:
        self.__dfs(key)

    self.post_order.reverse()
    self.__reverse_graph()

    component_index = 0
    for key in self.post_order:
      if key not in self.components:
        self.__dfs_for_reversed(key, component_index)
        component_index += 1

    return self.components


  def is_strongly_connected(self, v1, v2):
    return self.components[v1] == self.components[v2]

  #---------------------------------
  # private helpers
  #---------------------------------

  def __reverse_graph(self):
    for key in self.digraph.vertices:
      vertex = self.digraph.get_vertex(key)
      if not key in self.reversed_graph.vertices:
        self.reversed_graph.add_vertex(key, vertex.val)
      for c in vertex.get_connections():
        connection = self.digraph.get_vertex(c)
        if not c in self.reversed_graph.vertices:
          self.reversed_graph.add_vertex(c, connection.val)
        self.reversed_graph.get_vertex(c).add_connection(key, vertex.val)

  def __dfs(self, key):
    self.visited.append(key)
    vertex = self.digraph.get_vertex(key)
    for connection in vertex.get_connections():
      if connection not in self.visited:
        self.__dfs(connection)
    self.post_order.append(key)

  def __dfs_for_reversed(self, key, component_index):
    self.components[key] = component_index
    vertex = self.reversed_graph.get_vertex(key)
    for connection in vertex.get_connections():
      if connection not in self.components.keys():
        self.__dfs_for_reversed(connection, component_index)
