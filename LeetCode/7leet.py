# flake8: noqa
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        inverted_number = ""
        number = x
        reverse = False

        if x < 0:
            return -self.reverse(-x)
        elif x == 0:
            return 0

        while not reverse:
            if number == 0:
                inverted_number = int(inverted_number)
                break
            inverted_number = str(inverted_number) + str(number % 10)
            number = number // 10

        return inverted_number if inverted_number <= 0x7FFFFFFF else 0


if __name__ == "__main__":
    print(Solution().reverse(1534236469))
