/**
 * Problem: Depth-First Search (Graph Traversal)
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/depth-first-search
 * Date Solved: 2026-09-19
 * Difficulty: Easy-Medium
 * Topics: Graphs, Depth-First Search, Stack, Adjacency Matrix
 *
 * Approach:
 * Iterative DFS using an explicit stack instead of recursion.
 * Starting from `root`, push it onto the stack. While the stack isn't
 * empty, pop a node, mark it visited, and record it in the result.
 * Then scan its adjacency row in reverse order and push any unvisited
 * neighbor (graph[node][i] === 1) onto the stack, so traversal order
 * matches what a recursive DFS would produce.
 *
 * Time Complexity: O(V^2)  -- for each of V nodes, we scan its full
 *                             adjacency row of length V (matrix representation)
 * Space Complexity: O(V)   -- stack, visited array, and result array
 */


// ----------------------------------- Solution ------------------------------------------


function dfs(graph, root) {
  var stack = [root];
  var visited = [];
  var result = [];
  while (stack.length > 0) {
    var node = stack.pop();
    if (visited[node]) {
      continue;
    }
    visited[node] = true;
    result.push(node);
    for (var i = graph[node].length - 1; i >= 0; i--) {
      if (graph[node][i] === 1 && !visited[i]) {
        stack.push(i);
      }
    }
  }
  return result;
}

var exDFSGraph = [
  [0, 1, 0, 0],
  [1, 0, 1, 0],
  [0, 1, 0, 1],
  [0, 0, 1, 0]
];

console.log(dfs(exDFSGraph, 3));
