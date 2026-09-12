/**
 * Problem: Create a Set Class
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-set-class
 * Date: 2026-09-12
 * Difficulty: Easy
 * Topics: Data Structures, Hash Tables (Object-based), Sets, OOP
 *
 * Approach:
 * Implement a Set ADT backed by a plain JS object (`dictionary`) used as a
 * hash map, with a `length` counter tracked manually. `has()` checks key
 * existence, `add()`/`remove()` guard against duplicates/missing elements
 * before mutating, and `values()` returns all stored elements via
 * Object.values().
 *
 * Time Complexity: O(1) average for has/add/remove/size (object key lookup);
 *                   O(n) for values() since it copies all n elements.
 * Space Complexity: O(n) to store n elements in the dictionary.
 */


// --------------------------- Solution --------------------------------------


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
}
