# -*- coding: utf-8 -*-
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
     
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None 
        mlist = self.bfs(root,[]) 
        self.inPlace(root,mlist)
        
    def bfs(self,tree,nodes):
        if tree:
            nodes.append(tree.val)
            self.bfs(tree.left,nodes)
            self.bfs(tree.right,nodes)
        return nodes
    
    def inPlace(self, root,mList):
        current = root
        mList.pop(0)
        while mList:
            current.left = None
            if not current.right:
                nextNode = TreeNode(mList.pop(0))
                current.right = nextNode
            else:
                current.right.val = mList.pop(0)
            current = current.right
            
#Morris Traversal
"""
def flatten(self, root):
    if not root:
        return
    
    # using Morris Traversal of BT
    node=root
    
    while node:
        if node.left:
            pre=node.left
            while pre.right:
                pre=pre.right
            pre.right=node.right
            node.right=node.left
            node.left=None
        node=node.right
"""