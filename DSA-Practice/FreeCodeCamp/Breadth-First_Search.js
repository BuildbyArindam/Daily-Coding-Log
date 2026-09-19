/**
 * Problem: Breadth-First Search
 * Platform: FreeCodeCamp — Coding Interview Prep / Data Structures
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/breadth-first-search
 * Date: 2026-09-19
 * Difficulty: Easy-Medium
 * Topics: Graph Traversal / BFS / Queue / Adjacency Matrix
 *
 * Approach:
 * Standard BFS from `root` over a graph given as an adjacency matrix.
 * Track shortest edge-distance to every node in `nodesLen`, initialized
 * to Infinity (unvisited) except the root (0). Use a queue (array +
 * shift) to process nodes level by level; whenever an unvisited
 * neighbor is found (matrix cell === 1), set its distance to
 * currentDistance + 1 and enqueue it.
 *
 * Time complexity: O(V^2) — for each dequeued node we scan its full
 * row in the adjacency matrix (V neighbors), across V nodes.
 * (Would be O(V + E) with an adjacency list instead.)
 * Space complexity: O(V) — for `nodesLen` and the `queue`.
 */


// ---------------------------------- Solution -----------------------------------------


function bfs(graph, root) {
  var nodesLen = {};
  for (var i = 0; i < graph.length; i++) {
    nodesLen[i] = Infinity;
  }
  nodesLen[root] = 0;
  var queue = [root];
  while (queue.length > 0) {
    var currentNode = queue.shift();
    for (var i = 0; i < graph[currentNode].length; i++) {
      if (graph[currentNode][i] === 1) {
        if (nodesLen[i] === Infinity) {
          nodesLen[i] = nodesLen[currentNode] + 1;
          queue.push(i);
        }
      }
    }
  }
  return nodesLen;
};

var exBFSGraph = [
  [0, 1, 0, 0],
  [1, 0, 1, 0],
  [0, 1, 0, 1],
  [0, 0, 1, 0]
];

console.log(bfs(exBFSGraph, 3));
