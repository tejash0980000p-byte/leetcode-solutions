"""
Problem 06: Binary Search (LeetCode #704)
Topic: Basic Algorithms
Difficulty: Easy-Medium

Description:
Given an array of integers `nums` which is sorted in ascending order, and an integer 
`target`, write a function to search `target` in `nums`. If `target` exists, then return 
its index. Otherwise, return -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.search([-1, 0, 3, 5, 9, 12], 9))  # Expected: 4
    print("Test 2:", sol.search([-1, 0, 3, 5, 9, 12], 2))  # Expected: -1
