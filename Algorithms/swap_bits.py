"""
Given an integer and incices of 2 bits, swap the bits.
"""


class Solution:
    def swap_bits(self, num, i, j):
        if num == 0:
            return 0
        if num == 1:
            return 1

        bit_at_i = (num >> i) & 1
        bit_at_j = (num >> j) & 1

        print(bit_at_i)
        print(bit_at_j)

        if bit_at_i != bit_at_j:
            num = (1 << i) ^ num
            print(1 << i)
            num = (1 << j) ^ num
        return num


print(Solution().swap_bits(54, 0, 1))
