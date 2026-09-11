"""
Problem 07: Move Zeroes (LeetCode #283 / Bubble Sort Variant)
Topic: Basic Algorithms
Difficulty: Easy-Medium

Description:
Given an integer array `nums`, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements. You must do this in-place without making 
a copy of the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1

if __name__ == "__main__":
    sol = Solution()
    arr1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(arr1)
    print("Test 1:", arr1)  # Expected: [1, 3, 12, 0, 0]

    arr2 = [0]
    sol.moveZeroes(arr2)
    print("Test 2:", arr2)  # Expected: [0]
