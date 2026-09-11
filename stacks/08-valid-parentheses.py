"""
Problem 08: Valid Parentheses (LeetCode #20)
Topic: Stacks
Difficulty: Easy-Medium

Description:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isValid("()"))        # Expected: True
    print("Test 2:", sol.isValid("()[]{}"))    # Expected: True
    print("Test 3:", sol.isValid("(]"))        # Expected: False
    print("Test 4:", sol.isValid("([)]"))      # Expected: False
    print("Test 5:", sol.isValid("{[]}"))      # Expected: True
