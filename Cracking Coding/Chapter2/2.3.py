"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (Ie., 
any node but the first and last node, not necessarily the exact middle) of a 
singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""

import os
import sys

from LinkedList.Linked_list import Element, LinkedList

sys.path.append(os.path.abspath(os.path.join("../..", "DataStructures")))


def delete_middle_node(ll):
    current = ll.head
    for i in range(3):
        current = current.next
    current.value = current.next.value
    current.next = current.next.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
ll.append(e7)
ll.print_linked()
print("\n")
delete_middle_node(ll)
ll.print_linked()
