"""
Problem   : Timely Orders
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/timely-orders/
Difficulty: Easy
Topics    : Binary Search, Data Structures, Searching
Date      : 2026-10-03

Approach:
    Orders arrive in chronological order, so the `times` list stays sorted.
    A prefix-sum array stores the running total of order amounts.
    For a window query, bisect_left finds the first order with time >= t - k,
    and the answer is the prefix-sum difference from that index to the end.

Complexity:
    Time  : O(Q log Q) overall -> O(1) per insert, O(log Q) per query
    Space : O(Q) for the times and prefix arrays
"""


# --------------------------------------- Solution -------------------------------------------


from bisect import bisect_left
q = int(input())
times = []
prefix = [0]
for _ in range(q):
    query_type, a, t = map(int, input().split())
    if query_type == 1:
        times.append(t)
        prefix.append(prefix[-1] + a)
    else:
        k = a
        start = t - k
        left = bisect_left(times, start)
        right = len(times)
        total = prefix[right] - prefix[left]
        print(total)
