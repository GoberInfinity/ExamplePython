# Algorithms

## Table of Contents

1. [Binary Search](#binary_search)
1. [Modulo](#modulo)

## binary_search

<details>

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

1. Compare x with the middle element. `mid = left + (right - left) // 2`
1. `If` x is equal to the mid element return mid index.
1. `Else If` x is greater than the mid element, then x can only be in right half sub array after the mid element, so left is going to be `mid + 1`
1. `Else` (x is smaller) recur for the left half, so right is going to be `mid - 1`

</details>

## modulo

<details>

The modulo operation (abbreviated “mod”, or “%”) is the remainder when dividing, for example:

- 11 mod 4 = 3, because 11 divides by 4 (twice), with 3 remaining
- 25 mod 5 = 0, because 25 divides by 5 (five times), with 0 remaining

The formula to calculate the modulo is $mod(a, n) = a - n * floor(a / n)$

There is a pattern in modulus:

- 0 % 3 = 0
- 1 % 3 = 1
- 2 % 3 = 2
- 3 % 3 = 0
- 4 % 3 = 1
- 5 % 3 = 2

- 0 % 3 = 0
- -1 % 3 = 2
- -2 % 3 = 1
- -3 % 3 = 0
- -4 % 3 = 2
- -5 % 3 = 1

The remainders start at 0 and increases by 1 each time, until the number reaches one less than the number we are dividing by. After that, the sequence repeats, in the case of negative numbers the logic is the same but in a decreasing order.

If you are trying to get modulus using negative number be aware that the output depends on the language you are using (they show different results).

</details>

## References

<details>

### Binary Search

https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

### Modulo

https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic

</details>
