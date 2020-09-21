import math


class SparseTable:
    def __init__(self, array):
        self.input = array
        self.input_len = len(self.input)
        self.lookup_table = []
        self.build_lookup_table()

    def build_lookup_table(self):
        # Is the biggest power of two range, that we have to support
        max_elements = math.floor(math.log2(self.input_len)) + 1
        lookup = [[None for _ in range(max_elements)] for _ in range(self.input_len)]

        # Minimum of single element subarrays is the same element.
        for i in range(0, self.input_len):
            lookup[i][0] = self.input[i]

        # Counter to increase 2^exp_count
        for exp_count in range(1, max_elements + 1):
            # Compute minimum value for intervals with size 2^exp_count
            for index_elem in range(0, self.input_len):
                if index_elem + (1 << exp_count) <= self.input_len:
                    prev_exp = exp_count - 1
                    lookup[index_elem][exp_count] = min(
                        lookup[index_elem][prev_exp],
                        lookup[index_elem + (1 << prev_exp)][prev_exp],
                    )
                else:
                    break
        self.lookup_table = lookup
        print(*lookup, sep="\n")

    def query(self, L, R):
        range_of_exponent = int(math.log2(R - L + 1))
        return min(
            self.lookup_table[L][range_of_exponent],
            self.lookup_table[R - (1 << range_of_exponent) + 1][range_of_exponent],
        )


a = SparseTable([7, 2, 3, 0, 5, 10, 3, 12, 18])
print(a.query(0, 4))  # min = 0
print(a.query(4, 7))  # min = 3
print(a.query(7, 8))  # min = 12
