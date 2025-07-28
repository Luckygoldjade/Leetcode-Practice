#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find indices of the two numbers such that they add up to target.
        """
        # classic nested loop to check each pair. no early exit.
        # O(n^2) time complexity.
        outer_loop = 0
        inner_loop = 0
        for outer_loop in range(len(nums)):
            for inner_loop in range(outer_loop + 1, len(nums)):
                if nums[outer_loop] + nums[inner_loop] == target:
                    return [outer_loop, inner_loop]




        return [outer_loop, inner_loop]

# @lc code=end

# =======
# call functions from here



def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))
    return []

if __name__ == "__main__":
    main()
