# Binary Tree

## Concepts

- **Leaf**: A non-root node with no children.
- **Ancestor**: $a$ is an ancestor of $b$ if $b$ is located in a left or right subtree whose root node is $a$.
- **Heigh**: Number of edges between the root node and its furthest leaf.
- **Diameter**: Length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## Representation

You can model a binary tree in different ways:

- **List**
  To represent a binary tree as list you need to use the index $i$ of the element in order to get its left and right child:

  - Left: $i * 2 + 1$
  - Right: $i * 2 + 2$

- **Object**
  Each node can have two child nodes (left, right), you can reach any node traversing though the root.

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

  Applications:

  - Retrieves the keys in ascending sorted order a binary search tree

- Reverse in-order: (Right , Root, Left)

  Applications:

  - Retrieves the keys in descending sorted order in binary search tree

- Postorder: (Left, Right, Root) or follow the $+$ symbols: 2,3,1

  Applications:

  - Delete/Copy of a binary tree

- Breadth-first search:

  Traverse all the elements of the tree level by level: 1,2,3

- Inorder Morris Traversal:
  It helps to traverse a binary tree without stack or recursion, the algorithms says that:

  ```
  current = root
  while current it not null
    if not current.left
      print current
      current = current.right
    else
      # It's important to validate that the predecessor is not the same as
      # current if we don't do that, we're going to create an infinite loop)
      predecessor = find the right most node of the left subtree of current
      if not exists predecessor.right
        # It creates the blue arrows
        predecessor.right = current
        current = current.left
      else
        # Deletes the blue arrows in order to re create the original tree
        predecessor.right = none
        print current
        current = current.right
  ```

  ![morris](/Imgs/DataStructures/BinaryTree/morris.jpg)
  Figure 1. Example of a morris traversal, blue numbers indicates the creation order of the links and the red numbers the deletion order.

## Questions

- What kind of binary tree is the tree?

## Edge Cases

- Trees with only right/left sub trees
- Infinite trees

## Useful Information

- _Height of tree_
  $1 + max(height(leftSubtree), height(rightSubtree)) $

- _Unique Trees_
  Given a tree with distinct elements, either pre or post order paired with in-order is sufficient to describe the tree uniquely. However, pre-order with post-order leaves some ambiguity in the tree structure.

- _Topological Sort_
  The pre-order traversal is a topologically sorted one, because a parent node is processed before any of its child nodes is done.

- _Delete/Copy a binary tree_
  Post order traversal ensures that the parent cannot be deleted/copied before all children are finished.

- _DFS vs BFS in infinite trees_
  Given a binary tree of infinite depth, depth-first search will never end because it will never reach an leaf node, breadth-first traversal will traverse a binary tree of infinite depth without problem.

  On the other hand, given a tree where the root has infinitely children, a depth-first search will visit all nodes (assuming it is not post-order, in which case it never reaches the root). By contrast, a breadth-first search will never reach the grandchildren, as it seeks to exhaust the children first.

  Thus, **simple depth-first or breadth-first searches do not traverse every infinite tree**, and are not efficient on very large trees.However, hybrid methods can traverse any (countably) infinite tree

## References

https://en.wikipedia.org/wiki/Tree_traversal
