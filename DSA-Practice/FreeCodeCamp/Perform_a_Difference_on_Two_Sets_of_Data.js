/**
 * Problem: Perform a Difference on Two Sets of Data
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/perform-a-difference-on-two-sets-of-data
 * Date: 2026-09-12
 * Difficulty: Medium
 * Topics: Data Structures, Hash Maps, Sets, Set Operations
 *
 * Approach:
 * Implemented a Set data structure backed by a plain object (hash map) for
 * O(1) membership checks. difference(set) walks this set's values and keeps
 * only the ones NOT present in the other set, using has() for lookup.
 * union() and intersection() are implemented alongside it for completeness.
 *
 * Time Complexity:  O(n + m) — n = this.size(), m = set.size()
 *                   (iterate this set once, each has() check is O(1))
 * Space Complexity: O(n) — worst case newSet holds all of this set's values
 */


// -------------------------------- Solution ------------------------------------------


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
    let largeSet;
    let smallSet;
    if (this.dictionary.length > set.length) {
      largeSet = this;
      smallSet = set;
    } else {
      largeSet = set;
      smallSet = this;
    }
    smallSet.values().forEach(value => {
      if (largeSet.dictionary[value]) {
        newSet.add(value);
      }
    });
    return newSet;
  }
  difference(set) {
    const newSet = new Set();
    this.values().forEach(value => {
      if (!set.has(value)) {
        newSet.add(value);
      }
    });
    return newSet;
  }
}
