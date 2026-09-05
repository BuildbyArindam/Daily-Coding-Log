/**
 * Problem: Zig-Zag Matrix
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/rosetta-code-zig-zag-matrix
 * Date: 2026-09-05
 * Difficulty	: Easy-Medium
 * Topics : Arrays, Matrix, Diagonal Traversal, Simulation
 *
 * Approach:
 * Fill the matrix diagonal by diagonal (there are 2n-1 diagonals total).
 * For each diagonal index `d`, collect all (row, col) cells where row + col = d,
 * bounded by the matrix edges. Even-indexed diagonals get their cell order
 * reversed so the fill direction alternates (up-right / down-left), which is
 * what produces the zig-zag pattern. Assign values 0..n²-1 in that traversal order.
 *
 * Time complexity: O(n²) — every cell is visited and assigned exactly once.
 * Space complexity: O(n²) for the output matrix (O(n) extra for the diagonal buffer).
 */


// ------------------------------ Solution ----------------------------------


function ZigZagMatrix(n) {
  const matrix = Array.from({ length: n }, () => Array(n).fill(0));
  let value = 0;
  for (let diagonal = 0; diagonal < 2 * n - 1; diagonal++) {
    const startRow = diagonal < n ? 0 : diagonal - n + 1;
    const endRow = Math.min(diagonal, n - 1);
    const cells = [];
    for (let row = startRow; row <= endRow; row++) {
      const col = diagonal - row;
      cells.push([row, col]);
    }
    if (diagonal % 2 === 0) {
      cells.reverse();
    }
    for (const [row, col] of cells) {
      matrix[row][col] = value++;
    }
  }
  return matrix;
}
