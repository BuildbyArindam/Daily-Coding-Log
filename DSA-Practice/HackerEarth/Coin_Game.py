"""
Problem   : Coin Game
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/coin-game-3-1762eeeb/
Difficulty: Easy
Topic     : Ad-Hoc, Implementation, Game Theory (parity trick)
Date      : 2026-08-20

Approach:
  Each pile of coins can be repeatedly halved as long as it's even; each
  halving counts as one "move". Sum the total number of halving moves
  across all piles in a test case. Since players alternate moves and the
  player unable to move loses, the total move count's parity decides the
  winner: if total_moves is even, the first player (Alan) makes the last
  move and wins; if odd, the second player (Charlie) wins.

Time Complexity : O(N * log(max(A_i))) per test case
                   (each pile takes O(log a) halving steps)
Space Complexity: O(1) extra (excluding input buffer)
"""


# -------------------------- Solution ----------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        total_moves = 0
        for _ in range(n):
            a = int(data[idx]); idx += 1
            while a > 0 and a % 2 == 0:
                a //= 2
                total_moves += 1
        results.append("Charlie" if total_moves % 2 != 0 else "Alan")
    print("\n".join(results))

if __name__ == "__main__":
    solve()
