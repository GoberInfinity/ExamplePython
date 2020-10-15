# Binary Tree

## Concepts:

- **Leaf**: A non-root node with no children.
- **Ancestor**: $a$ is an ancestor of $b$ if $b$ is located in a left or right subtree whose root node is $a$.
- **Heigh**: Number of edges between the root node and its furthest leaf.

## Algorithms

```
    - 1 +
      *
    /   \
 - 2 + - 3 +
   *     *
```

- Preoder: (Root, Left, Right) or follow the $-$ symbols: 1,2,3
- Inorder: (Left, Root, Right) or follow the $*$ symbols: 2,1,3
- Postorder: (Left, Right, Root) or follow the $+$ symbols: 2,3,1

## Useful Information

- _Height of tree_
  $1 + max(height(leftSubtree), height(rightSubtree)) $

- _Unique Trees_
  Given a tree with distinct elements, either pre or post order paired with in-order is sufficient to describe the tree uniquely. However, pre-order with post-order leaves some ambiguity in the tree structure.

- _Topological Sort_
  The pre-order traversal is a topologically sorted one, because a parent node is processed before any of its child nodes is done.

## References

https://en.wikipedia.org/wiki/Tree_traversal
