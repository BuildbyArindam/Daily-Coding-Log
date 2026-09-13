/**
 * Problem: Towers of Hanoi
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/towers-of-hanoi
 * Date: 2026-09-13
 * Difficulty: Medium
 * Topics: Recursion, Divide and Conquer
 *
 * Approach:
 * Classic recursive Towers of Hanoi. To move n disks from rod `a` to rod `b`
 * (using `c` as the auxiliary rod):
 *   1. Move the top (n-1) disks from `a` to `c` (using `b` as auxiliary)
 *   2. Move the nth (largest) disk from `a` to `b`
 *   3. Move the (n-1) disks from `c` to `b` (using `a` as auxiliary)
 * Base case: n === 0 means no disks to move, return an empty move list.
 *
 * Time Complexity: O(2^n)  — each call spawns two recursive calls, halving n each time
 * Space Complexity: O(2^n) for the output move list; O(n) for the recursion call stack
 */


// ------------------------- Solution -------------------------------------


function towerOfHanoi(n, a, b, c) {
  if (n === 0) {
    return [];
  }
  let moves = towerOfHanoi(n - 1, a, c, b);
  moves.push([a, b]);
  moves = moves.concat(towerOfHanoi(n - 1, c, b, a));
  return moves;
}
