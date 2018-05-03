# -*- coding: utf-8 -*-
"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a 
singly linked list
"""

class Element:    
    def __init__(self,value):
        self.next = None 
        self.value = value

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def append(self,new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:   
            self.head = new_element
            
    def print_linked(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
            
    def nthToLast(self, k):
        p1 = self.head
        p2 = self.head
        for i in range(k):
            if not p1.next:
                return None
            p1 = p1.next
            
        while p1:
            p1 = p1.next
            p2 = p2.next
            
        while p2:
            print(p2.value),
            p2 = p2.next
            
        
            
            
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

ll.nthToLast(5)