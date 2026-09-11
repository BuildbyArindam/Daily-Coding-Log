/**
 * Problem: Implement Binary Search
 * Platform: FreeCodeCamp
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/implement-binary-search
 * Date: 2026-09-11
 * Difficulty: Easy
 * Topics: Binary Search, Divide and Conquer, Arrays
 *
 * Approach:
 * Standard iterative binary search on a sorted array. Maintain a min/max
 * pointer range, check the middle element each iteration, and narrow the
 * range based on comparison with the target. Also tracks the path of
 * middle values checked (arrayPath) for visibility into the search steps.
 *
 * Time Complexity: O(log n) — search space halves each iteration
 * Space Complexity: O(log n) — arrayPath grows with number of iterations
 *                    (would be O(1) if only returning a boolean/index)
 */


// ----------------------------- Solution ------------------------------------


function binarySearch(searchList, value) {
  let arrayPath = [];
  let min = 0;
  let max = searchList.length - 1;
  while (min <= max) {
    let middle = Math.floor((min + max) / 2);
    let middleValue = searchList[middle];
    arrayPath.push(middleValue);
    if (middleValue === value) {
      return arrayPath;
    } else if (middleValue < value) {
      min = middle + 1;
    } else {
      max = middle - 1;
    }
  }
  return "Value Not Found";
}
