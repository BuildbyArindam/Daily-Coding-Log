/**
 * Problem: Add a New Element to a Binary Search Tree
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/add-a-new-element-to-a-binary-search-tree
 * Date: 2026-09-15
 * Difficulty: Easy–Medium 
 * Topics: Trees, Binary Search Trees, Recursion vs. Iteration, Data Structures
 *
 * Approach:
 * Iterative insertion into a BST. Starting from the root, compare the
 * new value against the current node — move left if smaller, right if
 * larger, until an empty spot is found. Duplicate values are ignored
 * (no insertion, returns null).
 *
 * Time Complexity: O(h), where h = height of the tree
 *   - O(log n) average case (balanced tree)
 *   - O(n) worst case (skewed/unbalanced tree)
 * Space Complexity: O(1) — iterative, no recursion stack used
 */


// ---------------------------- Solution ------------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.add = function(value) {
    if (this.root === null) {
      this.root = new Node(value);
      return;
    }
    var current = this.root;
    while (true) {
      if (value === current.value) {
        return null;
      }
      if (value < current.value) {
        if (current.left === null) {
          current.left = new Node(value);
          return;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = new Node(value);
          return;
        }
        current = current.right;
      }
    }
  };
}
