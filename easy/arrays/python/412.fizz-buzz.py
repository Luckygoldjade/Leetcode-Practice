#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        Given an integer n, return a string array answer (1-indexed) where:
        answer[i] == "FizzBuzz" if i is divisible by 3 and 5
        """
        fizzbuzz_output = []
        bool_fizz = False
        bool_buzz = False
        string_fizz = "Fizz"
        string_buzz = "Buzz"
        string_fizzbuzz = "FizzBuzz"

        for ind in range(1, n + 1):
            bool_fizz = ind % 3 == 0
            bool_buzz = ind % 5 == 0

            if bool_fizz and bool_buzz:
                fizzbuzz_output.append(string_fizzbuzz)
            elif bool_fizz:
                fizzbuzz_output.append(string_fizz)
            elif bool_buzz:
                fizzbuzz_output.append(string_buzz)
            else:
                fizzbuzz_output.append(str(ind))

        return fizzbuzz_output


# @lc code=end

def main():
    solution = Solution()

    # Example 1:
    # Input: n = 3
    # Output: ["1","2","Fizz"]
    print(solution.fizzBuzz(3))  # Example usage, replace with actual test cases


    # Example 2:
    # Input: n = 5
    # Output: ["1","2","Fizz","4","Buzz"]
    print(solution.fizzBuzz(5))  # Example usage, replace with actual test cases


    # Example 3:
    # Input: n = 15
    # Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    print(solution.fizzBuzz(15))  # Example usage, replace with actual test cases

    return

if __name__ == "__main__":
    main()
