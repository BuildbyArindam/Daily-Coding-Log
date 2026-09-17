/**
 * Problem: Delete a Leaf Node in a Binary Search Tree
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-leaf-node-in-a-binary-search-tree
 * Date: 2026-09-17
 * Difficulty: Easy
 * Topics: Trees, Binary Search Tree
 *
 * Approach:
 * Iteratively search for the node with the target value while tracking
 * its parent. Once found, check if it's a leaf (no children). If it's
 * the root with no children, clear the root; otherwise detach it from
 * whichever side (left/right) of the parent it hangs off of.
 *
 * Time Complexity: O(h) — h = height of tree (O(log n) avg, O(n) worst case for skewed tree)
 * Space Complexity: O(1) — iterative, no extra structures
 */


// ---------------------------------- Solution ---------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.remove = function(value) {
    if (this.root === null) {
      return null;
    }
    var parent = null;
    var current = this.root;
    while (current !== null && current.value !== value) {
      parent = current;
      if (value < current.value) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    if (current === null) {
      return null;
    }
    var children = 0;
    if (current.left !== null) {
      children++;
    }
    if (current.right !== null) {
      children++;
    }
    if (children === 0) {
      if (parent === null) {
        this.root = null;
      }
      else if (parent.left === current) {
        parent.left = null;
      }
      else {
        parent.right = null;
      }
    }
    return current;
  };
}
