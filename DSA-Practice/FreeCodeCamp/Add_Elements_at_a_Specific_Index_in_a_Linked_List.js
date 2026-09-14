/**
 * Problem: Add Elements at a Specific Index in a Linked List
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/add-elements-at-a-specific-index-in-a-linked-list
 * Date: 2026-09-14
 * Platform: FreeCodeCamp
 * Difficulty: Easy-Medium
 * Topics: Linked List, Data Structures, Pointer Manipulation
 *
 * Approach:
 * Implemented a singly linked list with an `addAt(index, element)` method.
 * - Validates index bounds (0 to length inclusive).
 * - Special-cases insertion at head (index 0).
 * - Otherwise walks the list to the node just before the target index
 *   and relinks pointers to insert the new node.
 *
 * Time Complexity: O(n) — worst case traverses the list to reach the index
 * Space Complexity: O(1) — only one new node is allocated, no extra structures
 */


// ------------------------------- Solution --------------------------------------


function LinkedList() {
  var length = 0;
  var head = null;
  var Node = function(element) {
    this.element = element;
    this.next = null;
  };
  this.size = function() {
    return length;
  };
  this.head = function() {
    return head;
  };
  this.add = function(element) {
    var node = new Node(element);
    if (head === null) {
      head = node;
    } else {
      var currentNode = head;
      while (currentNode.next) {
        currentNode = currentNode.next;
      }
      currentNode.next = node;
    }
    length++;
  };
  this.addAt = function(index, element) {
    if (index < 0 || index > length) {
      return false;
    }
    var node = new Node(element);
    if (index === 0) {
      node.next = head;
      head = node;
      length++;
      return true;
    }
    var currentNode = head;
    var currentIndex = 0;
    while (currentIndex < index - 1) {
      currentNode = currentNode.next;
      currentIndex++;
    }
    node.next = currentNode.next;
    currentNode.next = node;
    length++;
    return true;
  };
}
