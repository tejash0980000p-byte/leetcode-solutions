/*
 * Problem 08: Valid Parentheses (LeetCode #20)
 * Topic: Stacks
 * Difficulty: Easy-Medium
 * Language: C
 */

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isValid(char* s) {
    int len = strlen(s);
    char* stack = (char*)malloc(len);
    int top = -1;
    
    for (int i = 0; i < len; i++) {
        char ch = s[i];
        if (ch == '(' || ch == '{' || ch == '[') {
            stack[++top] = ch;
        } else {
            if (top == -1) {
                free(stack);
                return false;
            }
            char topChar = stack[top--];
            if ((ch == ')' && topChar != '(') ||
                (ch == '}' && topChar != '{') ||
                (ch == ']' && topChar != '[')) {
                free(stack);
                return false;
            }
        }
    }
    bool result = (top == -1);
    free(stack);
    return result;
}

int main() {
    printf("Test 1: %s\n", isValid("()") ? "true" : "false");     // Expected: true
    printf("Test 2: %s\n", isValid("()[]{}") ? "true" : "false"); // Expected: true
    printf("Test 3: %s\n", isValid("(]") ? "true" : "false");     // Expected: false
    return 0;
}
