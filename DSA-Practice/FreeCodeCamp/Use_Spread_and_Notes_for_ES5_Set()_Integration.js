/**
 * Problem: Use Spread and Notes for ES5 Set() Integration
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/use-spread-and-notes-for-es5-set-integration
 * Date Solved: 2026-09-13
 * Difficulty: Easy
 * Topics: Data Structures, Sets, ES6 Spread Operator, Arrays
 *
 * Approach:
 * Use the ES6 spread operator (...) to unpack all elements of a Set
 * into a new array. Since Set only stores unique values, spreading it
 * into an array is a quick way to deduplicate a collection while
 * converting it back to a standard array structure.
 *
 * Time Complexity: O(n) — spreading iterates through all n elements once
 * Space Complexity: O(n) — a new array of size n is created
 */


// ------------------------------ Solution -----------------------------------


function checkSet(set){
   return [...set];
}
