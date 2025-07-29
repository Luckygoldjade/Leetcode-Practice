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

        # there is one pair that adds up to target.
        # therefore, the loop exits when the pair is found.
        # since there is an early exit then a hashmap can be used
        # to store the indices of the numbers.
        hash_map = {}
        for outer_loop in range(len(nums)):
            complement = target - nums[outer_loop]
            # store the index of the number in the hash_map
            hash_map[nums[outer_loop]] = outer_loop

            # check if the complement is in the hash_map
            if complement in hash_map:
                return [hash_map[complement], outer_loop]
        # if no pair is found, return an empty list
        return []



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
