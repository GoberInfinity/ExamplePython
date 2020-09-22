"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            left, right = q.popleft(), q.popleft()

            if not left and not right:
                continue
            if (not left or not right) or (left.val != right.val):
                return False
            q += [left.left, right.right, left.right, right.left]

        return True
