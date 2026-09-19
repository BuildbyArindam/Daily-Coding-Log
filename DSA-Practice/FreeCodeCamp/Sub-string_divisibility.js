/**
 * Project Euler #43 — Sub-string Divisibility
 * Link: https://www.freecodecamp.org/learn/project-euler/project-euler-problems-1-to-100/problem-43-sub-string-divisibility
 * Date: 2026-09-19
 * Difficulty: Medium
 * Topics: Backtracking, Permutations, Number Theory, Pruning
 *
 * Approach:
 * Backtracking / permutation generation over digits 0..n, building the number
 * digit-by-digit. At each position past index 2, the last 3 digits placed so
 * far are checked against the corresponding prime divisor (2,3,5,7,11,13,17)
 * for that substring position — pruning invalid branches early instead of
 * generating all permutations and filtering afterward.
 *
 * Time Complexity:  O(n!) worst case (permutation search space), but heavily
 *                    pruned in practice by the modulo checks at each step —
 *                    effectively much closer to O(k) where k = valid partial paths.
 * Space Complexity:  O(n) for the digits/used arrays + recursion stack depth O(n).
 */


// ----------------------------------- Solution --------------------------------------------


function substringDivisibility(n) {
  const divisors = [2, 3, 5, 7, 11, 13, 17];
  const digitCount = n + 1;
  const rules = n - 2;
  if (!Number.isInteger(n) || n < 2 || n > 9) {
    throw new Error("n must be an integer from 2 to 9");
  }
  const used = Array(n + 1).fill(false);
  const digits = Array(digitCount).fill(0);
  let sum = 0n;
  function backtrack(pos, value) {
    if (pos === digitCount) {
      sum += BigInt(value);
      return;
    }
    for (let digit = 0; digit <= n; digit++) {
      if (used[digit]) continue;
      digits[pos] = digit;
      used[digit] = true;
      let valid = true;
      const ruleIndex = pos - 3;
      if (ruleIndex >= 0 && ruleIndex < rules) {
        const threeDigitNumber =
          digits[pos - 2] * 100 +
          digits[pos - 1] * 10 +
          digits[pos];
        if (threeDigitNumber % divisors[ruleIndex] !== 0) {
          valid = false;
        }
      }
      if (valid) {
        backtrack(pos + 1, value * 10 + digit);
      }
      used[digit] = false;
    }
  }
  backtrack(0, 0);
  return Number(sum);
}

substringDivisibility(5);
