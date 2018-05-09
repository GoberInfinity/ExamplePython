# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:00:04 2018

@author: Gober
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'DataStructures')))
from LinkedList.Linked_list import LinkedList, Element

def is_palindrome(ll):
    if not ll:
        return False
    
    fast =  slow = ll.head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next 
        fast = fast.next.next
    
    if fast:
        slow = slow.next
        
    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next
    
    return True 
    
e1 = Element('p')
e2 = Element('e')
e3 = Element('p')
e4 = Element('p')
e5 = Element('e')
e6 = Element('p')

o1 = Element('o')
o2 = Element('s')
o3 = Element('o')

a1 = Element('p')
a2 = Element('e')
a3 = Element('p')
a4 = Element('p')
a5 = Element('a')
a6 = Element('p')

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
print(is_palindrome(ll))

ll2 = LinkedList(o1)
ll2.append(o2)
ll2.append(o3)
print(is_palindrome(ll2))

ll3 = LinkedList(a1)
ll3.append(a2)
ll3.append(a3)
ll3.append(a4)
ll3.append(a5)
ll3.append(a6)
print(is_palindrome(ll3))