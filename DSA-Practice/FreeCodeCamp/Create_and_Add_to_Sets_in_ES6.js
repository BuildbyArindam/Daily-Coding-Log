/**
 * Problem: Create and Add to Sets in ES6
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-and-add-to-sets-in-es6
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: JavaScript ES6, Data Structures, Sets, Deduplication
 *
 * Approach:
 * Use the ES6 Set object to store unique values. Sets automatically discard
 * duplicate entries on insertion, so initializing with a repeated array and
 * then calling .add() for new values naturally results in a deduplicated
 * collection. Array.from() converts the Set back to an array for logging.
 *
 * Time Complexity: O(n) - each insertion/lookup in a Set is O(1) amortized,
 *                   over n initial elements + m added elements
 * Space Complexity: O(k) - where k is the number of unique elements stored
 */


// ---------------------------- Solution ---------------------------------------


function checkSet() {
  var set = new Set([1, 2, 3, 3, 2, 1, 2, 3, 1]);
  set.add('Taco');
  set.add('Cat');
  set.add('Awesome');
  console.log(Array.from(set));
  return set;
}
checkSet();
