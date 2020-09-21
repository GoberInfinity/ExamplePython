"""

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        current_node = head
        reversed_list_head = None
        while current_node:
            element_to_append = ListNode(current_node.val)
            element_to_append.next = reversed_list_head
            reversed_list_head = element_to_append
            current_node = current_node.next
        return reversed_list_head
