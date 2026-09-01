/**
 * Problem: Balanced Brackets
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/balanced-brackets
 * Date: 2026-09-01
 * Difficulty: Easy
 * Topics: String Manipulation, Stack (Counter-based), Bracket Matching, Validation
 *
 * Approach:
 * Since only one bracket type ('[' and ']') is involved, a simple running
 * counter replaces the need for an actual stack. Increment on '[', decrement
 * on ']'. If the counter ever goes negative, a closing bracket appeared
 * before its matching opener, so the string is unbalanced. At the end, the
 * counter must be exactly 0 for all brackets to be matched.
 *
 * Time Complexity: O(n) — single pass through the string
 * Space Complexity: O(1) — only a counter variable is used
 */


// ---------------------------- Solution ------------------------------------


function isBalanced(str) {
  let count = 0;
  for (let char of str) {
    if (char === "[") {
      count++;
    } else if (char === "]") {
      count--;
      if (count < 0) {
        return false;
      }
    }
  }
  return count === 0;
}
