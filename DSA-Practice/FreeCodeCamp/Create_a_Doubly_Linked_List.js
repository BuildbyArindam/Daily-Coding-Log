/**
 * Problem: Create a Doubly Linked List
 * Platform: FreeCodeCamp (Coding Interview Prep — Data Structures)
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-doubly-linked-list
 * Date: 2026-09-15
 * Difficulty: Easy
 * Topics: Data Structures, Linked List, Doubly Linked List, Pointer Manipulation
 *
 * Approach:
 * Standard doubly linked list with head/tail pointers.
 * - add(data): appends a new node at the tail, linking prev/next in O(1).
 * - remove(data): scans from head, and when a matching node is found,
 *   unlinks it by rewiring prev.next / next.prev (and updates head/tail
 *   if the removed node was at either end). Continues scanning after a
 *   match, so it removes ALL nodes with that data, not just the first.
 *
 * Complexity:
 * - add:    Time O(1),  Space O(1)
 * - remove: Time O(n) — always walks the full list (even after a match)
 *           Space O(1)
 */


// ---------------------------- Solution ----------------------------------------


var Node = function(data, prev) {
  this.data = data;
  this.prev = prev;
  this.next = null;
};

var DoublyLinkedList = function() {
  this.head = null;
  this.tail = null;
  this.add = function(data) {
    var newNode;
    if (this.head === null) {
      newNode = new Node(data, null);
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode = new Node(data, this.tail);
      this.tail.next = newNode;
      this.tail = newNode;
    }
  };
  this.remove = function(data) {
    if (this.head === null) {
      return null;
    }
    var current = this.head;
    while (current !== null) {
      if (current.data === data) {
        if (current === this.head) {
          this.head = current.next;
          if (this.head !== null) {
            this.head.prev = null;
          }
        } else {
          current.prev.next = current.next;
        }
        if (current === this.tail) {
          this.tail = current.prev;
          if (this.tail !== null) {
            this.tail.next = null;
          }
        } else {
          current.next.prev = current.prev;
        }
      }
      current = current.next;
    }
    return null;
  };
};
