#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = str(x)
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
# @lc code=end
