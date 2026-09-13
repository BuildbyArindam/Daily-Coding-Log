/**
 * Problem: Create a Map Data Structure
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-map-data-structure
 * Platform: FreeCodeCamp
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: Data Structures, Hash Map / Object-based Storage, OOP (Constructor Functions)
 *
 * Approach:
 * Implement a Map ADT backed by a plain JS object as the underlying
 * hash table. Each method (add, remove, get, has, values, clear, size)
 * delegates to native object operations (property assignment, delete,
 * hasOwnProperty, Object.values/keys) to get near O(1) key access.
 *
 * Time Complexity:
 *   add()    - O(1) avg
 *   remove() - O(1) avg
 *   get()    - O(1) avg
 *   has()    - O(1) avg
 *   values() - O(n)
 *   clear()  - O(1)
 *   size()   - O(n)  (Object.keys builds an array of all keys)
 *
 * Space Complexity: O(n) for storing n key-value pairs in `collection`
 */


// ---------------------------- Solution ------------------------------------


var Map = function() {
  this.collection = {};
  this.add = function(key, value) {
    this.collection[key] = value;
  };
  this.remove = function(key) {
    delete this.collection[key];
  };
  this.get = function(key) {
    return this.collection[key];
  };
  this.has = function(key) {
    return this.collection.hasOwnProperty(key);
  };
  this.values = function() {
    return Object.values(this.collection);
  };
  this.clear = function() {
    this.collection = {};
  };
  this.size = function() {
    return Object.keys(this.collection).length;
  };
};
