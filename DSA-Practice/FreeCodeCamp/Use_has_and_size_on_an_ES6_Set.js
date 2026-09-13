/**
 * Problem: Use .has and .size on an ES6 Set
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/use--has-and--size-on-an-es6-set
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: ES6, Sets, Data Structures
 *
 * Approach: Convert the input array into a Set (which auto-dedupes),
 * then use the built-in .has() to check membership of checkValue and
 * .size to get the count of unique elements. Return both as an array.
 *
 * Time Complexity: O(n) — building the Set from the array takes O(n);
 *                   .has() and .size are O(1) on a Set.
 * Space Complexity: O(n) — for storing unique elements in the Set.
 */


// -------------------------- Solution -----------------------------------------


function checkSet(arrToBeSet, checkValue){
   var set = new Set(arrToBeSet);
   var hasValue = set.has(checkValue);
   var setSize = set.size;
   return [hasValue, setSize];
}
