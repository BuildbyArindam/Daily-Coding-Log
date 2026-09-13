/**
 * Problem: Create an ES6 JavaScript Map
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/create-an-es6-javascript-map
 * Date: 2026-09-13
 * Difficulty: Easy
 * Topics: ES6, Data Structures, Map
 *
 * Approach:
 * Instantiate a new ES6 Map object and use the .set() method to add
 * a key-value pair to it. Map preserves insertion order and allows
 * keys of any type (unlike plain objects, which coerce keys to strings).
 *
 * Time Complexity: O(1) — Map.set() is a constant-time operation
 * Space Complexity: O(1) — single key-value pair stored
 */


// --------------------------- Solution -----------------------------------


let myMap = new Map();
myMap.set("freeCodeCamp", "Awesome!");
