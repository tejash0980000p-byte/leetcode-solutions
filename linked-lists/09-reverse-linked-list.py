"""
Problem 09 (Bonus): Reverse Linked List (LeetCode #206)
Topic: Linked Lists
Difficulty: Easy-Medium

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals

if __name__ == "__main__":
    sol = Solution()
    head1 = create_linked_list([1, 2, 3, 4, 5])
    rev1 = sol.reverseList(head1)
    print("Test 1:", print_linked_list(rev1))  # Expected: [5, 4, 3, 2, 1]

    head2 = create_linked_list([1, 2])
    rev2 = sol.reverseList(head2)
    print("Test 2:", print_linked_list(rev2))  # Expected: [2, 1]
