# -*- coding: utf-8 -*-
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict.get(char) != stack.pop():
                    return False
            else:
                return False
        return stack == []


if __name__ == "__main__":
    print(Solution().isValid("[]()[]"))
