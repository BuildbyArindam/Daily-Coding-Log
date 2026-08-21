'''
Problem: Segregate Even And Odd Nodes In a Linked List
Platform: Coding Ninjas - Code360
Link: https://www.naukri.com/code360/problems/segregate-even-and-odd-nodes-in-a-linked-list_1116100
Difficulty: Easy
Topics: Linked List, Two-Pointer Technique, In-place Partitioning
Date: 2026-08-21

Approach:
Maintain two separate sub-lists (even and odd) built in-place while
traversing the original list once. Track head/tail pointers for each
sub-list to allow O(1) appends. Detach each node from the original
list before appending (current.next = None) to avoid cycles. After
traversal, link the tail of the even list to the head of the odd list.
Handles edge case where no even nodes exist (returns odd_head).

Time Complexity: O(n) - single pass through the list
Space Complexity: O(1) - only pointers used, nodes rearranged in-place
'''


# ---------------------------- Solution -----------------------------------


'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def segregateEvenOdd(head):
    # Write your code here
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = None
        if current.data % 2 == 0:
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        else:
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        current = next_node
    if even_head is None:
        return odd_head
    even_tail.next = odd_head
    return even_head
