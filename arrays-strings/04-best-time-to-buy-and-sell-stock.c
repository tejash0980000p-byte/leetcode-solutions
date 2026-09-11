/*
 * Problem 04: Best Time to Buy and Sell Stock (LeetCode #121)
 * Topic: Arrays & Strings
 * Difficulty: Easy-Medium
 * Language: C
 */

#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize <= 1) return 0;
    
    int min_price = prices[0];
    int max_profit = 0;
    
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < min_price) {
            min_price = prices[i];
        } else if (prices[i] - min_price > max_profit) {
            max_profit = prices[i] - min_price;
        }
    }
    return max_profit;
}

int main() {
    int prices1[] = {7, 1, 5, 3, 6, 4};
    printf("Test 1: %d\n", maxProfit(prices1, 6)); // Expected: 5

    int prices2[] = {7, 6, 4, 3, 1};
    printf("Test 2: %d\n", maxProfit(prices2, 5)); // Expected: 0
    return 0;
}
