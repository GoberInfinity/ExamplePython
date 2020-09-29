# Graph

## Concepts

- **In degree**: Edges coming out
- **Out degree**: Edges coming in

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

- **Topological sort**

In order to have a topological sorting the graph must not contain any cycles.

It is an ordering of the vertices in such a way, that if there is an edge directed towards vertex $v_b$ from vertex $v_a$, then $v_a$ comes before $v_b$.

Using the example above there are two topological orders:

1. **1,2,3,4,5**
1. **1,2,3,5,4**

## Useful Information

- _Find the smallest set of vertices from which all nodes in the graph are reachable_
  The nodes with 0 **in degree** are the answer

## References

1. https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
1. https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
