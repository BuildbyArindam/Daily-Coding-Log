/**
 * Problem: Check if Tree is Binary Search Tree
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/check-if-tree-is-binary-search-tree
 * Date: 2026-09-15
 * Difficulty: Medium 
 * Topics: Trees, Binary Search Trees, Recursion, Depth-First Search (DFS)
 * Approach: Recursive DFS with a shrinking valid range (min, max) passed down
 *           to each node. A node is valid only if it falls within the range
 *           inherited from its ancestors; the range is then tightened for
 *           each child (left child's max becomes parent.value - 1, right
 *           child's min becomes parent.value).
 * Time Complexity: O(n) — every node visited once
 * Space Complexity: O(h) — recursion stack, h = tree height
 *                    (O(log n) balanced, O(n) worst-case skewed tree)
 * Note: uses node.value - 1 for the upper bound, which assumes integer,
 *       distinct node values — won't hold for floats or duplicate values.
 */


// ---------------------------- Solution ---------------------------------------------


var displayTree = (tree) => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
}
function isBinarySearchTree(tree) {
  function check(node, min, max) {
    if (node === null) {
      return true;
    }
    if (node.value < min || node.value > max) {
      return false;
    }
    return (
      check(node.left, min, node.value - 1) &&
      check(node.right, node.value, max)
    );
  }
  return check(tree.root, -Infinity, Infinity);
}
