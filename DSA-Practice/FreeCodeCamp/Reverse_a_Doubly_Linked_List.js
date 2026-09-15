/**
 * Problem: Reverse a Doubly Linked List
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/reverse-a-doubly-linked-list
 * Date: 2026-09-15
 * Difficulty: Easy-Medium
 * Topics: Linked List, Doubly Linked List, Pointer Manipulation
 *
 * Approach:
 * Walk the list once from head to tail. At each node, swap its `next`
 * and `prev` pointers (store `next` in a temp before overwriting).
 * After the loop, swap `head` and `tail` on the list itself.
 *
 * Time Complexity:  O(n) - single pass through all nodes
 * Space Complexity: O(1) - only a few pointer variables, no extra structures
 */


// ---------------------------- Solution ---------------------------------------


var Node = function(data, prev) {
  this.data = data;
  this.prev = prev;
  this.next = null;
};

var DoublyLinkedList = function() {
  this.head = null;
  this.tail = null;
  this.reverse = function() {
    if (this.head === null) {
      return null;
    }
    var current = this.head;
    while (current !== null) {
      var temp = current.next;
      current.next = current.prev;
      current.prev = temp;
      current = temp;
    }
    var temp = this.head;
    this.head = this.tail;
    this.tail = temp;
    return this;
  };
};
