"""
Problem 03: Valid Anagram (LeetCode #242)
Topic: Arrays & Strings
Difficulty: Easy

Description:
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

Time Complexity: O(n)
Space Complexity: O(1) -- bounded by 26 lowercase English letters
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
            
        return True

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isAnagram("anagram", "nagaram"))  # Expected: True
    print("Test 2:", sol.isAnagram("rat", "car"))          # Expected: False
