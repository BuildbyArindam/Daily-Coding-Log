/**
 * Problem: Delete a Node with One Child in a Binary Search Tree
 * Platform: freeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-node-with-one-child-in-a-binary-search-tree
 * Date: 2026-09-17
 * Difficulty: Medium
 * Topics: Binary Search Tree, Recursion, Tree Deletion
 *
 * Approach:
 * Recursively search for the target node by comparing values, tracking
 * its parent along the way. Once found, count its children:
 *   - 0 children: unlink it directly from the parent (or clear root).
 *   - 1 child: splice the child up to take the target's place in the
 *     parent (or set it as the new root).
 * (2-children case is not handled here — this version targets the
 * 0/1-child scenarios.)
 *
 * Time Complexity: O(h) — h = height of tree, one root-to-node traversal
 * Space Complexity: O(h) — recursion call stack depth
 */


// ----------------------------------- Solution -----------------------------------------------


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
    var target = null;
    var parent = null;
    (function findValue(node = this.root) {
      if (value == node.value) {
        target = node;
      } else if (value < node.value && node.left !== null) {
        parent = node;
        return findValue(node.left);
      } else if (value > node.value && node.right !== null) {
        parent = node;
        return findValue(node.right);
      } else {
        return null;
      }
    }.bind(this)());
    if (target === null) {
      return null;
    }
    var children =
      (target.left !== null ? 1 : 0) +
      (target.right !== null ? 1 : 0);
    if (children === 0) {
      if (target == this.root) {
        this.root = null;
      } else {
        if (parent.left == target) {
          parent.left = null;
        } else {
          parent.right = null;
        }
      }
    }
    if (children === 1) {
      var child = target.left !== null ? target.left : target.right;
      if (target == this.root) {
        this.root = child;
      } else {
        if (parent.left == target) {
          parent.left = child;
        } else {
          parent.right = child;
        }
      }
    }
  };
}
