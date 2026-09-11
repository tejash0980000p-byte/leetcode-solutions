"""
Problem 01: Two Sum (LeetCode #1)
Topic: Arrays & Strings
Difficulty: Easy

Description:
Given an array of integers `nums` and an integer `target`, return indices of the 
two numbers such that they add up to `target`.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print("Test 2:", sol.twoSum([3, 2, 4], 6))        # Expected: [1, 2]
    print("Test 3:", sol.twoSum([3, 3], 6))           # Expected: [0, 1]
