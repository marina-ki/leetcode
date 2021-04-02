#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x > 0:
            while x > 0:
                q, mod = divmod(x, 10)
                res = res * 10 + mod
                x = q
        else:
            x = -x
            while x > 0:
                q, mod = divmod(x, 10)
                res = res * 10 + mod
                x = q
            res = -res
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            return 0
        else:
            return res
# @lc code=end

