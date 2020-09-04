# -*- coding: utf-8 -*-
"""

"""

from collections import deque


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
        right_part = nums[middle + 1 : len(nums)]
        tree = TreeNode(nums[middle])
        tree.left = self.sortedArrayToBST(left_part)
        tree.right = self.sortedArrayToBST(right_part)
        return tree


def level(root):
    if not root:
        return None
    que = deque([root])

    while que:
        max_elements = len(que)

        while max_elements > 0:
            current = que.popleft()
            print(current.val, end=" ")
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
            max_elements -= 1
        print(""),


level(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
