/**
 * Problem: Remove Elements from a Linked List by Index
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-elements-from-a-linked-list-by-index
 * Date: 2026-09-14
 * Difficulty: Easy
 * Topics: Linked List, Data Structures, Pointers
 *
 * Approach:
 * Implemented a singly linked list with add() and removeAt(index).
 * removeAt() walks the list with a currentNode/previousNode pair until
 * currentIndex reaches the target index, then relinks previousNode.next
 * to skip the removed node. Head removal (index 0) is handled as a
 * special case by simply reassigning head.
 *
 * Time Complexity: O(n) — worst case traverses the full list to reach the index
 * Space Complexity: O(1) — no extra data structures, just pointer reassignment
 */


// ----------------------------- Solution ------------------------------------------


function LinkedList() {
  var length = 0;
  var head = null;
  var Node = function(element){
    this.element = element;
    this.next = null;
  };
  this.size = function(){
    return length;
  };
  this.head = function(){
    return head;
  };
  this.add = function(element){
    var node = new Node(element);
    if(head === null){
      head = node;
    } else {
      var currentNode = head;
      while(currentNode.next){
        currentNode = currentNode.next;
      }
      currentNode.next = node;
    }
    length++;
  };
  this.removeAt = function(index) {
    if (index < 0 || index >= length) {
      return null;
    }
    var currentNode = head;
    var previousNode = null;
    var currentIndex = 0;
    if (index === 0) {
      head = currentNode.next;
      length--;
      return currentNode.element;
    }
    while (currentIndex < index) {
      previousNode = currentNode;
      currentNode = currentNode.next;
      currentIndex++;
    }
    previousNode.next = currentNode.next;
    length--;
    return currentNode.element;
  };
}
