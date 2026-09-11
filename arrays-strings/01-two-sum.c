/*
 * Problem 01: Two Sum (LeetCode #1)
 * Topic: Arrays & Strings
 * Difficulty: Easy
 * Language: C
 */

#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 0;
    
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    return result;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int* res = twoSum(nums, 4, target, &returnSize);
    
    if (returnSize == 2) {
        printf("Test 1: [%d, %d]\n", res[0], res[1]); // Expected: [0, 1]
    }
    free(res);
    return 0;
}
