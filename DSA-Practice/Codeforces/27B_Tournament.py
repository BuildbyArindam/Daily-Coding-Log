"""
Problem: Tournament
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/27/B
Difficulty: *1300
Topics: Bitmasks, Brute Force, DFS and Similar, Greedy
Date: 2026-08-28

Approach:
In a round-robin tournament of n players (n*(n-1)/2 total games), exactly
one game result is missing (n*(n-1)/2 - 1 games are given). Track wins per
player and a played[i][j] matrix. Find the single unplayed pair (a, b) by
scanning the upper triangle. Since every player's win count must differ
(strict ranking, no ties possible in this problem's guarantee), the missing
game's winner is whichever of a, b has the higher current win count -
their win count already reflects all other games, so the winner needs one
more win than the loser to keep the strict total ordering consistent.

Time Complexity: O(n^2) - dominated by the played[][] matrix scan
Space Complexity: O(n^2) - played[][] matrix; O(n) for wins[]
"""


# ---------------------------------- Solution ------------------------------------------


n = int(input())
wins = [0] * n
played = [[False] * n for _ in range(n)]

for _ in range(n * (n - 1) // 2 - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    played[x][y] = played[y][x] = True
    wins[x] += 1
a = b = -1
for i in range(n):
    for j in range(i + 1, n):
        if not played[i][j]:
            a, b = i, j
            break
    if a != -1:
        break
if wins[a] >= wins[b]:
    print(a + 1, b + 1)
else:
    print(b + 1, a + 1)
