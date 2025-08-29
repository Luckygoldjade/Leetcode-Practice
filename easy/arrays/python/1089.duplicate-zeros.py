#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (52.87%)
# Likes:    2748
# Dislikes: 775
# Total Accepted:    510.4K
# Total Submissions: 964.1K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return
# anything.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 9
# 
# 
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        The array size is fixed and new duplicate zeros cannot be added.
        When a zero is detected, the elements to the right are shifted one position to the right.
        """
        n = len(arr)
        # Prescan of the array to count zeros
        zero_count = 0
        for i in range(n):
            if arr[i] == 0:
                zero_count += 1
        # Shift elements to the right by the number of zeros found
