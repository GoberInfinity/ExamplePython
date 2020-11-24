# Common Strategies

## Fast and Slow Pointer

You begin with two pointers/positioning to the initial node/element, you need to move two times the fast pointers each time the slow pointer moves forward or move the fast pointer with a certain criteria

Related to: [linked list](../DataStructures/LinkedList/Info.md),[list]()

## Two pointers

One pointer starts from the beginning while the other pointer starts from the end, the algorithm ends when they both meet or they reach certain criteria.

## Sliding window

A sliding window is a **sub array/list** of length _n_ of the original **array/list**.
For example, if the original array is [a b c d] and we have a sliding windows of size _2_ the technique is going to check the elements in chunks of _2_: [a, b], [b, c], [c, d]

There are two types of sliding window:

1. Fixed Windows: The length of the window is fixed
1. Two pointers + criteria: The window size is not fixed, usually it asks you to find a sub array that meets the criteria

Related to: [arrays](), [strings]()

## Single Heap

You can use a single heap with a fixed size to get the first top _k_ largest or smallest element(s) (you need to insert the first _k_ elements in the heap before beginning the iteration), after that you can go trough the array from the _kth_ element to the end and each time you find a larger/smaller number than the smallest/larger number in the top of the (min/max)heap you delete the element and insert the new one.

A single heap it is also used to sort a list of _k_ unsorted lists, you need to create a heap with the size of the number of lists and every time you remove an element from the heap, you need to append a new value from the list where the item was remove used to be.

## Two Heaps

It is common when there is a set of elements and you need to divide them into two parts, you can know the smallest element in one part and the biggest element in the other part using min heap and max heap.
