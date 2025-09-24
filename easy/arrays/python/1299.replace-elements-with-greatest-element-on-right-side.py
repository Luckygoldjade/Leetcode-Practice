#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
#
# algorithms
# Easy (71.58%)
# Likes:    2781
# Dislikes: 257
# Total Accepted:    494.3K
# Total Submissions: 689.7K
# Testcase Example:  '[17,18,5,4,6,1]'
#
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with
# -1.
# 
# After doing so, return the array.
# 
# 
# Example 1:
# 
# 
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# 
# 
# Example 2:
# 
# 
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        return []
    
# @lc code=end

def main():
    sol = Solution()

    # Example 1
    arr = [17,18,5,4,6,1]
    print(sol.replaceElements(arr))
    # Output: [18,6,6,6,1,-1]

    # Example 2:
    arr = [400]
    print(sol.replaceElements(arr))
    # Output: [-1]

    return 0

if __name__ == "__main__":
    main()
