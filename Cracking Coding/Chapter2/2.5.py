# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:30:09 2018

@author: Gober
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'DataStructures')))
from LinkedList.Linked_list import LinkedList, Element

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
    print('\n')
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
sum_lists(ll,ll2)