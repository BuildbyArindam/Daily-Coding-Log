"""
Problem   : Cutlet (Codeforces 939F)
Link      : https://codeforces.com/contest/939/problem/F
Date      : 2026-08-15
Difficulty: CF *2400
Topics    : Data Structures, DP (sliding window minimum)

Approach:
  Cutlet needs n seconds of frying on each side; k disjoint time
  intervals allow a flip. Track dp0[x] / dp1[x] = min flips so that
  the "currently-down" side has been fried for x seconds total, with
  dp0/dp1 distinguishing which physical side is currently down.
  Between intervals, x is simply shifted forward by the idle time
  (no flip possible). Within an interval of length L, a flip can
  happen at any point, so the best value reachable at position x is
  the min of dp[x-L..x] (0 or 1 flips) — computed with a monotonic
  deque (sliding window minimum) instead of a segment tree, giving
  O(1) amortized work per index per interval.
  Answer: feasibility ("Hungry") + min flips ("Full") after
  processing all k intervals and the trailing idle time to 2n.

Complexity:
  Time : O(n) amortized work per interval (deque-based sliding min)
         → O(n * k) overall in the worst case
  Space: O(n) for the dp arrays
"""


# ----------------------- Solution --------------------------


from collections import deque
import sys

def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  k = int(input_data[1])
  intervals = []
  ptr = 2
  for _ in range(k):
    l = int(input_data[ptr])
    r = int(input_data[ptr + 1])
    intervals.append((l, r))
    ptr += 2
  INF = float('inf')
  dp0 = [INF] * (n + 1)
  dp1 = [INF] * (n + 1)
  dp0[0] = 0
  last_r = 0
  for l, r in intervals:
    time_passed = l - last_r
    new_dp0 = [INF] * (n + 1)
    new_dp1 = [INF] * (n + 1)
    for x in range(n + 1):
      if x + time_passed <= n:
        new_dp0[x + time_passed] = dp0[x]
      new_dp1[x] = dp1[x]
    dp0 = new_dp0
    dp1 = new_dp1
    len_interval = r - l
    next_dp0 = [INF] * (n + 1)
    next_dp1 = [INF] * (n + 1)
    for x in range(n + 1):
      if x + len_interval <= n:
        next_dp0[x + len_interval] = dp0[x]
      next_dp1[x] = dp1[x]
    q = deque()
    for x in range(n + 1):
      while q and dp1[q[-1]] >= dp1[x]:
        q.pop()
      q.append(x)
      while q and q[0] < x - len_interval:
        q.popleft()
      if dp1[q[0]] != INF:
        next_dp0[x] = min(next_dp0[x], dp1[q[0]] + 1)
    q.clear()
    for x in range(n + 1):
      while q and dp0[q[-1]] >= dp0[x]:
        q.pop()
      q.append(x)
      while q and q[0] < x - len_interval:
        q.popleft()
      if dp0[q[0]] != INF:
        next_dp1[x] = min(next_dp1[x], dp0[q[0]] + 1)
    q.clear()
    for x in range(n + 1):
      while q and dp0[q[-1]] >= dp0[x]:
        q.pop()
      q.append(x)
      while q and q[0] < x - len_interval:
        q.popleft()
      if dp0[q[0]] != INF:
        next_dp0[x] = min(next_dp0[x], dp0[q[0]] + 2)
    q.clear()
    for x in range(n + 1):
      while q and dp1[q[-1]] >= dp1[x]:
        q.pop()
      q.append(x)
      while q and q[0] < x - len_interval:
        q.popleft()
      if dp1[q[0]] != INF:
        next_dp1[x] = min(next_dp1[x], dp1[q[0]] + 2)
    dp0 = next_dp0
    dp1 = next_dp1
    last_r = r
  time_passed = 2 * n - last_r
  final_ans = INF
  if n - time_passed >= 0:
    final_ans = min(final_ans, dp0[n - time_passed])
  final_ans = min(final_ans, dp1[n])
  if final_ans == INF:
    print("Hungry")
  else:
    print("Full")
    print(final_ans)

if __name__ == "__main__":
  solve()
  
