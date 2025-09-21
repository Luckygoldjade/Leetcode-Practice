#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (34.40%)
# Likes:    3072
# Dislikes: 198
# Total Accepted:    515.5K
# Total Submissions: 1.5M
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        """
        Check if the given array is a valid mountain array.
        A valid mountain array must have at least 3 elements, with a peak element.
        No inversions or plateaus are allowed.
        """
        # early exit
        if len(arr) < 3:
            return False
        
        # walk the array until find the peak
        # it must be strictly increasing
        read_ptr = 0
        for read_ptr in range(1, len(arr)):
            if arr[read_ptr] <= arr[read_ptr - 1]:
                break

        # if no peak or peak is at the ends
        if read_ptr == 1 or read_ptr == len(arr) - 1:
            return False

        # walk the array down from the peak
        # it must be strictly decreasing
        for read_ptr in range(read_ptr + 1, len(arr)):
            if arr[read_ptr] >= arr[read_ptr - 1]:
                return False


        # if we reached the end, it's a valid mountain
        return True


# @lc code=end

def main():

    sol = Solution()
    # Example 1:
    arr = [2,1]
    # Output: false
    print(sol.validMountainArray(arr))

    # Example 2:
    arr = [3,5,5]
    # Output: false
    print(sol.validMountainArray(arr))

    # Example 3:
    arr = [0,3,2,1]
    # Output: true
    print(sol.validMountainArray(arr))

    # Extra test cases
    arr = [0,2,3,4,5,2,1,0]
    print(sol.validMountainArray(arr))  # True

    # Edge cases
    print(sol.validMountainArray([0,1,2,3,4,5,6,7,8,9]))  # False

    # Edge cases
    print(sol.validMountainArray([9,8,7,6,5,4,3,2,1,0]))  # False

if __name__ == "__main__":
    main()
