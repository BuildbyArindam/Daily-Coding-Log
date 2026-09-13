/**
 * Problem: Topological Sort
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/topological-sort
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topics: Graphs, Topological Sort, Kahn's Algorithm (BFS-based), Queue, Dependency Resolution
 *
 * Approach:
 * Parse each line into a library and its dependencies, building an adjacency
 * map (dependencies) and a reverse map (dependents). Any dependency not seen
 * as a key is added with an empty dependency list. Using Kahn's algorithm,
 * start with all libraries having zero dependencies, repeatedly remove one,
 * add it to the result, and decrement the dependency count of its dependents,
 * pushing any that reach zero onto the queue.
 *
 * Time complexity: O(V + E) — each library and each dependency edge is
 * processed a constant number of times.
 * Space complexity: O(V + E) — for the dependencies map, dependents map,
 * and queue/result arrays.
 */


// -------------------------- Solution -------------------------------------


function topologicalSort(libs) {
  const dependencies = new Map();
  libs
    .split(/\r?\n/)
    .forEach(line => {
      const parts = line.trim().split(/\s+/);
      if (!parts[0]) return;
      const library = parts[0];
      const deps = parts
        .slice(1)
        .filter(dep => dep !== library);
      dependencies.set(library, deps);
    });
  for (const deps of dependencies.values()) {
    for (const dep of deps) {
      if (!dependencies.has(dep)) {
        dependencies.set(dep, []);
      }
    }
  }
  const dependents = new Map();
  for (const library of dependencies.keys()) {
    dependents.set(library, []);
    for (const [otherLibrary, deps] of dependencies) {
      if (deps.includes(library)) {
        dependents.get(library).push(otherLibrary);
      }
    }
  }
  const queue = [...dependencies.keys()]
    .filter(library => dependencies.get(library).length === 0);
  const result = [];
  while (queue.length > 0) {
    const current = queue.pop();
    result.push(current);
    for (const next of dependents.get(current)) {
      const remaining = dependencies.get(next)
        .filter(dep => dep !== current);
      dependencies.set(next, remaining);
      if (remaining.length === 0) {
        queue.push(next);
      }
    }
  }
  return result;
}
