/**
 * Problem: Find the Symmetric Difference
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference
 * Date: 2026-09-11
 * Difficulty: Easy
 * Topics: Arrays, Sets, Hash Tables
 *
 * Approach:
 * Reduce over all input arrays, computing the pairwise symmetric
 * difference between the running result and the next array. For each
 * pair, build a Set of each array and filter out elements present in
 * the other, then concatenate the two filtered lists. Dedupe with a
 * Set and sort numerically at the end.
 *
 * Time Complexity: O(n * m) where n = number of arrays, m = avg array length
 *                  (each pairwise diff is O(len(arr1) + len(arr2)))
 * Space Complexity: O(m) for the Sets and intermediate result arrays
 */


// -------------------------- Solution ---------------------------------


function sym(args) {
  const arrays = Array.from(arguments);
  let result = [...new Set(arrays[0])];
  function difference(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    return [
      ...arr1.filter(value => !set2.has(value)),
      ...arr2.filter(value => !set1.has(value))
    ];
  }
  for (let i = 1; i < arrays.length; i++) {
    result = difference(result, [...new Set(arrays[i])]);
  }
  return [...new Set(result)].sort((a, b) => a - b);
}
sym([1, 2, 3], [5, 2, 1, 4]);
