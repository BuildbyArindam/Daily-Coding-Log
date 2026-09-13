/**
 * Problem: Remove Elements from a Linked List
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-elements-from-a-linked-list
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: Linked List, Pointer Manipulation
 *
 * Approach:
 * Implemented a singly linked list with add() and remove() methods.
 * remove() handles two cases: (1) target is the head node — reassign
 * head to head.next; (2) target is elsewhere — walk the list keeping
 * a reference to the node before the target, then splice it out by
 * pointing currentNode.next to currentNode.next.next.
 *
 * Time Complexity: O(n) — worst case traverses the full list to find the element
 * Space Complexity: O(1) — no extra data structures, only pointer reassignment
 */


// -------------------------- Solution -------------------------------------


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
  this.remove = function(element){
    if (head === null) {
      return;
    }
    if (head.element === element) {
      head = head.next;
      length--;
      return;
    }
    var currentNode = head;
    while (currentNode.next !== null) {
      if (currentNode.next.element === element) {
        currentNode.next = currentNode.next.next;
        length--;
        return;
      }
      currentNode = currentNode.next;
    }
  };
}
