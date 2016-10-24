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

Typically, topological sort can be solved using a DFS and keeping reverse
post-order track of processed items. Post-order can be defined as the order
in which something is completed. For toplogical sort, we can create a stack
to track post-order, and then reverse it at the end.

'''

from directed_graph import DirectedGraph

class TopologicalSort(object):
  def __init__(self, dg):
    self.digraph = dg
    self.post_order = []
    self.visited = []

  # detects cycles and sorts topologically
  def topological_sort(self):
    for key in self.digraph.vertices:
      if key not in self.visited:
        self.__dfs(key)

    print(self.visited)
    # print(self.post_order)
    # return self.post_order.reverse()

  def __dfs(self, key, prev = None):
    self.visited.append(key)
    vertex = self.digraph.get_vertex(key)
    # print(key)
    # print(self.visited)
    for connection in vertex.get_connections():
      if connection not in self.visited:
        self.__dfs(connection, key)
    self.post_order.append(key)


dg = DirectedGraph()

for i in range(0, 7):
  dg.add_vertex(i, "Class %d" % (i))

dg.add_edge(0, 1)
dg.add_edge(0, 6)
dg.add_edge(1, 4)
dg.add_edge(0, 5)
dg.add_edge(5, 2)
dg.add_edge(3, 5)
dg.add_edge(3, 4)
dg.add_edge(3, 6)
dg.add_edge(6, 4)

print(dg)

print(dg.display())

ts = TopologicalSort(dg)
ts.topological_sort()

