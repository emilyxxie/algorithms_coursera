'''

On MSTs (Minimal Spanning Trees):

Imagine a graph with weights on the edges (weights being positive values only).
Any spanning tree of a graph is a subgraph that is connected and has no cycles.

A *minimum spanning tree* of a graph is the subset of the edges that
connects all the vertices of an edge-weighted undirected graph together
without any cycles and with the minimum possible edge weight.

Applications for MSTs:
- Dithering in image processing
- Network analysis
- Road networks, Google Maps

Simplest Way to find MSTs:

The simple greedy algorithm uses a graph-cutting technique. Cutting a graph simply means
coloring any random set of nodes gray. After cutting, examine all "crossing paths."
Crossing paths are the points where the gray and the white nodes intersect.
Out of these crossing paths, pick the shortest one. The shortest one is guaranteed to be
in the minimal spanning tree. After, re-cut the graph, finding
a cut with no black crossing edges. Find the next black edge. Repeat until
V - 1 edges are colored black. (The number of edges in your minimum spanning tree
will always be one less than the total vertices in the graph.)

What if not all edges are distinct?:
If that is the case, that means that there are multiple MSTs. The
greedy algorithm is still correct.

What if the graphs are not all connected? Then we will get an MST Forest, which comprises of
the MST of each connected component.

'''

