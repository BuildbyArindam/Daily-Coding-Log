/**
 * Problem: Implement Insertion Sort
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-insertion-sort
 * Date: 2026-09-11
 * Difficulty: Easy
 * Topics: Sorting, Arrays
 *
 * Approach:
 * Standard insertion sort — build the sorted portion of the array one
 * element at a time. For each element starting at index 1, shift it
 * leftward past all larger elements in the already-sorted prefix
 * until it lands in its correct position.
 *
 * Time Complexity: O(n^2) worst/average case (nearly sorted input drops to O(n))
 * Space Complexity: O(1) — sorts in place
 */


// ------------------------- Solution --------------------------------


function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    let current = array[i];
    let j = i - 1;
    while (j >= 0 && array[j] > current) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = current;
  }
  return array;
}
