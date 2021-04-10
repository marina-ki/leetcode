#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        minus = False
        a = 0
        if s == "":
            return 0
        if s[0] == "-":
            minus = True
            s = s[1::]
        elif s[0] == "+":
            s = s[1::]
        for i in range(len(s)):
            try:
                a = a * 10 + int(s[i])
            except:
                break
        if minus:
            if -a < - 2 ** 31:
                a = 2 ** 31
            return -a
        else:
            if a > 2 ** 31 - 1:
                a = 2 ** 31 - 1
            return a


# @lc code=end
