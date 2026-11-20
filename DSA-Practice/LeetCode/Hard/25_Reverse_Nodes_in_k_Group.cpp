/**
 * Problem   : 25. Reverse Nodes in k-Group
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/reverse-nodes-in-k-group/
 * Date      : 2026-10-05
 * Difficulty: Hard
 * Topics    : Linked List, Recursion
 *
 * Approach  : Iterative, in-place group reversal using a dummy node.
 *             1. `prev` marks the node before the current group; `end` walks
 *                k nodes ahead to find the group's tail.
 *             2. If fewer than k nodes remain, stop (leave the remainder as is).
 *             3. Detach the group (end->next = nullptr), reverse it with a
 *                standard list reversal, and reconnect both ends.
 *             4. The old group head (`start`) becomes the new tail, so it
 *                becomes `prev` for the next iteration.
 *
 * Time      : O(n)  - each node is visited a constant number of times
 *                     (once to find the group end, once to reverse)
 * Space     : O(1)  - only pointers are used, no recursion or extra storage
 */


// -------------------------------------- Solution --------------------------------------------


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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* end = dummy;

        while (end != nullptr) {
            for (int i = 0; i < k && end != nullptr; ++i) {
                end = end->next;
            }
            if (end == nullptr) {
                break;
            }
            ListNode* start = prev->next;
            ListNode* next = end->next;
            end->next = nullptr;  // Disconnect the k-group
            prev->next = reverseList(start);  // Reverse the k-group
            start->next = next;  // Connect the reversed group to the rest
            prev = start;
            end = start;
        }
        return dummy->next;
    }

private:
    ListNode* reverseList(ListNode* head)
{
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};
