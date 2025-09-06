#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
#
# algorithms
# Easy (41.33%)
# Likes:    2464
# Dislikes: 249
# Total Accepted:    586.9K
# Total Submissions: 1.4M
# Testcase Example:  '[10,2,5,3]'
#
# Given an array arr of integers, check if there exist two indices i and j such
# that :
# 
# 
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# 
# 
# Example 2:
# 
# 
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
# @lc code=end

def main():
    sol = Solution()

    # Example 1
    arr = [10,2,5,3]
    print(sol.checkIfExist(arr))
    # Output: true

    # Example 2
    arr = [3,1,7,11]
    print(sol.checkIfExist(arr))
    # Output: false
    
    return

if __name__ == "__main__":
    main()
