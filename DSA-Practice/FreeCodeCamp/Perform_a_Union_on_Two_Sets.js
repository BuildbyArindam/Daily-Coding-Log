/**
 * Problem: Perform a Union on Two Sets
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/perform-a-union-on-two-sets
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Data Structures, Sets, Hash Maps
 *
 * Approach:
 * Implement a Set class backed by a plain object (dictionary) for O(1)
 * membership checks. union(otherSet) creates a new Set, then adds every
 * element from `this` and `otherSet` into it — duplicates are naturally
 * skipped because add() checks has() before inserting.
 *
 * Time Complexity: O(n + m) — n = this.length, m = otherSet.length
 * Space Complexity: O(n + m) — worst case, no overlap between the two sets
 */


// ------------------------------ Solution -----------------------------------


class Set {
  constructor() {
    this.dictionary = {};
    this.length = 0;
  }
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  values() {
    return Object.values(this.dictionary);
  }
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = element;
      this.length++;
      return true;
    }
    return false;
  }
  remove(element) {
    if (this.has(element)) {
      delete this.dictionary[element];
      this.length--;
      return true;
    }
    return false;
  }
  size() {
    return this.length;
  }
  union(otherSet) {
    const unionSet = new Set();
    this.values().forEach(element => unionSet.add(element));
    otherSet.values().forEach(element => unionSet.add(element));
    return unionSet;
  }
}
