/**
 * Problem: Implement Merge Sort
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-merge-sort
 * Date: 2026-09-11
 * Difficulty: Medium
 * Topics: Divide and Conquer, Recursion, Sorting Algorithms, Arrays
 *
 * Approach:
 * Classic divide-and-conquer merge sort. Recursively split the array in half
 * until subarrays have length <= 1, then merge sorted halves back together
 * by comparing front elements of each half and pushing the smaller one.
 *
 * Time Complexity: O(n log n) — log n levels of splitting, O(n) work to merge at each level
 * Space Complexity: O(n) — new arrays created at each merge/slice step (not in-place)
 */


// --------------------------- Solution -----------------------------------


function mergeSort(array) {
  if (array.length <= 1) {
    return array;
  }
  const middle = Math.floor(array.length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);
  const sortedLeft = mergeSort(left);
  const sortedRight = mergeSort(right);
  const result = [];
  let i = 0;
  let j = 0;
  while (i < sortedLeft.length && j < sortedRight.length) {
    if (sortedLeft[i] <= sortedRight[j]) {
      result.push(sortedLeft[i]);
      i++;
    } else {
      result.push(sortedRight[j]);
      j++;
    }
  }
  while (i < sortedLeft.length) {
    result.push(sortedLeft[i]);
    i++;
  }
  while (j < sortedRight.length) {
    result.push(sortedRight[j]);
    j++;
  }
  return result;
}
