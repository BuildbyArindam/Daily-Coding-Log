/*
 * Problem   : 92. Reverse Linked List II
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/reverse-linked-list-ii/
 * Difficulty: Medium
 * Topics    : Linked List
 * Date      : 2026-10-07
 *
 * Approach  : In-place head insertion with a dummy node.
 *   1. Use a dummy node so left == 1 needs no special case.
 *   2. Move `prev` to the node just before position `left`.
 *   3. Let `current` be the first node of the sublist; it stays fixed and
 *      ends up as the tail of the reversed segment.
 *   4. Repeat (right - left) times: take current->next and move it to the
 *      front of the sublist (right after `prev`).
 *
 * Time      : O(n) - one pass to reach `left`, then (right - left) relinks
 * Space     : O(1) - only pointer variables
 */


// ---------------------------------- Solution ---------------------------------------------


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        
        for (int i = 0; i < left - 1; ++i) {
            prev = prev->next;
        }
        
        ListNode* current = prev->next;
        
        for (int i = 0; i < right - left; ++i) {
            ListNode* next_node = current->next;
            current->next = next_node->next;
            next_node->next = prev->next;
            prev->next = next_node;
        }
        
        return dummy.next;
    }
};
