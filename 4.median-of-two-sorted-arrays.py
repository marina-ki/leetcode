#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        a = len(nums1) // 2
        if len(nums1) % 2 == 0:
            return (nums1[a-1] + nums1[a])/2
        else:
            return nums1[a]

# @lc code=end
