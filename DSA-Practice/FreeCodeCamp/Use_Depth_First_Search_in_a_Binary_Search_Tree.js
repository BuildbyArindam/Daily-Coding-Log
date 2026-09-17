/**
 * Problem: Use Depth First Search in a Binary Search Tree
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/use-depth-first-search-in-a-binary-search-tree
 * Date: 2026-09-17
 * Difficulty: Easy
 * Topics: Trees, Binary Search Tree, DFS, Recursion
 *
 * Approach:
 * Implemented three DFS traversal orders (inorder, preorder, postorder)
 * on a Binary Search Tree using recursive helper functions. Each traversal
 * builds a result array by visiting left/right subtrees in a different
 * sequence relative to the current node:
 *   - Inorder:   left -> node -> right
 *   - Preorder:  node -> left -> right
 *   - Postorder: left -> right -> node
 *
 * Time Complexity: O(n) per traversal — each node is visited exactly once
 * Space Complexity: O(n) for the result array, O(h) additional for the
 *                    recursion call stack (h = tree height)
 */


// ----------------------------------- Solution ----------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.inorder = function() {
    if (this.root === null) {
      return null;
    }
    var result = [];
    function traverse(node) {
      if (node === null) {
        return;
      }
      traverse(node.left);
      result.push(node.value);
      traverse(node.right);
    }
    traverse(this.root);
    return result;
  };
  this.preorder = function() {
    if (this.root === null) {
      return null;
    }
    var result = [];
    function traverse(node) {
      if (node === null) {
        return;
      }
      result.push(node.value);
      traverse(node.left);
      traverse(node.right);
    }
    traverse(this.root);
    return result;
  };
  this.postorder = function() {
    if (this.root === null) {
      return null;
    }
    var result = [];
    function traverse(node) {
      if (node === null) {
        return;
      }
      traverse(node.left);
      traverse(node.right);
      result.push(node.value);
    }
    traverse(this.root);
    return result;
  };
}
