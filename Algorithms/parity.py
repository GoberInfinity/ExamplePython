def parity(num):
    """
    Given an integer compute its parity (number of set bits). for negative numbers
    the MSB will be set, take that into account while counting set bits.
    """
    count = 0
    if num < 0:
        num = -num
        count = 1
    while num != 0:
        count += 1
        num = num & (num - 1)
    return count


print(parity(-4))
