/**
 * Problem: Invert a Binary Tree
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/invert-a-binary-tree
 * Date: 2026-09-17
 * Difficulty: Easy
 * Topics: Trees, Binary Tree, Recursion, DFS
 *
 * Approach:
 * Recursively swap the left and right children of every node,
 * starting from the root and descending depth-first. Base case
 * is a null node, which returns null unchanged.
 *
 * Time Complexity: O(n) — visits every node exactly once
 * Space Complexity: O(h) — recursion call stack, where h is tree height
 *                    (O(log n) avg for balanced trees, O(n) worst case for skewed trees)
 */


// ---------------------------- Solution --------------------------------------------


var displayTree = (tree) => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.invert = function() {
    function invertNode(node) {
      if (node === null) {
        return null;
      }
      var temp = node.left;
      node.left = node.right;
      node.right = temp;
      invertNode(node.left);
      invertNode(node.right);
      return node;
    }
    this.root = invertNode(this.root);
    return this.root;
  };
}
