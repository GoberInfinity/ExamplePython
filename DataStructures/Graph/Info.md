# Graph

## Concepts

- **In degree**: Edges coming in
- **Out degree**: Edges coming out

## Representation

You can model a graph in different ways:

- **Adjacency Matrix**
  For a graph with **∣V∣**, an adjacency matrix is a **∣V∣×∣V∣** matrix of 0s and 1s, where the entry in row _i_ and column _j_ is 1 if and only if the edge _(i,j)_ is in the graph. If you want to indicate an edge weight, put it in the _(i,j)_ entry, and reserve a special value (perhaps null) to indicate an absent edge
- **Adjacency List**
  Each vertex _i_ is an entry on a dictionary and the values of that entry is the vertices adjacent to it.
- **Edge List**
  Array of **E** edges, each edge is an element in the array containing the vertex numbers. If edges have weights, add either a third element to the array.

## Algorithms

```
1 --> 2 --> 4
      |    ^
      |   /
      v /
      3 --> 5
```

- **BFS**

  Begin from a selected node and traverse the graph layerwise thus exploring the neighbor nodes (nodes which are directly connected to source node) then you must move towards the next-level neighbor nodes.

  Using the example above an example of BFS is:

  - 1,2,3,4,5

- **DFS**

  Recursive algorithm that searches exhaustively all the nodes by going ahead, if possible, else by backtracking. Backtrack means that when you are moving forward and there are no more nodes along the current path, you move backwards on the same path to find nodes to traverse.

  Using the example above an example of DFS is:

  - 1,2,4,3,5

- **Topological sort**

  In order to have a topological sorting the graph must not contain any cycles. It is an ordering of the vertices in such a way, that if there is an edge directed towards vertex $v_b$ from vertex $v_a$, then $v_a$ comes before $v_b$.

  The first vertex in topological sorting is always a vertex with in degree 0. Topological Sorting for a graph is not possible if the graph is not a DAG.

  In topological sort you only need to perform a DFS and when you reach the base case (current has no more nodes to visit) you need to append current to the left of a list

  Using the example above there are two topological orders:

  - 1,2,3,4,5
  - 1,2,3,5,4

## Edge Cases

- Graph with cycles
- Graph with not connected nodes `1->2 3`
- Graph that have connected nodes but you can not reach them `1->2<-3 `

## Useful Information

- _Find the smallest set of vertices from which all nodes in the graph are reachable_
  The nodes with 0 **in degree** are the answer

## References

1. https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
1. https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
