/**
 * Problem: Perform an Intersection on Two Sets of Data
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/perform-an-intersection-on-two-sets-of-data
 * Date: 2026-09-12
 * Difficulty: Easy–Medium
 * Topics: Data Structures, Sets, Hash Tables
 *
 * Approach:
 * Implement a Set class backed by a plain object (hash map) for O(1) average
 * membership checks. `intersection(set)` iterates over this set's values and
 * keeps only the ones also present in the other set, using `has()` for lookup.
 *
 * Time Complexity:
 *   - add/has/remove: O(1) average
 *   - union: O(n + m)
 *   - intersection: O(n + m) — O(n) to iterate this set's values, each `has()`
 *     check O(1) average, plus O(m) implicit cost of `values()` on the other set
 * Space Complexity: O(n + m) — new Set created to hold the result
 */


// -------------------------------- Solution -----------------------------------


class Set {
  constructor() {
    this.dictionary = {};
    this.length = 0;
  }
  has(element) {
    return this.dictionary[element] !== undefined;
  }
  values() {
    return Object.keys(this.dictionary);
  }
  add(element) {
    if (!this.has(element)) {
      this.dictionary[element] = true;
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
  union(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      newSet.add(value);
    });
    set.values().forEach(value => {
      newSet.add(value);
    });
    return newSet;
  }
  intersection(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      if (set.has(value)) {
        newSet.add(value);
      }
    });
    return newSet;
  }
}
