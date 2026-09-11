/**
 * Problem: Implement Quick Sort
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-quick-sort
 * Date: 2026-09-11
 * Difficulty: Medium
 * Topics: Sorting, Divide and Conquer, Recursion, Arrays
 *
 * Approach:
 * Classic divide-and-conquer quicksort using the first element as pivot.
 * Partition the remaining elements into `left` (< pivot) and `right` (>= pivot)
 * arrays, recursively sort each half, then concatenate left + pivot + right.
 * This is a non-in-place (auxiliary array) variant — simpler to reason about
 * than Lomuto/Hoare in-place partitioning, at the cost of extra space.
 *
 * Time Complexity: O(n log n) average, O(n^2) worst case (e.g. already-sorted
 *                   or reverse-sorted input with first-element pivot)
 * Space Complexity: O(n) — new arrays created at every recursive call
 *                   (plus O(log n) average call stack depth)
 */


// ----------------------------- Solution -------------------------------


function quickSort(array) {
  if (array.length <= 1) {
    return array;
  }
  const pivot = array[0];
  const left = [];
  const right = [];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < pivot) {
      left.push(array[i]);
    } else {
      right.push(array[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}
