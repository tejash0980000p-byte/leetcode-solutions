/*
 * Problem 09 (Bonus): Reverse Linked List (LeetCode #206)
 * Topic: Linked Lists
 * Difficulty: Easy-Medium
 * Language: C
 */

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    while (curr != NULL) {
        struct ListNode* nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

struct ListNode* createNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

int main() {
    struct ListNode* head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    
    struct ListNode* rev = reverseList(head);
    printf("Test 1: ");
    struct ListNode* curr = rev;
    while (curr) {
        printf("%d ", curr->val);
        curr = curr->next;
    }
    printf("\n"); // Expected: 3 2 1
    return 0;
}
