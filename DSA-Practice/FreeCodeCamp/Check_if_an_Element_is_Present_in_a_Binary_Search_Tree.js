/**
 * Problem: Check if an Element is Present in a Binary Search Tree
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/check-if-an-element-is-present-in-a-binary-search-tree
 * Date: 2026-09-15
 * Difficulty: Easy
 * Topics: Binary Search Tree, Trees, Search Algorithms
 *
 * Approach:
 * Build a standard BST with an `add` method that inserts nodes by comparing
 * values (smaller -> left, else -> right). `isPresent` walks down from the
 * root iteratively, moving left or right based on comparison with the
 * current node, until it finds the target value or hits a null child.
 *
 * Time Complexity: O(h) where h = tree height — O(log n) average (balanced),
 *                   O(n) worst case (skewed tree)
 * Space Complexity: O(1) — iterative traversal, no extra structures
 */


// ---------------------------- Solution ---------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.add = function(value) {
    var newNode = new Node(value);

    if (this.root === null) {
      this.root = newNode;
      return;
    }
    var current = this.root;
    while (true) {
      if (value < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = newNode;
          return;
        }
        current = current.right;
      }
    }
  };
  this.isPresent = function(value) {
    var current = this.root;
    while (current !== null) {
      if (current.value === value) {
        return true;
      }
      if (value < current.value) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    return false;
  };
}
