# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:27:39 2018

@author: Gober
"""

# -*- coding: utf-8 -*-
"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. Note that the intersection is defined based on 
reference, not value. That is, if the kth node of the first linked list is the 
exact same node (by reference) as the jth node of the second linked list, then 
they are intersecting.
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'DataStructures')))
from LinkedList.Linked_list import LinkedList, Element
import copy

def intersection(l1,l2):
    if not l1 or not l2:
        return False 
    
    def get_tail_and_size(l):
        size = 1
        current = l.head
        while current.next:
            size += 1
            current = current.next
        return (size,current)

    l1_size, l1_tail = get_tail_and_size(l1)
    l2_size, l2_tail = get_tail_and_size(l1)

    if l1_tail is not l2_tail:
        return False
    
    shorter = l1.head if l1_size < l2_size else l2.head
    longer = l2.head if l2_size > l1_size else l1.head
    
    diff = abs(l1_size - l2_size)
    
    for i in range(diff):
        longer = longer.next
        
    while longer.value != shorter.value:
        longer = longer.next
        shorter = shorter.next 
        
    return longer.value
    
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

e1p = Element(7)
e2p = Element(4)
e3p = copy.deepcopy(e3)
e4p = copy.deepcopy(e4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

l2 = LinkedList(e1p)
l2.append(e2p)
l2.append(e3p)
l2.append(e4p)

print(intersection(ll,l2))