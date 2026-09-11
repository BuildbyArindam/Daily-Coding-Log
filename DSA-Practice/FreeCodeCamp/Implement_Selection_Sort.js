/**
 * Problem: Implement Selection Sort
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-selection-sort
 * Date: 2026-09-11
 * Difficulty: Easy
 * Topics: Arrays, Sorting
 *
 * Approach:
 * For each index i, scan the unsorted remainder of the array to find the
 * index of the minimum element (minIndex). If that minimum isn't already
 * at position i, swap it into place. Repeat until the array is fully sorted.
 *
 * Time Complexity: O(n^2) — nested loop, always scans remaining elements
 *                   regardless of input order (no early exit / best case).
 * Space Complexity: O(1) — sorts in place, only a few scalar variables used.
 */


// ------------------------------ Solution ---------------------------------


function selectionSort(array) {
  for (let i = 0; i < array.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < array[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      let temp = array[i];
      array[i] = array[minIndex];
      array[minIndex] = temp;
    }
  }
  return array;
}
