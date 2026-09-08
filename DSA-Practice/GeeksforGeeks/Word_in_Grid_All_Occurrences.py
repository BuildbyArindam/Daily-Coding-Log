"""
Problem   : Word in Grid - All Occurrences
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/find-the-string-in-grid0111/1
Date      : 2026-09-08
Difficulty: Medium
Topics    : Recursion, DFS, Matrix

Approach:
For each cell matching the word's first character, try all 8 directions
(N, S, E, W, and 4 diagonals). Walk along a direction character-by-character,
bounds-checking at each step, until the full word matches or the walk breaks.
Record the starting cell if any direction yields a full match.

Time Complexity : O(n * m * 8 * k)  -- n,m = grid dims, k = word length
Space Complexity: O(1) extra (excluding output list)
"""


# ----------------------- Solution ----------------------------------


class Solution:
    def searchWord(self, mat, word):
        # code here
        n = len(mat)
        m = len(mat[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        ans = []
        k = len(word)
        for i in range(n):
            for j in range(m):
                if mat[i][j] != word[0]:
                    continue
                found = False
                for di, dj in directions:
                    x, y = i, j
                    p = 0
                    while p < k:
                        if (x < 0 or x >= n or
                            y < 0 or y >= m or
                            mat[x][y] != word[p]):
                            break
                        x += di
                        y += dj
                        p += 1
                    if p == k:
                        found = True
                        break
                if found:
                    ans.append([i, j])
        return ans
