#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (62.91%)
# Likes:    18528
# Dislikes: 552
# Total Accepted:    4.5M
# Total Submissions: 7.1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointers approach. one pointer to for reading the array
        # and another pointer to keep track of the position to place the next non-zero element.
        read_ptr = 0
        write_ptr = 0
        n = len(nums)

        # early return if array has only one element. No empty array case is not possible as per constraints.
        if n == 1:
            return
        
        # read the array. every element needs to be read. so for loop.
        for read_ptr in range(len(nums)):
            # yes shift element to left.
            # one case. element is non-zero.
            if nums[read_ptr] != 0:
                nums[write_ptr] = nums[read_ptr]
                # increment write pointer only when we write a non-zero element.
                write_ptr += 1


        # all the non-zero elements are now at the beginning of the array.
        # write_ptr is now at the position where the next non-zero element would go.
        # fill the remaining elements with zero.
        for i in range(write_ptr, n):
            nums[i] = 0

        return
    

# @lc code=end

def main():
    sol = Solution()
    print("\n283. Move Zeroes\n")
    # Example 1
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums, "\n")     # Output should be [1,3,12,0,0]

    # Example 2
    nums = [0]
    sol.moveZeroes(nums)
    print(nums, "\n")     # Output should be [0]

if __name__ == "__main__":
    main()
