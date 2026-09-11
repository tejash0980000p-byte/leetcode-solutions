"""
Problem 04: Best Time to Buy and Sell Stock (LeetCode #121)
Topic: Arrays & Strings
Difficulty: Easy-Medium

Description:
You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock. Return the maximum profit 
you can achieve from this transaction.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print("Test 2:", sol.maxProfit([7, 6, 4, 3, 1]))     # Expected: 0
