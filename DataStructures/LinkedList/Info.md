# Linked Lists

## Notes

One advantage of the linked list is that elements can be added indefinitely, while an array will eventually get filled or have to be resized (a costly operation that isn't always possible).

Linked lists also use more storage space in a computer's memory as each node in the list contains both a data item and a reference to the next node.

It follows that linked lists should be used for large lists of data where the total number of items in the list is changing.

## Algorithms

- **Fast Slow Pointer**

  You begin with two pointers to the initial node, you need to move two times the fast pointers each time the slow pointer moves forward. Applications:

  - Middle of the linked list
  - Detect cycle in linked list

## Useful Information

- **Return the head of a modified linked list**
  Before beginning to traverse the linked list remember to create an extra node that keeps track of the first element and modify the second one.

## References

1. https://www.interviewbit.com/tutorial/arrays-vs-linked-lists/
