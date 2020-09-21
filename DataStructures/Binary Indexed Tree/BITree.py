"""
input = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
biarray = [2, 3, 1, 7, 2, 5, 4, 21, 6, 13, 8, 30]
           1  2  3  4  5  6  7  8   9  10  11  12
(index, val)
                        0
(1,2)     (2,3)       (4,7)              (8,21)
          (3,1)   (5,2)   (6,5)    (9,6)(10,13)(12,30)
                          (7,4)          (11,8)
"""


class BITree:
    # Partial sums are stored in bit
    def __init__(self, array):
        self.array_len = len(array)
        self.bit_array = [0] * (self.array_len + 1)
        # Store the actual values in bit_array using update()
        for index in range(self.array_len):
            self.update(index, array[index])

    # The given value 'val' is added to BITree[i] and
    # all of its ancestors in tree.
    def update(self, index, value):
        # index in bit_array is 1 more than the index in array
        index += 1

        # Traverse all ancestors and add their 'value'
        while index <= self.array_len:
            self.bit_array[index] += value

            # Update index to that of parent in update View
            index += index & (-index)
            """   0   ->   2   ->   3
                0   0    2  0     2   1
            """

    # Search in bit_array
    def query(self, index):
        result = 0
        # index in bit_array is 1 more than the index in arr[]
        index += 1
        # Traverse ancestors of BITree[index]
        while index > 0:
            result += self.bit_array[index]
            # Move index to parent node
            index -= index & (-index)
        return result


freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bitree = BITree(freq)
print("Sum of elements in arr[0..5] is " + str(bitree.query(5)))
