"""
Problem   : Crossword Puzzle Solver
Platform  : Coding360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/crossword_626480?kunjiRedirection=true
Date      : 2026-08-27
Difficulty: Medium

Approach:
- Backtracking over the list of words. For each word, try every cell (r, c)
  in the 10x10 grid as a horizontal or vertical starting position.
- A placement is valid if it fits within bounds, the cell just before/after
  the word (if any) is a '+' separator, and every cell along the word is
  either blank ('-') or already matches the required letter.
- Place the word (only overwriting '-' cells, tracking which cells were
  changed), recurse to the next word, and undo the placement if the
  recursive call fails (classic backtrack-and-restore).

Time Complexity : O(W * N^2 * L) per attempt in the worst case, with
                   exponential blowup from backtracking across W words
                   (W = number of words, N = 10, L = max word length).
Space Complexity: O(N^2) for the grid + O(L) recursion/undo bookkeeping
                   per call, O(W) for recursion depth.
"""


# -------------------------- Solution --------------------------------


def solve_crossword(grid, words):
    n = 10
    def can_place_horizontal(r, c, word):
        if c + len(word) > n:
            return False
        if c > 0 and grid[r][c - 1] != '+':
            return False
        if c + len(word) < n and grid[r][c + len(word)] != '+':
            return False
        for i in range(len(word)):
            if grid[r][c + i] not in ('-', word[i]):
                return False
        return True
    def can_place_vertical(r, c, word):
        if r + len(word) > n:
            return False
        if r > 0 and grid[r - 1][c] != '+':
            return False
        if r + len(word) < n and grid[r + len(word)][c] != '+':
            return False
        for i in range(len(word)):
            if grid[r + i][c] not in ('-', word[i]):
                return False
        return True
    def place_horizontal(r, c, word):
        changed = []
        for i in range(len(word)):
            if grid[r][c + i] == '-':
                grid[r][c + i] = word[i]
                changed.append((r, c + i))
        return changed
    def place_vertical(r, c, word):
        changed = []
        for i in range(len(word)):
            if grid[r + i][c] == '-':
                grid[r + i][c] = word[i]
                changed.append((r + i, c))
        return changed
    def undo(changed):
        for r, c in changed:
            grid[r][c] = '-'
    def backtrack(index):
        if index == len(words):
            return True
        word = words[index]
        for r in range(n):
            for c in range(n):
                if can_place_horizontal(r, c, word):
                    changed = place_horizontal(r, c, word)
                    if backtrack(index + 1):
                        return True
                    undo(changed)
                if can_place_vertical(r, c, word):
                    changed = place_vertical(r, c, word)
                    if backtrack(index + 1):
                        return True
                    undo(changed)
        return False
    backtrack(0)

grid = [list(input().strip()) for _ in range(10)]
words = input().strip().split(';')
solve_crossword(grid, words)
for row in grid:
    print(''.join(row))
