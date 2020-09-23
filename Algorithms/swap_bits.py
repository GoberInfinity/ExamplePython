"""
Given an integer and incices of 2 bits, swap the bits.
"""


def swap_bits(num, i, j):
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


print(swap_bits(54, 0, 1))
