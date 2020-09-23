"""
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

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None

        if current:
            while current:
                if counter == position:
                    return current
                counter += 1
                current = current.next

        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head

        if position == 1:
            new_element.next = current
            self.head = new_element
        else:
            counter += 1
            while current:
                if counter == position:
                    tail = current.next
                    current.next = new_element
                    new_element.next = tail
                    break
                current = current.next
                counter += 1
        pass

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head

        if value == current.value:
            self.head = current.next
        else:
            while current:
                if current.next is None:
                    break
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
        pass

    def print_linked(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
