"""
Problem: End Game
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/end-game/
Difficulty: Easy
Topics: Algorithms, Approved, Math, Open
Date Solved: 2026-09-07

Approach:
Simulate king-vs-king chess distance rules on an n x n board.
- Kings are "adjacent" (touching) if both the horizontal gap and 
  vertical gap between them are <= 1.
- If it's White's move (Move == 0), White wins unless moving toward 
  the Black king would bring it adjacent to Black's king before 
  reaching the edge — i.e., Black can "Draw" only if it can stay 
  >= 1 square away both horizontally and keep enough room (c >= a) 
  while the horizontal offset (d - b) fits within the remaining board (n - a).
- If it's Black's move (Move == 1), Black gets one extra tempo, 
  relaxing the horizontal/vertical thresholds by 1 (c >= a - 1, 
  horizontal <= n - a + 1).
- Otherwise White forces a win by cornering.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# --------------------------- Solution ------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, a, b, c, d, Move = map(int, input().split())
    horizontal = abs(d - b)
    if Move == 0:
        if c >= a and horizontal <= (n - a):
            print("Draw")
        else:
            print("White Wins")
    else:
        if c >= a - 1 and horizontal <= (n - a + 1):
            print("Draw")
        else:
            print("White Wins")
