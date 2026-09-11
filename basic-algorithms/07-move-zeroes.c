/*
 * Problem 07: Move Zeroes (LeetCode #283 / Bubble Sort Variant)
 * Topic: Basic Algorithms
 * Difficulty: Easy-Medium
 * Language: C
 */

#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    int last_non_zero = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) {
            int temp = nums[last_non_zero];
            nums[last_non_zero] = nums[i];
            nums[i] = temp;
            last_non_zero++;
        }
    }
}

int main() {
    int nums[] = {0, 1, 0, 3, 12};
    moveZeroes(nums, 5);
    printf("Test 1: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n"); // Expected: 1 3 12 0 0
    return 0;
}
