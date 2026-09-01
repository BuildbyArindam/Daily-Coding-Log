/**
 * Problem: Averages/Root Mean Square
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/averagesroot-mean-square
 * Date: 2026-09-01
 * Difficulty: Easy
 * Topics: Math, Array, Statistics
 *
 * Approach:
 * Compute the mean of the squares of all elements, then take the
 * square root of that mean. Uses Array.reduce to accumulate the
 * sum of squares in a single pass, then divides by array length
 * and applies Math.sqrt.
 *
 * Time Complexity: O(n) — single pass over the array via reduce
 * Space Complexity: O(1) — only a running accumulator is stored
 */


// ------------------------------- Solution ------------------------------


function rms(arr) {
  const sumOfSquares = arr.reduce((sum, num) => sum + num ** 2, 0);
  return Math.sqrt(sumOfSquares / arr.length);
}
