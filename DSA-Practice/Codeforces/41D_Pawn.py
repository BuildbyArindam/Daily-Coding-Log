"""
Problem: Pawn
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/41/D
Difficulty: *1900
Date solved: 2026-09-09
Topic: DP (grid path DP with modulo state)

Approach:
    Process the board bottom-up. State = (column, running_sum % (k+1)).
    From each cell in a row, transition only comes from the two possible
    "previous" columns below it (since a pawn moves up-left or up-right,
    reversed here as coming from below-left/below-right). Track the max
    sum achievable for each (column, remainder) pair, and store parent
    pointers to reconstruct the actual path afterward. Answer is the best
    sum in the top row with remainder 0 (i.e., sum % (k+1) == 0).

Complexity:
    Let mod = k + 1.
    Time:  O(n * m * mod)  -- each of n rows, m columns, mod remainders,
                              2 transitions each.
    Space: O(n * m * mod)  -- parent table stores a pointer for every
                              (row, col, remainder); dp itself only needs
                              O(m * mod) since only the previous row matters.
"""


# ------------------------- Solution ------------------------------


n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
mod = k + 1
NEG = -10**9
dp = [[NEG] * mod for _ in range(m)]
parent = [[ [None] * mod for _ in range(m)] for _ in range(n)]
for c in range(m):
    value = board[n - 1][c]
    dp[c][value % mod] = value
for row in range(n - 2, -1, -1):
    new_dp = [[NEG] * mod for _ in range(m)]
    for c in range(m):
        for prev_c, move in ((c - 1, 'R'), (c + 1, 'L')):
            if 0 <= prev_c < m:
                for rem in range(mod):
                    if dp[prev_c][rem] == NEG:
                        continue
                    new_sum = dp[prev_c][rem] + board[row][c]
                    new_rem = new_sum % mod
                    if new_sum > new_dp[c][new_rem]:
                        new_dp[c][new_rem] = new_sum
                        parent[row][c][new_rem] = (
                            prev_c,
                            rem,
                            move
                        )
    dp = new_dp
best_sum = NEG
best_col = -1
for c in range(m):
    if dp[c][0] > best_sum:
        best_sum = dp[c][0]
        best_col = c
if best_sum == NEG:
    print(-1)
    exit()
moves = []
row = 0
col = best_col
rem = 0
while row < n - 1:
    prev_col, prev_rem, move = parent[row][col][rem]
    moves.append(move)
    col = prev_col
    rem = prev_rem
    row += 1
moves.reverse()
print(best_sum)
print(col + 1)
print(''.join(moves))
