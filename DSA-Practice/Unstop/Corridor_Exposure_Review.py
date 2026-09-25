# Problem: Corridor Exposure Review
# Platform: Unstop
# Link: https://unstop.com/code/practice/660869
# Solved: 2026-09-25
# Difficulty: Hard
# Topics: Fenwick Tree, Offline/Version Queries, Range Addition, Range Sum Query, prefix aggregation, Monotone Stack, Monotonic Stack, Binary Indexed Tree, Array
#
# Approach:
# - Process the array from left to right using a monotonic decreasing stack.
# - For every right endpoint, maintain the ranges over which each stack value
#   is the maximum, along with a cumulative sum of suffix-maximum contributions.
# - Store binary-lifting ancestors of each stack node so a query [l, r] can
#   jump through the previous-greater chain and locate the block crossing l
#   in O(log n).
# - Use the precomputed cumulative contribution plus a direct boundary-block
#   adjustment to answer each query.
#
# Complexity:
# - Preprocessing: O(n log n)
# - Each query: O(log n)
# - Total: O((n + q) log n)
# - Space: O(n log n)


# --------------------------------------- Solution ------------------------------------------


import sys
from array import array

MOD = 1_000_000_007
data = list(map(int, sys.stdin.buffer.read().split()))
p = 0
n = data[p]
p += 1
a = data[p:p + n]
p += n
q = data[p]
p += 1
queries = []
for _ in range(q):
    l = data[p]
    r = data[p + 1]
    p += 2
    queries.append((l, r))
LOG = n.bit_length()
start = array('i')
pref = array('i')
up = [array('i') for _ in range(LOG)]
top = -1
for r in range(1, n + 1):
    x = a[r - 1]
    s = r
    while top != -1 and a[top] <= x:
        s = start[top]
        top = up[0][top]
    node = r - 1
    contribution = ((r - s + 1) * x) % MOD
    if top != -1:
        contribution = (contribution + pref[top]) % MOD
    start.append(s)
    pref.append(contribution)
    up[0].append(top)
    for k in range(1, LOG):
        parent = up[k - 1][node]
        if parent == -1:
            up[k].append(-1)
        else:
            up[k].append(up[k - 1][parent])
    top = node
out = []
for l, r in queries:
    cur = r - 1
    if start[cur] > l:
        for k in range(LOG - 1, -1, -1):
            anc = up[k][cur]
            if anc != -1 and start[anc] > l:
                cur = anc
        block = up[0][cur]
    else:
        block = cur
    ans = pref[r - 1]
    if block != -1:
        ans -= pref[block]
        length = (block + 1) - l + 1
        ans += a[block] * length
    out.append(str(ans % MOD))
sys.stdout.write("\n".join(out))
