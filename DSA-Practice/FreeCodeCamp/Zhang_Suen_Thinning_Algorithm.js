/**
 * Problem: Zhang-Suen Thinning Algorithm
 * Platform: FreeCodeCamp — Rosetta Code Challenges
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/zhang-suen-thinning-algorithm
 * Date Solved: 2026-09-05
 * Difficulty: Medium-Hard (respected estimate — image-processing + iterative matrix simulation)
 * Topics: Matrix/Grid Simulation, Image Processing, Iterative Convergence, 2D Array Traversal, Bitwise-style Neighbor Counting
 *
 * Approach:
 * Convert the ASCII image into a boolean pixel grid. Repeatedly apply two
 * sub-iterations (Step 1 and Step 2) that each scan every interior black
 * pixel, compute:
 *   - B(P1): count of black 8-neighbors (must be 2–6)
 *   - A(P1): number of white-to-black transitions in the ordered
 *     neighbor sequence P2..P9..P2 (must be exactly 1)
 *   - Step-specific corner conditions (P2*P4*P6 / P4*P6*P8 for step 1,
 *     P2*P4*P8 / P2*P6*P8 for step 2)
 * Pixels satisfying all conditions are marked for deletion and removed
 * only after the full pass (avoids mutating neighbors mid-scan). The
 * loop continues until neither step deletes any pixel (convergence),
 * producing the topological skeleton of the shape.
 *
 * Time Complexity: O(k * h * w), where h*w is the grid size and k is the
 * number of thinning iterations until convergence (k is small/bounded
 * in practice, but not a fixed constant — depends on image shape).
 * Space Complexity: O(h * w) for the pixel grid and per-pass deletion lists.
 */


// ------------------------- Solution -------------------------------------


function thinImage(image) {
    const pixels = image.map(row => row.split('').map(ch => ch === '#'));
    const height = pixels.length;
    const width = height > 0 ? pixels[0].length : 0;
    function A(p2, p3, p4, p5, p6, p7, p8, p9) {
        const sequence = [p2, p3, p4, p5, p6, p7, p8, p9, p2];
        let transitions = 0;
        for (let i = 0; i < 8; i++) {
            if (!sequence[i] && sequence[i + 1]) {
                transitions++;
            }
        }
        return transitions;
    }
    function B(p2, p3, p4, p5, p6, p7, p8, p9) {
        return (
            Number(p2) +
            Number(p3) +
            Number(p4) +
            Number(p5) +
            Number(p6) +
            Number(p7) +
            Number(p8) +
            Number(p9)
        );
    }
    let changed = true;
    while (changed) {
        changed = false;
        const toDeleteStep1 = [];
        for (let r = 1; r < height - 1; r++) {
            for (let c = 1; c < width - 1; c++) {
                if (!pixels[r][c]) {
                    continue;
                }
                const p2 = pixels[r - 1][c];
                const p3 = pixels[r - 1][c + 1];
                const p4 = pixels[r][c + 1];
                const p5 = pixels[r + 1][c + 1];
                const p6 = pixels[r + 1][c];
                const p7 = pixels[r + 1][c - 1];
                const p8 = pixels[r][c - 1];
                const p9 = pixels[r - 1][c - 1];
                const blackNeighbors = B(
                    p2, p3, p4, p5, p6, p7, p8, p9
                );
                const transitions = A(
                    p2, p3, p4, p5, p6, p7, p8, p9
                );
                if (
                    blackNeighbors >= 2 &&
                    blackNeighbors <= 6 &&
                    transitions === 1 &&
                    !(p2 && p4 && p6) &&
                    !(p4 && p6 && p8)
                ) {
                    toDeleteStep1.push([r, c]);
                }
            }
        }
        for (const [r, c] of toDeleteStep1) {
            pixels[r][c] = false;
        }
        if (toDeleteStep1.length > 0) {
            changed = true;
        }
        const toDeleteStep2 = [];
        for (let r = 1; r < height - 1; r++) {
            for (let c = 1; c < width - 1; c++) {
                if (!pixels[r][c]) {
                    continue;
                }
                const p2 = pixels[r - 1][c];
                const p3 = pixels[r - 1][c + 1];
                const p4 = pixels[r][c + 1];
                const p5 = pixels[r + 1][c + 1];
                const p6 = pixels[r + 1][c];
                const p7 = pixels[r + 1][c - 1];
                const p8 = pixels[r][c - 1];
                const p9 = pixels[r - 1][c - 1];
                const blackNeighbors = B(
                    p2, p3, p4, p5, p6, p7, p8, p9
                );
                const transitions = A(
                    p2, p3, p4, p5, p6, p7, p8, p9
                );
                if (
                    blackNeighbors >= 2 &&
                    blackNeighbors <= 6 &&
                    transitions === 1 &&
                    !(p2 && p4 && p8) &&
                    !(p2 && p6 && p8)
                ) {
                    toDeleteStep2.push([r, c]);
                }
            }
        }
        for (const [r, c] of toDeleteStep2) {
            pixels[r][c] = false;
        }
        if (toDeleteStep2.length > 0) {
            changed = true;
        }
    }
    return pixels.map(row =>
        row.map(pixel => pixel ? '#' : ' ').join('')
    );
}

const testImage1 = [
    '                               ',
    '#########       ########       ',
    '###   ####     ####  ####      ',
    '###    ###     ###    ###      ',
    '###   ####     ###             ',
    '#########      ###             ',
    '### ####       ###    ###      ',
    '###  ####  ### ####  #### ###  ',
    '###   #### ###  ########  ###  ',
    '                               '
];

console.log(thinImage(testImage1).join('\n'));
