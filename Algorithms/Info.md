## collapsible markdown?

# Table of Contents

1. [Binary Search](#binary_search)

## binary_search

<details>

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

1. Compare x with the middle element. `mid = left + (right - left) // 2`
1. `If` x is equal to the mid element return mid index.
1. `Else If` x is greater than the mid element, then x can only be in right half sub array after the mid element, so left is going to be `mid + 1`
1. `Else` (x is smaller) recur for the left half, so right is going to be `mid - 1`

</details>

## References

<details>

### Binary Search

https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

</details>
