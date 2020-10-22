# Dictionary (Hash Table)

## Notes

A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

A good hash function satisfies two basic properties:

1. It should be very fast to compute
1. It should minimize duplication of output values (collisions)

Hash collisions are practically unavoidable when hashing. Therefore, almost all hash table implementations have some collision resolution strategy to handle such events like:

- Separate chaining: Each bucket is independent, and has some sort of list (array or linked list) of entries with the same index. The time for hash table operations is the time to find the bucket (which is constant) plus the time for the list operation.

  For separate-chaining, the worst-case scenario is when all entries are inserted into the same bucket.
  ![separate_chaining](/Imgs/DataStructures/Dict/separe_chaining.jpg)
  Figure 1. Collision solved by separate chaining

- Separate chaining with other structures: By using a self-balancing binary search tree, the theoretical worst-case time of common hash table operations (insertion, deletion, lookup) can be brought down to O(log n) rather than O(n). However, this introduces extra complexity into the implementation, and may cause even worse performance for smaller hash tables, where the time spent inserting into and balancing the tree is greater than the time needed to perform a linear search on all of the elements of a list.

- Open addressing: All entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some **probe sequence**, until an unoccupied slot is found. When searching for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table.

  ![open_addressing](/Imgs/DataStructures/Dict/open_addressing.jpg)
  Figure 2. Hash collision resolved by open addressing with linear probing (interval=1). Note that "Ted Baker" has a unique hash, but nevertheless collided with "Sandra Dee", that had previously collided with "John Smith"

When an insert is made such that the number of entries in a hash table exceeds the product of the **load factor** and the current capacity then the hash table will need to be rehashed. Rehashing includes increasing the size of the underlying data structure and mapping existing items to new bucket locations.

## Concepts

- **Capacity**: Number of buckets in the hash table, and the initial capacity is simply the capacity at the time the hash table is created.
- **Load Factor**: The load factor is a measure of how full the hash table is allowed to get before its capacity is automatically increased.
- **Hash Function**: A function that takes data as input and outputs a hash code used as index in a hash table
- **Collision**: Hash function generates the same index for more than one key
- **Prove Sequence**: Sequence (e.g. 0,1,2 ...) of slots examined during a key search. Probe sequence must be permutation of slot numbers.We examine every slot in the table if we have to.But no slot is examined more than once.

## Questions

- Is it possible to have repeated values?
- How should I handle the collision?

## References

https://en.wikipedia.org/wiki/Hash_table
https://gateoverflow.in/18002/what-is-the-meaning-of-probe-sequence-in-hashing
