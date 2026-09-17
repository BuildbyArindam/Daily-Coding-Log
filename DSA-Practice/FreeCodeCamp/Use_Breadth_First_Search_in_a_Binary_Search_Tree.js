/**
 * Problem: Use Breadth First Search in a Binary Search Tree
 * Platform: freeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/use-breadth-first-search-in-a-binary-search-tree
 * Date: 2026-09-17
 * Difficulty: Easy
 * Topics: Trees, Binary Search Tree, BFS, Queue
 *
 * Approach:
 * Implement level-order (BFS) and reverse level-order traversal on a BST
 * using an explicit queue. levelOrder() processes nodes left-to-right at
 * each depth by pushing left child before right child into the queue.
 * reverseLevelOrder() flips this by pushing right before left, so nodes
 * are dequeued level-by-level but right-to-left within each level.
 *
 * Time complexity: O(n) — every node is visited exactly once.
 * Space complexity: O(n) — worst case the queue holds an entire level,
 *                    which can be up to ~n/2 nodes in a balanced tree,
 *                    plus O(n) for the result array.
 */


// --------------------------------- Solution -----------------------------------------


var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}
function BinarySearchTree() {
  this.root = null;
  this.levelOrder = function() {
    if (this.root === null) {
      return null;
    }
    var queue = [this.root];
    var result = [];
    while (queue.length > 0) {
      var current = queue.shift();
      result.push(current.value);
      if (current.left !== null) {
        queue.push(current.left);
      }
      if (current.right !== null) {
        queue.push(current.right);
      }
    }
    return result;
  };
  this.reverseLevelOrder = function() {
    if (this.root === null) {
      return null;
    }
    var queue = [this.root];
    var result = [];
    while (queue.length > 0) {
      var current = queue.shift();
      result.push(current.value);
      if (current.right !== null) {
        queue.push(current.right);
      }
      if (current.left !== null) {
        queue.push(current.left);
      }
    }
    return result;
  };
}
