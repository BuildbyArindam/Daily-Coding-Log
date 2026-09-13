/**
 * Problem: Remove Items from a Set in ES6
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-items-from-a-set-in-es6
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: Data Structures, Sets (ES6), JavaScript Fundamentals
 *
 * Approach:
 * Create a Set from an array of numbers, then use the built-in
 * Set.prototype.delete() method to remove specific elements (2 and 5).
 * Sets store unique values and delete() removes an element by value
 * in-place, returning true/false depending on whether it existed.
 *
 * Time Complexity: O(1) per delete() call (average case, hash-based)
 * Space Complexity: O(n) for storing the Set of n elements
 */


// ------------------------------ Solution ------------------------------------


function checkSet(){
  var set = new Set([1, 2, 3, 4, 5]);
  set.delete(2);
  set.delete(5);
  return set;   
}
