'''

Topological sorting is a widely used digraph processing application that
creates a linear ordering of vertices based on what must be done first.
Vertices represent tasks, while edges represent precedence constraints.
Note that there can be more than one topological sort for a graph.

A simple example is precendence scheduling:
imagine a set of tasks that have to be completed with precedence constraints.
In which order should we schedule the tasks? Concretely, an example would be
classes and pre-requisites. To take class A, you first need class B.

A --> B

The topological sorting problem necessarily operates on a DAG, which is a digraph that
contains no cycles. If you have a cycle, you will not be able to solve the problem.

The classes and pre-requisite example can also give insight as to why you must have a DAG.
A cyclic graph would mean that something requires itself. e.g. HAA 51 requires HAA 51
before you can take it. This is simply illogical / would break.

Typically, topological sort can be solved using a DFS and keeping post-order
track of processed items. Post-order can be defined as the order
in which something is completed.

'''

from directed_graph import DirectedGraph
import sys

class TopologicalSort(object):

  def __init__(self, digraph):
    '''
    stack holds all vertices within current recursive call,
    used to detect cycles. Visited contains all vertices
    across all recursive calls.
    '''
    self.stack = []
    self.visited = []
    self.digraph = digraph
    self.post_order = []


  def topological_sort(self):
    '''
    acounts for cycles and sorts topologically
    '''
    for key in self.digraph.vertices:
      if key not in self.visited:
        self.__dfs(key)
    return self.post_order


  #---------------------------------
  # private helpers
  #---------------------------------

  def __dfs(self, key, prev = None):
    self.stack.append(key)
    vertex = self.digraph.get_vertex(key)
    for connection in vertex.get_connections():
      if connection not in self.stack and connection not in self.visited and connection != prev:
        self.__dfs(connection, key)
      self.__check_cycle(connection)
    self.visited += self.stack
    self.stack = []
    self.post_order.append(key)

  def __check_cycle(self, connection):
    if connection in self.stack:
      sys.exit("Cycle detected: %s" % ("".join(str(self.stack))))


