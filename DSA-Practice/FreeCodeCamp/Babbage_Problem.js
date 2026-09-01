/**
 * Problem: Babbage Problem
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/babbage-problem
 * Date Solved: 2026-09-01
 * Difficulty: Easy
 * Topics: Math, Brute Force, Number Theory (Squares)
 *
 * Approach:
 * Brute-force search — increment n starting from 1 and check whether
 * n^2 mod 1,000,000 equals the given endDigits. Return the first n
 * that satisfies the condition (guaranteed to exist for valid input).
 *
 * Time Complexity: O(n) — n grows until the matching square is found
 *                  (n ≈ 25264 for the classic 269696 case)
 * Space Complexity: O(1) — only a single counter variable used
 */


// ------------------------- Solution ------------------------------


function babbage(babbageNum, endDigits) {
  let n = 1;
  while (true) {
    if ((n * n) % 1000000 === endDigits) {
      return n;
    }
    n++;
  }
}
