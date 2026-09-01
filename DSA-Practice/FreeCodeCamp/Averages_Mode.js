/**
 * Problem: Averages/Mode
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/averagesmode
 * Date: 2026-09-01
 * Difficulty: Easy
 * Topics: Arrays, Hashing, Frequency Counting
 *
 * Approach:
 * Single pass to build a frequency map (`counts`) while tracking the
 * running maxCount. Second pass collects every value whose frequency
 * equals maxCount, using `modes.includes()` to avoid duplicate entries
 * (handles multi-modal arrays correctly).
 *
 * Time Complexity: O(n) — two linear passes over the array
 * Space Complexity: O(n) — frequency map + modes array in the worst case
 */


// ---------------------------------- Solution --------------------------------


function mode(arr) {
  const counts = {};
  let maxCount = 0;
  for (const value of arr) {
    counts[value] = (counts[value] || 0) + 1;
    maxCount = Math.max(maxCount, counts[value]);
  }
  const modes = [];
  for (const value of arr) {
    if (counts[value] === maxCount && !modes.includes(value)) {
      modes.push(value);
    }
  }
  return modes;
}
