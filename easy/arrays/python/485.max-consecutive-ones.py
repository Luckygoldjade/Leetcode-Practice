#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (62.83%)
# Likes:    6378
# Dislikes: 475
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '[1,1,0,1,1,1]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s. The maximum number of consecutive 1s is 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        only 0's and 1's in list.
        """
        # loop through list and start count on first 1.
        current_cnt = 0
        best_cnt = 0
        # after first 1, exit on 0.
        for ind in range(len(nums)):
            if nums[ind] == 1:
                current_cnt += 1
                if current_cnt > best_cnt:
                    best_cnt = current_cnt
            else:
                # reset current count on 0.
                # no break on 0. it will continue counting to end.
                current_cnt = 0

        return best_cnt


# @lc code=end

def main():
    # Example 1
    nums = [1,1,0,1,1,1]
    # Output: 3
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums))

    return

if __name__ == "__main__":
    main()
