/**
 * Problem: Perform a Subset Check on Two Sets of Data
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/perform-a-subset-check-on-two-sets-of-data
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topics: Data Structures, Sets, Hashing/Hash Tables, Object-Oriented Design
 *
 * Approach:
 * Custom Set class backed by a hash map (object) for O(1) membership checks.
 * isSubsetOf() iterates over this set's values and checks that every one
 * exists in the target set, short-circuiting on the first miss via Array.every().
 *
 * Time Complexity:  O(n) — n = size of the current set (this.values().length),
 *                    each `.has()` lookup is O(1) average case.
 * Space Complexity: O(n) — for the array produced by `this.values()`.
 */


// ------------------------------ Solution ----------------------------------


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
      if (!set.dictionary[value]) {
        newSet.add(value);
      }
    });
    return newSet;
  }
  isSubsetOf(set) {
    return this.values().every(value => set.has(value));
  }
}
