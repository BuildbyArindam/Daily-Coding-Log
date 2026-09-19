/**
 * Problem: Adjacency Matrix
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/adjacency-matrix
 * Date: 2026-09-19
 * Difficulty: Easy
 * Topics: Graphs, Arrays, Data Structures
 *
 * Approach:
 * Represent an undirected graph with 5 vertices as a 2D adjacency matrix.
 * matrix[i][j] = 1 indicates an edge between vertex i and vertex j.
 * Since the graph is undirected, the matrix is symmetric (matrix[i][j] === matrix[j][i]).
 * A 0 diagonal indicates no self-loops.
 *
 * Time Complexity:  O(1) for edge lookup (matrix[i][j]) | O(V^2) for space/traversal setup
 * Space Complexity: O(V^2) — matrix size grows with the square of vertex count,
 *                    which is inefficient for sparse graphs (use adjacency list instead)
 */


// -------------------------------- Solution -------------------------------------


var adjMatUndirected = [
  [0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [0, 0, 1, 1, 0]
];
