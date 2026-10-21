"""
Problem   : Water Hole Vigilance
Platform  : Unstop
Link      : https://unstop.com/code/practice/667528
Difficulty: Easy
Topics    : Sliding Window, Hashing, Queue, Frequency Counting, Two Pointers
Date      : 2026-10-21

Approach:
    Process the (T, S) records in order while maintaining a time window
    [T - W, T] with a frequency map of species/IDs inside it. For each new
    record, advance the left pointer to evict records older than T - W
    (decrementing their counts), then add the current record. If the count
    of S in the window reaches K, count it as an alert and remember the
    first one seen. Print the alert count and the earliest alert, or
    "QUIET" if there were none.

Complexity:
    Time  : O(N) - each record is added once and evicted at most once.
    Space : O(N) - records list is never trimmed (O(W + distinct S) if a
            deque were used to drop evicted records).
"""


# ------------------------------------------- Solution ------------------------------------------------


import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N, W, K = map(int, input().split())
    records = []
    freq = defaultdict(int)
    alerts = 0
    earliest_alert = None
    left = 0
    for _ in range(N):
        T, S = map(int, input().split())
        while left < len(records) and records[left][0] < T - W:
            old_T, old_S = records[left]
            freq[old_S] -= 1
            left += 1
        records.append((T, S))
        freq[S] += 1
        if freq[S] >= K:
            alerts += 1
            if earliest_alert is None:
                earliest_alert = (T, S)
    print(alerts)
    if earliest_alert is not None:
        print(earliest_alert[0], earliest_alert[1])
    else:
        print("QUIET")

if __name__ == "__main__":
    main()
