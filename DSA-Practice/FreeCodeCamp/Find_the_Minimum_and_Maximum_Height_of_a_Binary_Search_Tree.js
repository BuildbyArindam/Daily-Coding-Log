/*
 * Problem: Find the Minimum and Maximum Height of a Binary Search Tree
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/find-the-minimum-and-maximum-height-of-a-binary-search-tree
 * Date: 2026-09-16
 * Difficulty: Easy
 * Topics: Binary Search Tree (BST), Binary Trees, Recursion, Tree Traversal, Divide and Conquer, Tree Height/Depth, Balanced Trees
 *
 * Approach:
 * - Recursively calculate the minimum height by following the shorter
 *   root-to-leaf path.
 * - Recursively calculate the maximum height by following the longer
 *   root-to-leaf path.
 * - An empty tree has height -1 and a leaf has height 0.
 * - A tree is considered balanced when max height - min height <= 1.
 *
 * Time Complexity:
 * - findMinHeight: O(n) worst case
 * - findMaxHeight: O(n)
 * - isBalanced: O(n) overall, with the current implementation potentially
 *   traversing the tree twice.
 *
 * Space Complexity:
 * - O(h) auxiliary space due to recursion, where h is the tree height.
 */


// -------------------------------- Solution -------------------------------------------


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
      return this;
    }
    var current = this.root;
    while (true) {
      if (value < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return this;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = newNode;
          return this;
        }
        current = current.right;
      }
    }
  };
  this.findMinHeight = function(node) {
    if (node === undefined) {
      node = this.root;
    }
    if (node === null) {
      return -1;
    }
    if (node.left === null && node.right === null) {
      return 0;
    }
    if (node.left === null) {
      return 1 + this.findMinHeight(node.right);
    }
    if (node.right === null) {
      return 1 + this.findMinHeight(node.left);
    }
    return 1 + Math.min(
      this.findMinHeight(node.left),
      this.findMinHeight(node.right)
    );
  };
  this.findMaxHeight = function(node) {
    if (node === undefined) {
      node = this.root;
    }
    if (node === null) {
      return -1;
    }
    return 1 + Math.max(
      this.findMaxHeight(node.left),
      this.findMaxHeight(node.right)
    );
  };
  this.isBalanced = function() {
    return this.findMaxHeight() - this.findMinHeight() <= 1;
  };
}
