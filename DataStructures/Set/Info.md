# Set

## Notes

Unordered collection data type with no duplicate elements

## Types

- Static sets: Don't change after they are constructed. Static sets allow only query operations on their elements
- Dynamic sets: Allow the insertion and deletion of elements from the set
- Multi set: Similar to a set but allows repeated values. This is used in two distinct senses: either equal values are considered identical, and are simply counted, or equal values are considered equivalent, and are stored as distinct items, python has collections.Counter, which is similar to a multiset.

## Concepts

- **Cardinality**: Let S be a set. If there are exactly n distinct elements in S, we say S is a finite set and that n is the cardinality of S. The cardinality of S is denoted by $|S|$
- **Power Set**: The power set of S is the set of all subsets of S. e.g.
  P( {1,2} ) = { 0, {1}, {2}, {1,2} }
- **Cartesian Product**: Let S and T be sets. The Cartesian product of S and T, denoted by $S x T$,is the set of all ordered pairs (s,t). e.g.
  S = {1,2}, T = {a,b,c}
  S x T = { (1,a), (1,b), (1,c), (2,a), (2,b), (2,c) }
  T x S = { (a,1), (a, 2), (b,1), (b,2), (c,1), (c,2) }
- **Cardinality of the Cartesian product**: |S x T| = |S| \* |T|
- **Disjoint sets**: Two sets are called disjoint if their intersection is empty.

## Algorithms:

- **Power Set**

![](/Imgs/DataStructures/Set/powerset.png)

## References

https://en.wikipedia.org/wiki/Set_(abstract_data_type)
https://people.cs.pitt.edu/~milos/courses/cs441/lectures/Class7.pdf
https://leetcode.com/problems/subsets/solution/
