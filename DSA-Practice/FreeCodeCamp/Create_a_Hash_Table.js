/**
 * Problem: Create a Hash Table
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-a-hash-table
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topics: Hash Tables, Hashing Functions, Collision Handling (Separate Chaining)
 *
 * Approach:
 * - Custom hash() sums char codes of the key string to produce a bucket index.
 * - Each bucket in `collection` is an array of [key, value] pairs (separate chaining)
 *   to handle collisions when two different keys hash to the same value.
 * - add(): hashes key, creates bucket if needed, updates value if key exists,
 *   otherwise pushes new [key, value] pair.
 * - lookup(): hashes key, linear-scans bucket for matching key.
 * - remove(): hashes key, linear-scans bucket, splices out match, deletes
 *   empty bucket to avoid leaving stale empty arrays.
 *
 * Time Complexity:
 * - hash(): O(m) where m = key string length
 * - add() / lookup() / remove(): O(m + k) average, where k = number of keys
 *   in the colliding bucket (O(1) average with a well-distributed hash,
 *   worst case O(m + n) if all keys collide into one bucket)
 *
 * Space Complexity: O(n) where n = number of key-value pairs stored
 */


// ---------------------------- Solution ---------------------------------


var called = 0;
var hash = string => {
  called++;
  var hashed = 0;
  for (var i = 0; i < string.length; i++) {
    hashed += string.charCodeAt(i);
  }
  return hashed;
};
var HashTable = function() {
  this.collection = {};
  this.add = function(key, value) {
    var hashedKey = hash(key);
    if (!this.collection[hashedKey]) {
      this.collection[hashedKey] = [];
    }
    for (var i = 0; i < this.collection[hashedKey].length; i++) {
      if (this.collection[hashedKey][i][0] === key) {
        this.collection[hashedKey][i][1] = value;
        return;
      }
    }
    this.collection[hashedKey].push([key, value]);
  };
  this.lookup = function(key) {
    var hashedKey = hash(key);
    if (!this.collection[hashedKey]) {
      return null;
    }
    for (var i = 0; i < this.collection[hashedKey].length; i++) {
      if (this.collection[hashedKey][i][0] === key) {
        return this.collection[hashedKey][i][1];
      }
    }
    return null;
  };
  this.remove = function(key) {
    var hashedKey = hash(key);
    if (!this.collection[hashedKey]) {
      return;
    }
    for (var i = 0; i < this.collection[hashedKey].length; i++) {
      if (this.collection[hashedKey][i][0] === key) {
        this.collection[hashedKey].splice(i, 1);
        if (this.collection[hashedKey].length === 0) {
          delete this.collection[hashedKey];
        }
        return;
      }
    }
  };
};
