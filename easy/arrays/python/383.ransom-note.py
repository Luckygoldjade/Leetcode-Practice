#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (64.70%)
# Likes:    5453
# Dislikes: 532
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        two loops. one for each character in ransomNote, and one for each character in magazine.
        once a letter match is found in magazine to letter in ransomNote, it is removed from magazine and the search exits. So, use hashmap for magazine.
        """
        # convert magazine to hashmap. build a frequency map (“hashmap”) of characters in a string
        magazine_count = {}     # magazine is string
        # dot get() is clean built-in dict patterns (no extra import)
        for ch in magazine:
            magazine_count[ch] = magazine_count.get(ch, 0) + 1
            print(f"magazine_count: {magazine_count}")  # debug

        # check
        # if length of ransomNote is greater than length of magazine, it cannot be constructed
        if len(ransomNote) > len(magazine):
            return False

        # check if ransomNote can be constructed from magazine
        for ch in ransomNote:
            if magazine_count.get(ch, 0) == 0:
                return False
            magazine_count[ch] -= 1

        return True

# @lc code=end

# # alternate for loop method to create hashmap
#         for char in magazine: 
#             if char in magazine_count: 
#                 magazine_count[char] += 1
#             else: 
#                 magazine_count[char] = 1

def main():
    # Example 1
    ransomNote = "a"
    magazine = "b"
    # Output: false
    s = Solution()
    print(s.canConstruct(ransomNote, magazine))


    # Example 2:
    ransomNote = "aa"
    magazine = "ab"
    # Output: false
    s = Solution()
    print(s.canConstruct(ransomNote, magazine))


    # Example 3:
    ransomNote = "aa"
    magazine = "aab"
    # Output: true
    s = Solution()
    print(s.canConstruct(ransomNote, magazine))


    return

if __name__ == "__main__":
    main()
