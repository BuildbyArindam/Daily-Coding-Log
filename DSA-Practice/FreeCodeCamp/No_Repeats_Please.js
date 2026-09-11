/**
 * Problem: No Repeats Please
 * Link: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please
 * Date: 2026-09-11
 * Difficulty: Medium
 * Topics: Backtracking, Permutations, Recursion, String Manipulation
 *
 * Approach:
 * Generate all permutations of the string via backtracking, skipping any
 * choice that would place the same character adjacent to the previous one.
 * Each time a full-length permutation is built without an adjacent repeat,
 * increment the count. The `used` array prevents reusing the same index
 * within one permutation path.
 *
 * Time Complexity: O(n! ) in the worst case (all unique chars → all
 * permutations get explored), though repeated-character pruning cuts this
 * down significantly in practice.
 * Space Complexity: O(n) for the recursion stack and the `used` array
 * (excluding the implicit O(n!) work done, no extra permutation storage).
 */


// ---------------------------- Solution ----------------------------------


function permAlone(str) {
  let count = 0;
  let used = new Array(str.length).fill(false);
  function generatePermutations(previousChar, length) {
    if (length === str.length) {
      count++;
      return;
    }
    for (let i = 0; i < str.length; i++) {
      if (!used[i] && str[i] !== previousChar) {
        used[i] = true;
        generatePermutations(str[i], length + 1);
        used[i] = false;
      }
    }
  }
  generatePermutations("", 0);
  return count;
}

permAlone('aab');
