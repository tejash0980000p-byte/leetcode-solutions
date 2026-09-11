"""
Problem 02: Reverse String (LeetCode #344)
Topic: Arrays & Strings
Difficulty: Easy

Description:
Write a function that reverses a string. The input string is given as an array 
of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print("Test 1:", s1)  # Expected: ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    print("Test 2:", s2)  # Expected: ["h", "a", "n", "n", "a", "H"]
