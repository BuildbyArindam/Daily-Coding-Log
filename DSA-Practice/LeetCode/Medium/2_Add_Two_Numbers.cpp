/*
 * Problem:    2. Add Two Numbers
 * Platform:   LeetCode 
 * Link:       https://leetcode.com/problems/add-two-numbers/
 * Date:       2026-10-04
 * Difficulty: Medium
 * Topics:     Linked List, Math, Recursion
 *
 * Approach:
 *   Digits are stored in reverse order, so the heads are the least
 *   significant digits and we can add column by column, like
 *   grade-school addition. Walk both lists together, summing
 *   l1->val + l2->val + carry. Append (sum % 10) as a new node and
 *   carry forward (sum / 10). A dummy head avoids special-casing the
 *   first node. The loop continues while either list has nodes OR a
 *   carry remains, which handles unequal lengths and a final carry
 *   (e.g. 99 + 1 = 100).
 *
 * Time:  O(max(m, n))  - one pass over the longer list
 * Space: O(max(m, n))  - result list (O(1) extra beyond the output)
 */


// ------------------------------------------ Solution ------------------------------------------------


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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0); 
        ListNode* current = dummyHead;        
        int carry = 0;               
        while (l1 || l2 || carry) {          
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = sum / 10;                
            current->next = new ListNode(sum % 10); 
            current = current->next;         
            l1 = l1 ? l1->next : l1; 
            l2 = l2 ? l2->next : l2;       
        }
        return dummyHead->next;  
    }
};
