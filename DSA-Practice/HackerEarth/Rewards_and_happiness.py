"""
Problem   : Rewards and Happiness
Platform  : HackerEarth (Monk series, Hard)
Link      : https://www.hackerearth.com/practice/codemonk/8/1504742/
Date      : 2026-09-23
Topics    : Binary Search, Graphs (adjacency list), Prefix Sums

Approach  :
  - Each person's happiness is the sum of rewards their friends have received so
    far, and this only grows over time (rewards are added, never removed).
    That makes "earliest day the sum reaches k" a monotonic predicate, so we can
    binary search on the day.
  - For each friend, store the days they got rewards plus a running prefix sum.
    The friend's total on day d is one bisect_right lookup into their prefix sums.
  - Per person: first check the final totals. If the sum of friends' final
    rewards is below k, the answer is -1. Otherwise binary search over [1, q].
    Both the total check and the predicate stop early once the sum reaches k.

Complexity:
  Time  : O(q + m * log q * log R), where R is the max number of reward events
          for a single person. Each edge is visited once per binary-search
          step per endpoint, and each visit costs one bisect.
  Space : O(n + m + q) for adjacency lists, reward days and prefix sums.
"""


# ------------------------------------------- Solution -----------------------------------------


import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())
    friends = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    q = int(input())
    reward_days = [[] for _ in range(n)]
    reward_sum = [[] for _ in range(n)]
    for day in range(1, q + 1):
        p, z = map(int, input().split())
        p -= 1
        reward_days[p].append(day)
        previous = reward_sum[p][-1] if reward_sum[p] else 0
        reward_sum[p].append(previous + z)
    total_reward = [s[-1] if s else 0 for s in reward_sum]
    answer = [-1] * n
    for person in range(n):
        total = 0
        for friend in friends[person]:
            total += total_reward[friend]
            if total >= k:
                break
        if total < k:
            continue
        def enough(day):
            total = 0
            for friend in friends[person]:
                days = reward_days[friend]
                idx = bisect_right(days, day) - 1
                if idx >= 0:
                    total += reward_sum[friend][idx]
                    if total >= k:
                        return True
            return False
        left = 1
        right = q
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        answer[person] = left
    print(*answer)

if __name__ == "__main__":
    solve()
