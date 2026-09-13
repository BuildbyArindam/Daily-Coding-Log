/**
 * Problem: Work with Nodes in a Linked List
 * Platform: FreeCodeCamp - Coding Interview Prep (Data Structures)
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/work-with-nodes-in-a-linked-list
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: Linked List, Data Structures
 *
 * Approach:
 * Defined a Node constructor with `element` and `next` properties.
 * Created individual Node instances and manually linked them together
 * via their `next` pointers to form a singly linked list structure
 * (Kitten -> Puppy -> Cat -> Dog).
 *
 * Time Complexity: O(1) - fixed number of node creations and pointer assignments
 * Space Complexity: O(n) - n nodes allocated, each storing a value and a reference
 */


// ---------------------------- Solution -----------------------------------------


var Node = function(element) {
  this.element = element;
  this.next = null;
};
var Kitten = new Node('Kitten');
var Puppy = new Node('Puppy');
Kitten.next = Puppy;
var Cat = new Node('Cat');
var Dog = new Node('Dog');
Puppy.next = Cat;
Cat.next = Dog;
