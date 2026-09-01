/**
 * Problem: Averages/Pythagorean means
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/averagespythagorean-means
 * Date: 2026-09-01
 * Difficulty: Easy
 * Topics: Math, Arrays, Array.reduce(), Statistics (AM-GM-HM inequality)
 *
 * Approach:
 * Compute the three Pythagorean means over the input array using reduce():
 *   - Arithmetic mean = sum(values) / n
 *   - Geometric mean  = (product(values))^(1/n)
 *   - Harmonic mean   = n / sum(1/value)
 * Then verify the AM-GM-HM inequality (A >= G >= H) holds, which is
 * guaranteed for any set of positive real numbers.
 *
 * Time complexity:  O(n) — three linear passes over the array
 * Space complexity: O(1) — only scalar accumulators used
 */


// --------------------------- Solution ----------------------------------


function pythagoreanMeans(rangeArr) {
  const n = rangeArr.length;
  const arithmetic =
    rangeArr.reduce((sum, value) => sum + value, 0) / n;
  const product =
    rangeArr.reduce((prod, value) => prod * value, 1);
  const geometric = Math.pow(product, 1 / n);
  const reciprocalSum =
    rangeArr.reduce((sum, value) => sum + 1 / value, 0);
  const harmonic = n / reciprocalSum;
  return {
    values: {
      Arithmetic: arithmetic,
      Geometric: geometric,
      Harmonic: harmonic
    },
    test: `is A >= G >= H ? ${arithmetic >= geometric && geometric >= harmonic ? "yes" : "no"}`
  };
}
