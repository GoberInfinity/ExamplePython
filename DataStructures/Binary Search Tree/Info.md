# Binary Search Tree

## Notes

Is a binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree. Binary search trees allow binary search for fast lookup, addition and removal of data items. The whole lookup takes time proportional to the binary logarithm of the number of items stored in the tree.

## Algorithms

```
   20
  /  \
10    30
     /  \
    25    40
```

- Validation of a binary search tree

  You need to check two conditions:

  1. If the node is the left child of its parent, then it must be smaller than (or equal to) the parent and it must pass down the value from its parent to its right subtree to make sure none of the nodes in that subtree is greater than the parent
  1. if the node is the right child of its parent, then it must be larger than the parent and it must pass down the value from its parent to its left subtree to make sure none of the nodes in that subtree is lesser than the parent.

  ```
  isBST(current, minKey, maxKey)
      if (current == NULL) return true;
      if (current.val < minKey || current.val > maxKey) return false;

      return isBST(current.left, minKey, current.val-1) && isBST(current.right, current.val+1, maxKey);
  ```

## Questions

- Are duplicates values allowed?
- What kind of information is stored in the binary search tree?

## Useful information

- _Is binary tree a binary search tree?_
  In a binary search tree inorder traversal retrieves the keys in ascending sorted order or the recursive solution

## References

https://en.wikipedia.org/wiki/Tree_traversal
