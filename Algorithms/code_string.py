"""
Given a number encode it into a spreadsheet column title.
1 => A
26 => AA
"""


class Solution:
    def codeString(self, number):
        # @param number : int
        # @return an string
        if number == 0:
            return ""
        solution = ""
        while number > 0:
            digit = number % 26
            if digit == 0:
                solution += "Z"
                number = number // 26 - 1
            else:
                char_num = ord("A") + digit - 1
                solution += chr(char_num)
                number //= 26
        return solution[::-1]


print(Solution().codeString(28))
