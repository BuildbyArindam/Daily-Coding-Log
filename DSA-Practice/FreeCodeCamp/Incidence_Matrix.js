/**
 * Problem: Incidence Matrix
 * Platform: freeCodeCamp — Coding Interview Prep / Data Structures
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/incidence-matrix
 * Date: 2026-09-19
 * Difficulty: Easy
 * Topics: Graphs, Matrix Representation, Data Structures
 *
 * Approach:
 * Represent a graph using an incidence matrix — rows correspond to edges,
 * columns correspond to vertices. Each cell is 1 if the vertex is an
 * endpoint of that edge, 0 otherwise. For an undirected graph, an edge
 * touches exactly two vertices, so each row sums to 2 (except self-loops).
 *
 * Time Complexity: O(1) — static declaration, no traversal/construction logic
 * Space Complexity: O(E * V) — E rows (edges) by V columns (vertices)
 */


// -------------------------------------- Solution ---------------------------------------------------


var incMatUndirected = [
  [1, 0, 0, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 0],
  [0, 0, 0, 1],
  [0, 0, 1, 0]
];
