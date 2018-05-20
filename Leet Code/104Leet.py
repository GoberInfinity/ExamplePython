# -*- coding: utf-8 -*-
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node. 

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.depthTree(root,[],1)
        
    def depthTree(self,root,levels,level):
        if root:
            levels.append(level)
            self.depthTree(root.left, levels, level+1)
            self.depthTree(root.right, levels, level+1)
        return max(levels)
    
    #Other solution
    """
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    """