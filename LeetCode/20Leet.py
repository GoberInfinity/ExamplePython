class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if stack == [] or brackets.get(char) != stack.pop():
                    return False
            else:
                return False
        return stack == []


if __name__ == "__main__":
    print(Solution().isValid("[]()[]"))
