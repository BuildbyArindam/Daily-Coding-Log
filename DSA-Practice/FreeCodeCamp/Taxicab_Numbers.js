/**
 * Problem: Taxicab Numbers
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/rosetta-code-taxicab-numbers
 * Date: 2026-09-05
 * Difficulty: Medium
 * Topics: Number Theory, Brute Force, Hashing/Map, Search Space Expansion
 *
 * Approach:
 *   A "taxicab number" is expressible as a^3 + b^3 in more than one way.
 *   For a growing search limit L, compute every sum a^3 + b^3 for 1 <= a < b <= L,
 *   tracking sums seen once (Map) vs. sums seen a second time (Set = confirmed
 *   taxicab numbers). If fewer than n taxicab numbers are found, double L and
 *   redo the search (cheap since numbers are small until n grows large).
 *   Finally sort the found set and return the first n.
 *
 * Time complexity:  O(L^2) per pass, where L doubles on each retry, so total
 *                   work is dominated by the final pass -> O(L_final^2).
 * Space complexity: O(L^2) for the sums Map/Set at the final limit.
 */


// --------------------------- Solution --------------------------------


function taxicabNumbers(n) {
  const found = new Set();
  let limit = 12;
  while (found.size < n) {
    const sums = new Map();
    for (let a = 1; a <= limit; a++) {
      for (let b = a + 1; b <= limit; b++) {
        const sum = a ** 3 + b ** 3;
        if (!sums.has(sum)) {
          sums.set(sum, 1);
        } else {
          found.add(sum);
        }
      }
    }
    limit *= 2;
  }
  return [...found].sort((a, b) => a - b).slice(0, n);
}
