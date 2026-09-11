/*
 * Problem 03: Valid Anagram (LeetCode #242)
 * Topic: Arrays & Strings
 * Difficulty: Easy
 * Language: C
 */

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isAnagram(char* s, char* t) {
    int len_s = strlen(s);
    int len_t = strlen(t);
    if (len_s != len_t) return false;
    
    int count[26] = {0};
    for (int i = 0; i < len_s; i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) return false;
    }
    return true;
}

int main() {
    printf("Test 1: %s\n", isAnagram("anagram", "nagaram") ? "true" : "false"); // Expected: true
    printf("Test 2: %s\n", isAnagram("rat", "car") ? "true" : "false");         // Expected: false
    return 0;
}
