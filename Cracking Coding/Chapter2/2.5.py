# -*- coding: utf-8 -*-
"""
Sum Lists: You have two numbers represented by a linked list, where each node 
contains a single digit. The digits are stored in reverse order, such that the 
1 's digit is at the head of the list. Write a function that adds the two numbers 
and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .That is,617 + 295.
Output: 2 - > 1 - > 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 - > 1 - > 2. That is, 912.
"""

import os
import sys

from LinkedList.Linked_list import Element, LinkedList

sys.path.append(os.path.abspath(os.path.join("../..", "DataStructures")))


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.append(Element(result % 10))
        carry = result // 10

    if carry:
        ll.append(Element(carry))
    print("\n")
    ll.print_linked()


e1 = Element(7)
e2 = Element(1)
e3 = Element(6)
e4 = Element(5)
e5 = Element(9)
e6 = Element(2)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

ll2 = LinkedList(e4)
ll2.append(e5)
ll2.append(e6)

ll.print_linked()
print("\n")
ll2.print_linked()
sum_lists(ll, ll2)
