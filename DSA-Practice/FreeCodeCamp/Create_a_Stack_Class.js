/**
 * Problem: Create a Stack Class
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-stack-class
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Data Structures, Stack, Closures/Encapsulation, OOP (Constructor Functions)
 *
 * Approach:
 * Implement a Stack using a constructor function with a private `collection`
 * array captured via closure. Standard stack operations (push, pop, peek,
 * isEmpty, clear) are exposed as privileged methods that mutate/read the
 * closed-over array. push/pop delegate directly to native Array methods,
 * which already run in O(1) amortized time.
 *
 * Time Complexity:  O(1) for push, pop, peek, isEmpty, clear
 * Space Complexity: O(n) for storing n elements in the collection
 */


// -------------------------------- Solution -------------------------------------


function Stack() {
  var collection = [];
  this.print = function() {
    console.log(collection);
  };
  this.push = function(element) {
    collection.push(element);
  };

  this.pop = function() {
    return collection.pop();
  };
  this.peek = function() {
    return collection[collection.length - 1];
  };
  this.isEmpty = function() {
    return collection.length === 0;
  };
  this.clear = function() {
    collection = [];
  };
}
