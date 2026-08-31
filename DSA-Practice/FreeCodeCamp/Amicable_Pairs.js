/**
 * Problem: Amicable Pairs
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/amicable-pairs
 * Date: 2026-08-31
 * Difficulty: Easy-Medium
 * Topics: Number Theory, Divisor Sums, Sieve-style Precomputation, Math
 *
 * Approach:
 * Precompute the sum of proper divisors for every number up to maxNum
 * using a sieve: for each divisor d, add d to every multiple of d
 * greater than d itself (O(n log n) total, instead of O(n * sqrt(n))
 * from checking divisors individually per number).
 * Then scan n from 2..maxNum, let m = divisorSums[n]; if m > n,
 * m <= maxNum, and divisorSums[m] === n, (n, m) is an amicable pair.
 *
 * Time Complexity: O(n log n) — harmonic sum from the sieve loop
 * Space Complexity: O(n) — the divisorSums array
 */


// ---------------------------------- Solution -------------------------------------------


function amicablePairsUpTo(maxNum) {
  const divisorSums = new Array(maxNum + 1).fill(0);
  for (let divisor = 1; divisor <= Math.floor(maxNum / 2); divisor++) {
    for (let multiple = divisor * 2; multiple <= maxNum; multiple += divisor) {
      divisorSums[multiple] += divisor;
    }
  }
  const pairs = [];
  for (let n = 2; n <= maxNum; n++) {
    const m = divisorSums[n];
    if (
      m > n &&
      m <= maxNum &&
      divisorSums[m] === n
    ) {
      pairs.push([n, m]);
    }
  }
  return pairs;
}
