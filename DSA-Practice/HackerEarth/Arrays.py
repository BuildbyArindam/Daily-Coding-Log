"""
Problem   : Arrays
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/theatre-830bdbff/
Difficulty: Hard
Topics    : Ad-Hoc, Data Structures, Heaps, Trees
Date      : 2026-09-03

Approach:
    Each of the n items has three "buckets" (a, b, c) that sum to s = a+b+c.
    We want to repeatedly reduce the max element across all buckets (each
    reduction costs 1 and shrinks one bucket by 1) k times total... actually,
    reframed: track s = q*k + r for each item, and bucket items by quotient
    q into cnt[q]. Every unit "spend" event ((k - a), (k - b), (k - c)) marks
    the earliest point at which bucket a/b/c would need another reduction
    to stay under threshold. Process spend events in increasing time order,
    decrementing each item's quotient (moving it from cnt[old_q] to
    cnt[old_q-1]) as its threshold is crossed. At each time step, find the
    currently-highest quotient bucket Q with count > 0, then take the item
    in that bucket with the largest remainder to compute a candidate score
    (3*t + Q*k + best_r), and keep the running minimum as the answer.

    order[] presorts items by remainder (descending) so that once we know
    Q, we scan forward from ptr to find the first still-in-bucket-Q item
    with the largest remainder in O(1) amortized per step.

Complexity:
    Time : O(N log N + N + Q_events) ≈ O(N log N), events processed
           in a single amortized pass (~3N events total)
    Space: O(N) for rem[], qcur[], events[], order[]
"""


# ------------------------------ Solution ------------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    rem = [0] * n
    qcur = [0] * n
    cnt = [0] * 6
    ans = 0
    SHIFT = 19
    MASK = (1 << SHIFT) - 1
    events = []
    for i in range(n):
        a, b, c = map(int, input().split())
        s = a + b + c
        if s > ans:
            ans = s
        q, r = divmod(s, k)
        qcur[i] = q
        rem[i] = r
        cnt[q + 3] += 1
        if a:
            events.append(((k - a) << SHIFT) | i)
        if b:
            events.append(((k - b) << SHIFT) | i)
        if c:
            events.append(((k - c) << SHIFT) | i)
    order = list(range(n))
    order.sort(key=rem.__getitem__, reverse=True)
    events.sort()
    Q = 2
    while cnt[Q + 3] == 0:
        Q -= 1
    ptr = 0
    p = 0
    m = len(events)
    while p < m:
        t = events[p] >> SHIFT
        while p < m and (events[p] >> SHIFT) == t:
            i = events[p] & MASK
            old_q = qcur[i]
            new_q = old_q - 1
            qcur[i] = new_q
            cnt[old_q + 3] -= 1
            cnt[new_q + 3] += 1
            p += 1
        while cnt[Q + 3] == 0:
            Q -= 1
            ptr = 0
        while qcur[order[ptr]] != Q:
            ptr += 1
        best_r = rem[order[ptr]]
        cur = 3 * t + Q * k + best_r
        if cur < ans:
            ans = cur
    print(ans)

if __name__ == "__main__":
    solve()
