/**
 * Problem: Pairwise
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/pairwise
 * Date: 2026-09-11
 * Difficulty: Easy-Medium 
 * Topics: Arrays, Two Pointers, Hashing/Sets, Brute Force -> Optimization
 *
 * Approach:
 * Brute-force pairwise scan. For each index i, scan forward for a j such that
 * arr[i] + arr[j] === arg, skipping indices already used in a prior pair.
 * Once a pair is found, mark both indices used and add (i + j) to the running sum.
 *
 * Time Complexity: O(n^2) — nested loop over the array in the worst case
 * Space Complexity: O(n) — the `used` Set can hold up to n indices
 */


// -------------------------- Solution --------------------------------------


function pairwise(arr, arg) {
  let sum = 0;
  let used = new Set();
  for (let i = 0; i < arr.length; i++) {
    if (used.has(i)) continue;
    for (let j = i + 1; j < arr.length; j++) {
      if (used.has(j)) continue;
      if (arr[i] + arr[j] === arg) {
        sum += i + j;
        used.add(i);
        used.add(j);
        break;
      }
    }
  }
  return sum;
}

pairwise([1, 4, 2, 3, 0, 5], 7);
