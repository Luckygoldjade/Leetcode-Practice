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
        # There are two main approaches to solve this problem:
        # 1. Use a two-pass algorithm to first count the zeros and then shift elements.
        # Moving-boundary pre-scan. Compute possible_dups How many zeros can actually be duplicated within the fixed size 
        # and the last readable index.

        # 2. Use a single pass with a write pointer to overwrite elements in place.
        # Virtual-length pre-scan. Compute: total_zeros (all zeros, not just duplicable).

        # I will use the moving-boundary pre-scan approach. First approach
        n = len(arr)


        possible_dups = 0
        last_readable = n - 1

        # Pre scan to see how many zeros can be duplicated
        # left is boundary pointer
        left = 0
        while left <= last_readable - possible_dups:
            if arr[left] == 0:
                # special case: zero at the last readable position
                if left == last_readable - possible_dups:
                    # If we encounter a zero at the last readable position,
                    # we just set it to zero and reduce the last readable index by one.
                    arr[last_readable] = 0  # just set the last element to zero
                    last_readable -= 1
                    left += 1
                    break
                possible_dups += 1
            left += 1



        # backward filling of output array
        for i in range(last_readable - possible_dups, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0      # duplicate the zero
            else:
                arr[i + possible_dups] = arr[i]

        return None
    
# @lc code=end


def main():
    solution = Solution()
    print("\n")
    # Example 1 test case
    arr1 = [1,0,2,3,0,4,5,0]
    solution.duplicateZeros(arr1)
    print("Example 1 output:", arr1)
    # Output: [1,0,0,2,3,0,0,4]

    # Example 2 test case
    arr2 = [1,2,3]
    solution.duplicateZeros(arr2)
    print("Example 2 output:", arr2)
    # Output: [1,2,3]

    return

if __name__ == "__main__":
    main()
