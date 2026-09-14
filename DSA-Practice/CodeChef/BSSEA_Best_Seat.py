"""
Problem   : Best Seat
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY020/problems/BSSEA
Date      : 2026-09-14
Difficulty: Easy
Topics    : Arrays, Math, Greedy

Approach:
  Find the "center" of the seat range as the midpoint of (min, max) seat
  numbers. Since we're comparing distances of the form |2*seat - (low+high)|,
  we avoid floating-point division by working with center_twice = low + high
  and doubling each seat's distance instead. Scan once to find the seat
  closest to this center; on a tie, prefer the smaller seat number.

Time Complexity  : O(n)  -> one pass for min/max (via min()/max()), one pass to scan
Space Complexity : O(n)  -> for storing the input list (O(1) extra beyond input)
"""


# ------------------------------ Solution -------------------------------------


n = int(input())
seats = list(map(int, input().split()))
low = min(seats)
high = max(seats)
center_twice = low + high
best = seats[0]
for seat in seats[1:]:
    current_dist = abs(2 * seat - center_twice)
    best_dist = abs(2 * best - center_twice)
    if current_dist < best_dist or (
        current_dist == best_dist and seat < best
    ):
        best = seat
print(best)
