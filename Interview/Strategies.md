# Common Strategies

## Fast and Slow Pointer

You begin with two pointers/positioning to the initial node/element, you need to move two times the fast pointers each time the slow pointer moves forward.

Related to: [linked list](../DataStructures/LinkedList/Info.md),[list]()

## Sliding window

A sliding window is a **sub array/list** of length _n_ of the original **array/list**.
For example, if the original array is [a b c d] and we have a sliding windows of size _2_ the technique is going to check the elements in chunks of _2_: [a, b], [b, c], [c, d]

There are two types of sliding window:

1. Fixed Windows: The length of the window is fixed
1. Two pointers + criteria: The window size is not fixed, usually it asks you to find a sub array that meets the criteria

Related to: [arrays](), [strings]()
