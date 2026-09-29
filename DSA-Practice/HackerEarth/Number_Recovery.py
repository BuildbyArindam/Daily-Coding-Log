"""
Problem   : Number Recovery
Platform  : HackerEarth (Data Structures > Queues > Basics of Queues)
Link      : https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/number-recovery-0b988eb2/
Date      : 2026-09-29
Difficulty: Medium

Approach:
  Each person i has at most two candidate values {a-d, a+d} (positive only).
  Maintain hash-map counters of how many trusted and distrusted people
  contain each value. After every query, a value x is valid iff:
    trusted_count[x] == total_trusted  and  distrusted_count[x] == 0
  Any valid x must appear in every trusted person's set, so it is enough
  to test the (<= 2) candidates of one arbitrary trusted person.
  State changes are handled by removing the old state's contribution and
  adding the new one, so each query is O(1) work.

Complexity:
  Time : O(N + Q) (each query touches <= 2 values, plus sorting <= 2 items)
  Space: O(N) for candidate tuples, state, and the counter maps
"""


# ------------------------------------ Solution --------------------------------------------


import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
vals = [None] * N
for i in range(N):
    a, d = map(int, input().split())
    s = set()
    x1 = a - d
    x2 = a + d
    if x1 > 0:
        s.add(x1)
    if x2 > 0:
        s.add(x2)
    vals[i] = tuple(s)
state = [0] * N
trusted_total = 0
trusted_count = {}
distrusted_count = {}
trusted_ids = set()

def add_count(mp, x):
    mp[x] = mp.get(x, 0) + 1

def remove_count(mp, x):
    v = mp[x] - 1
    if v == 0:
        del mp[x]
    else:
        mp[x] = v
out = []
for _ in range(Q):
    t, idx = map(int, input().split())
    idx -= 1
    old = state[idx]
    new = t
    if old == 1:
        trusted_total -= 1
        trusted_ids.remove(idx)
        for x in vals[idx]:
            remove_count(trusted_count, x)
    elif old == 2:
        for x in vals[idx]:
            remove_count(distrusted_count, x)
    if new == 1:
        trusted_total += 1
        trusted_ids.add(idx)
        for x in vals[idx]:
            add_count(trusted_count, x)
    elif new == 2:
        for x in vals[idx]:
            add_count(distrusted_count, x)
    state[idx] = new
    if trusted_total == 0:
        out.append("-1")
        continue
    first_id = next(iter(trusted_ids))
    answer = []
    for x in vals[first_id]:
        if trusted_count.get(x, 0) != trusted_total:
            continue
        if distrusted_count.get(x, 0) != 0:
            continue
        answer.append(x)
    answer.sort()
    if not answer:
        out.append("0")
    else:
        out.append(str(len(answer)) + " " + " ".join(map(str, answer)))
sys.stdout.write("\n".join(out))
