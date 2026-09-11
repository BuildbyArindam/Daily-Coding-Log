/**
 * Problem: Implement Bubble Sort
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-bubble-sort
 * Date: 2026-09-11
 * Difficulty: Easy
 * Topics: Sorting, Arrays, Comparison-based Sort
 *
 * Approach:
 * Standard bubble sort with adjacent-element comparison and swap.
 * Includes an optimization: a `swapped` flag breaks out early if a full
 * pass makes no swaps, meaning the array is already sorted.
 *
 * Time Complexity: O(n^2) worst/average case, O(n) best case (already sorted, due to early exit)
 * Space Complexity: O(1) - sorts in place, no extra data structures
 */


// --------------------------- Solution ---------------------------------


function bubbleSort(array) {
  for (let i = 0; i < array.length - 1; i++) {
    let swapped = false;
    for (let j = 0; j < array.length - 1 - i; j++) {
      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return array;
}
