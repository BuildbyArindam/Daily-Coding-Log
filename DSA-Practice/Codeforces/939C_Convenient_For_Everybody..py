"""
Problem: Convenient For Everybody
Platform: Codeforces
Link: https://codeforces.com/contest/939/problem/C
Date: 2026-08-15
Difficulty: *1600
Topics: Binary Search, Two Pointers (Sliding Window)

Approach:
Duplicate the array (a2 = a + a) to linearize the circular hour range.
Maintain a fixed-size sliding window of length (f - s) over a2, updating
the window sum in O(1) per shift (add incoming hour, drop outgoing hour).
Track the maximum participant sum and, on ties, the smallest start time
(mapped back to the original 1..n hour labeling via get_start_time).

Time Complexity: O(n)   -- single pass with a sliding window
Space Complexity: O(n)  -- doubled array a2
"""


# --------------------- Solution --------------------------


import sys

def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  a = [int(x) for x in input_data[1 : n + 1]]
  s = int(input_data[n + 1])
  f = int(input_data[n + 2])
  len_window = f - s
  a2 = a + a
  current_participants = sum(a2[:len_window])
  max_participants = current_participants
  best_start_time = float("inf")
  def get_start_time(i):
    t = (s - (i + 1)) % n + 1
    return t
  best_start_time = get_start_time(0)
  for i in range(1, n):
    current_participants += a2[i + len_window - 1] - a2[i - 1]
    start_time = get_start_time(i)
    if current_participants > max_participants:
      max_participants = current_participants
      best_start_time = start_time
    elif current_participants == max_participants:
      best_start_time = min(best_start_time, start_time)
  print(best_start_time)

if __name__ == "__main__":
  solve()
  
