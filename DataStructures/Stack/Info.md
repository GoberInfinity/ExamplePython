# Stack

## Notes

LIFO (last in, first out) data structure, the push and pop operations occur only at the top of the stack. Additionally, a peek operation may give access to the top without modifying the stack.

If the stack is full and does not contain enough space to accept an entity to be pushed, the stack is then considered to be in an overflow state.

When moving a and oversized data item into a stack location that is not large enough to contain it malicious parties may attempt to take advantage of this type of implementation by providing oversized data input to a program that does not check the length of input.

## Types:

- Min stack: Contains the min element so far
- Max stack: Contains the max element so far

## References

https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
