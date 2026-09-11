/*
 * Problem 02: Reverse String (LeetCode #344)
 * Topic: Arrays & Strings
 * Difficulty: Easy
 * Language: C
 */

#include <stdio.h>

void reverseString(char* s, int sSize) {
    int left = 0;
    int right = sSize - 1;
    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}

int main() {
    char str[] = {'h', 'e', 'l', 'l', 'o'};
    reverseString(str, 5);
    printf("Test 1: ");
    for (int i = 0; i < 5; i++) {
        printf("%c ", str[i]);
    }
    printf("\n"); // Expected: o l l e h
    return 0;
}
