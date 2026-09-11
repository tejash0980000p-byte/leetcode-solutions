"""
Problem 05: Longest Common Prefix (LeetCode #14)
Topic: Arrays & Strings
Difficulty: Easy-Medium

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Time Complexity: O(S) where S is the total number of characters in all strings
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: "fl"
    print("Test 2:", sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Expected: ""
