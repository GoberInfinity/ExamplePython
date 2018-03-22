# -*- coding: utf-8 -*-
"""
Given an array where elements are sorted in ascending order, convert it to a 
height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following 
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        middle = len(nums) // 2 
        left_part = nums[:middle]
        right_part = nums[middle+1:len(nums)]
        tree = TreeNode(nums[middle])
        tree.left = self.sortedArrayToBST(left_part)
        tree.right = self.sortedArrayToBST(right_part)
        return tree
       
Solution().sortedArrayToBST([-10,-3,0,5,9]);