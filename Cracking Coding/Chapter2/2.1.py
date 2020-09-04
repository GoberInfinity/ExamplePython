# -*- coding: utf-8 -*-
"""
Write code to remove duplicates from an unsorted linked list.
"""


class Element:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
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

    def remove_dups(self):
        if not self.head:
            return None

        current = self.head
        seen = set([current.value])
        while current.next:

            if current.next.value in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.value)
                current = current.next
        pass


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(7)
e6 = Element(7)
e7 = Element(5)
e8 = Element(1)
e9 = Element(1)


# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
ll.append(e7)
ll.append(e8)
ll.append(e9)

ll.print_linked()
ll.remove_dups()
ll.print_linked()
