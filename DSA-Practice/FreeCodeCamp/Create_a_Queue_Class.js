/**
 * Problem: Create a Queue Class
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-queue-class
 * Platform: FreeCodeCamp
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Data Structures, Queue, Closures/OOP
 *
 * Approach:
 * Implement a Queue using a constructor function with a private array
 * (via closure) as the underlying collection. Standard FIFO operations
 * are exposed as public methods: enqueue (push to back), dequeue
 * (shift from front), front (peek), size, isEmpty, and print.
 *
 * Time Complexity:
 *   enqueue: O(1)
 *   dequeue: O(n) — Array.shift() re-indexes the remaining elements
 *   front, size, isEmpty: O(1)
 * Space Complexity: O(n) — n elements stored in the collection array
 */


// -------------------------- Solution ----------------------------------


function Queue() {
  var collection = [];
  this.print = function() {
    console.log(collection);
  };
  this.enqueue = function(element) {
    collection.push(element);
  };
  this.dequeue = function() {
    return collection.shift();
  };
  this.front = function() {
    return collection[0];
  };
  this.size = function() {
    return collection.length;
  };
  this.isEmpty = function() {
    return collection.length === 0;
  };
}
