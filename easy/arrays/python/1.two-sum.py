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
        # --
        # classic nested loop to check each pair. no early exit.
        # O(n^2) time complexity.
        outer_loop = 0
        inner_loop = 0
        # for outer_loop in range(len(nums)):
        #     for inner_loop in range(outer_loop + 1, len(nums)):
        #         if nums[outer_loop] + nums[inner_loop] == target:
        #             return [outer_loop, inner_loop]

        # --
        # this is a classic problem that can be solved with a hashmap
        # there is one pair that adds up to target.
        # therefore, the loop exits when the pair is found.
        # since there is an early exit then a hashmap can be used
        # to store the indices of the numbers.
        hash_map = {}   # dictionary. key is the outer, value is the complement
        # Step 1: Build hashmap
        for inner_loop in range(len(nums)):
            hash_map[nums[inner_loop]] = inner_loop
        
        # print(hash_map)  # for debugging
        # print("hash_map:", hash_map)  # for debugging

        # Step 2: Check for each number if its complement exists in hashmap
        for outer_loop in range(len(nums)):
            complement = target - nums[outer_loop]
            # Step 2: Check if complement exists in hashmap
            # but not the same index
            # if the complement is in the hashmap, return the indices
            if complement in hash_map and hash_map[complement] != outer_loop:
                # print(f"Found: {nums[outer_loop]} + {complement} = {target}")
                # print(f"Indices: {outer_loop}, {hash_map[complement]}")
                # return the indices of the two numbers
                # the outer_loop is the index of the first number

                return [hash_map[complement], outer_loop]
        # if no pair is found, return an empty list
        return []
# @lc code=end

# ======= 
# call functions from here



def main():
    solution = Solution()
    
    # nums = [2, 7, 11, 15]
    # target = 9
    # print(solution.twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))


    return

if __name__ == "__main__":
    main()
