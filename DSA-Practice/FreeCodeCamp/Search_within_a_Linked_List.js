/**
 * Problem: Search within a Linked List
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/search-within-a-linked-list
 * Date: 2026-09-13
 * Difficulty: Easy–Medium (linked list traversal fundamentals)
 * Topics: Linked List, Traversal, Data Structures
 *
 * Approach:
 * Custom singly linked list implementation with core operations:
 * - add(): append node at tail (O(n) walk to find tail)
 * - remove(): find node by value, splice it out
 * - indexOf(): linear search, return index or -1
 * - elementAt(): linear traversal to given index, return element or undefined
 *
 * Time Complexity:
 * - add: O(n)      (no tail pointer, walks list each time)
 * - remove: O(n)
 * - indexOf: O(n)
 * - elementAt: O(n)
 *
 * Space Complexity: O(1) extra space for all operations (O(n) for the list itself)
 */


// ----------------------------- Solution -------------------------------------


function LinkedList() {
  var length = 0;
  var head = null;
  var Node = function(element){
    this.element = element;
    this.next = null;
  };
  this.size = function() {
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
    var currentNode = head;
    var previousNode;
    if(currentNode.element === element){
      head = currentNode.next;
    } else {
      while(currentNode.element !== element) {
        previousNode = currentNode;
        currentNode = currentNode.next;
      }
      previousNode.next = currentNode.next;
    }
    length--;
  };
  this.isEmpty = function() {
    return length === 0;
  };
  this.indexOf = function(element) {
    var currentNode = head;
    var index = 0;
    while (currentNode) {
      if (currentNode.element === element) {
        return index;
      }
      currentNode = currentNode.next;
      index++;
    }
    return -1;
  };
  this.elementAt = function(index) {
    var currentNode = head;
    var currentIndex = 0;
    while (currentNode) {
      if (currentIndex === index) {
        return currentNode.element;
      }
      currentNode = currentNode.next;
      currentIndex++;
    }
    return undefined;
  };
}
