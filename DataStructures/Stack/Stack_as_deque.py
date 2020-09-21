"""
Stack as Deque

It provides you with a double ended queue which means that you can
append and delete elements from either side of the list

https://docs.python.org/3/library/collections.html#collections.deque

"""

from collections import deque

q = deque()

q.append("eat")  # add a new entry to the right side
q.append("sleep")
q.append("code")
q.pop()  # return and remove the rightmost item
