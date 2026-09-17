/**
 * Problem: Delete a Node with Two Children in a Binary Search Tree
 * Platform: FreeCodeCamp — Coding Interview Prep / Data Structures
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-node-with-two-children-in-a-binary-search-tree
 * Date: 2026-09-17
 * Difficulty: Medium 
 * Topics: Data Structures, Trees, Binary Search Trees, Recursion, Node Deletion / Successor-based Removal
 *
 * Approach:
 * Standard BST deletion. First locate the target node and track its parent
 * via recursive search. Based on child count:
 *   - 0 children: unlink node from parent (or clear root).
 *   - 1 child: splice the single child up into the node's position.
 *   - 2 children: find the in-order successor (leftmost node in the right
 *     subtree), copy its value into the target node, then remove the
 *     successor node from its original position (it has at most a right child).
 *
 * Time Complexity:  O(h) — h = tree height. O(log n) average (balanced),
 *                    O(n) worst case (skewed tree).
 * Space Complexity: O(h) auxiliary — recursion stack from the findValue
 *                    search; deletion itself is O(1) extra space.
 */


// ------------------------------- Solution ------------------------------------


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
      } else if (value < node.value && node.left === null) {
        return null;
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
    else if (children === 1) {
      var newChild =
        target.left !== null ? target.left : target.right;
      if (parent === null) {
        this.root = newChild;
      } else if (parent.left == target) {
        parent.left = newChild;
      } else {
        parent.right = newChild;
      }
      target = null;
    }
    else {
      var successorParent = target;
      var successor = target.right;
      while (successor.left !== null) {
        successorParent = successor;
        successor = successor.left;
      }
      target.value = successor.value;
      if (successorParent.left === successor) {
        successorParent.left = successor.right;
      } else {
        successorParent.right = successor.right;
      }
      successor = null;
    }
  };
}
