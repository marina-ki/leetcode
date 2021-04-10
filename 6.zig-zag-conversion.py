#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        a = [""] * numRows
        b = 0
        reverse = False
        for i in range(len(s)):
            a[b] += s[i]
            if reverse:
                b -= 1
                if b == 0:
                    reverse = False
            else:
                b += 1
                if b == numRows - 1:
                    reverse = True
        return ''.join(a)

# @lc code=end
