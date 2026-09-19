/**
 * Problem: Adjacency List
 * Platform: freeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/adjacency-list
 * Date: 2026-09-19
 * Difficulty: Easy
 * Topics: Graphs, Data Structures, Hash Maps
 *
 * Approach:
 * Represent an undirected graph using a plain JS object as an adjacency
 * list. Each key is a vertex (person), and its value is an array of
 * neighboring vertices it shares an edge with. Since the graph is
 * undirected, each edge is stored symmetrically — e.g. James-Jeff appears
 * in both James's and Jeff's neighbor lists.
 *
 * Time Complexity:  O(1) to build (fixed, hardcoded structure);
 *                    O(1) average for a lookup of any vertex's neighbors.
 * Space Complexity: O(V + E) — one entry per vertex, one array slot per
 *                    edge endpoint (each undirected edge counted twice).
 */


// ---------------------------------------- Solution -------------------------------------


var undirectedAdjList = {
  James: ["Jeff"],
  Jill: ["Jenny"],
  Jenny: ["Jill", "Jeff"],
  Jeff: ["James", "Jenny"]
};
