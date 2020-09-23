class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        serie = "1"
        elem = serie[0]
        elem_counter = 0

        for _ in range(n - 1):
            answer = ""
            for number in serie:
                if elem == number:
                    elem_counter += 1
                else:
                    answer += str(elem_counter) + str(elem)
                    elem = number
                    elem_counter = 1
            answer += str(elem_counter) + str(elem)
            serie = answer
            elem_counter = 0
            elem = serie[0]

        return answer


if __name__ == "__main__":
    print(Solution().countAndSay(6))
