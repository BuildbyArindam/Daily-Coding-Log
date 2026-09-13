/**
 * Problem: Create a Linked List Class
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-linked-list-class
 * Date: 2026-09-13
 * Difficulty: Easy-Medium
 * Topics: Data Structures, Linked Lists, OOP (Closures)
 *
 * Approach:
 * Implemented a singly linked list using a constructor function with
 * private state (head, length) captured via closure. The Node is an
 * inner constructor holding `element` and a `next` pointer. `add()`
 * walks from head to the last node (O(n)) and appends a new node,
 * incrementing length. `head()` and `size()` are simple accessors.
 *
 * Time Complexity:
 *   - add(): O(n) — must traverse to the tail each time (no tail pointer)
 *   - head(): O(1)
 *   - size(): O(1)
 * Space Complexity: O(n) — one Node object per element stored
 *
 * Possible improvement: maintain a `tail` reference to make add() O(1).
 */


// ---------------------------- Solution -------------------------------------


function LinkedList() {
  var length = 0;
  var head = null;
  var Node = function(element){
    this.element = element;
    this.next = null;
  };
  this.head = function(){
    return head;
  };
  this.size = function(){
    return length;
  };
  this.add = function(element){
    var node = new Node(element);
    if (head === null) {
      head = node;
    } else {
      var current = head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = node;
    }
    length++;
  };
}
