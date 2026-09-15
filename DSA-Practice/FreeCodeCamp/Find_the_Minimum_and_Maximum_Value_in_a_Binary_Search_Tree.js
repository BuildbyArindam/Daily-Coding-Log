/**
 * Problem: Find the Minimum and Maximum Value in a Binary Search Tree
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/find-the-minimum-and-maximum-value-in-a-binary-search-tree
 * Date: 2026-09-15
 * Difficulty: Easy
 * Topics: Binary Search Tree, Tree Traversal
 *
 * Approach:
 * Leverage the BST invariant (left < node < right). To find the minimum,
 * walk left from the root until there's no left child. To find the maximum,
 * walk right from the root until there's no right child. No recursion or
 * extra storage needed — just an iterative pointer walk down one side.
 *
 * Time Complexity:  O(h) — h = height of tree (O(log n) balanced, O(n) worst case skewed)
 * Space Complexity: O(1) — iterative, no extra structures
 */


// --------------------------- Solution -----------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.findMin = function() {
    if (this.root === null) {
      return null;
    }
    var current = this.root;
    while (current.left !== null) {
      current = current.left;
    }
    return current.value;
  };
  this.findMax = function() {
    if (this.root === null) {
      return null;
    }
    var current = this.root;
    while (current.right !== null) {
      current = current.right;
    }
    return current.value;
  };
}
