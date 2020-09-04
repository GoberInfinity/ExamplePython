# -*- coding: utf-8 -*-
"""
Given a spreadsheet column string like AA, AZ etc, decode it into its numeric 
value
"""


class Solution:
    def spreadsheet_decoding(self, str):
        value = 0
        for c in str:
            value = value * 26 + ord(c) - ord("A") + 1
        return value


print(Solution().spreadsheet_decoding("AA"))
