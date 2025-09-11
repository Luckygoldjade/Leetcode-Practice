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
    def checkIfExist(self, arr: list[int]) -> bool:
        """
        nested loop approach but use a set to track seen numbers and one loop
        Time Complexity: O(n)
        Space Complexity: O(n)
        similar to using one pointer for read and set Not hashmap for seen numbers
        we are finding a pair that satisfies the condition
        one of the pair is arr[i] which is element in the input array.
        the other one of the pair is element in arr[j] which is the seen set.
        """
        # use a read pointer to traverse the array
        # use a set to track seen numbers
        # A set is a guest list: you check if a name is on it—simple yes/no.
        # A hashmap is a rolodex: each name has a card with extra details. Great if you need those details; overkill if you just need to know whether they’re in the building.
        seen = set()
        # no pre populate seen set. check first then add current number to seen set

        # step 1: compare each number to seen set
        # use a read pointer to traverse the array
        # compare each number to seen set
        for read_ptr in range(len(arr)):
            # all odd or even number then check for double in seen
            if arr[read_ptr] * 2 in seen:
                # step 2
                # always check first; if match, then add x
                seen.add(arr[read_ptr])
                print(f"seen: {seen}")
                return True
            # only even number then check for half in seen
            if arr[read_ptr] % 2 == 0 and arr[read_ptr] / 2 in seen:
                # step 2
                # always check first; if no match, then add x
                seen.add(arr[read_ptr])
                print(f"seen: {seen}")
                return True
            else:
                # add current number to seen set
                seen.add(arr[read_ptr])
                print(f"seen: {seen}")
        
        return False
    
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

    # Example 3
    arr = [0,-2,2]
    print(sol.checkIfExist(arr))
    # Output: False

    return

if __name__ == "__main__":
    main()
