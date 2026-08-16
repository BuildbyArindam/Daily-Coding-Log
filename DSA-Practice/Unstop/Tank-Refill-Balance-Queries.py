# Problem: Tank Refill Balance Queries
# Platform: Unstop
# Link: https://unstop.com/code/practice/649849
# Difficulty: Easy
# Topic: Array, Prefix Sum
# Date Solved: 2026-08-16
#
# Approach:
# Build a prefix sum array `pre` where pre[i] = sum of a[0..i-1].
# For each query (l, r) (1-indexed, inclusive), the range sum is
# pre[r] - pre[l-1], computed in O(1) after O(n) preprocessing.
# Classify the sum as SURPLUS (>0), DEFICIT (<0), or BALANCED (=0).
#
# Time Complexity: O(n + q)  -> O(n) to build prefix sums, O(1) per query
# Space Complexity: O(n)     -> prefix sum array


# --------------------------- Solution ----------------------------


import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    a = [int(x) for x in data[idx:idx+n]]; idx += n
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i+1] = pre[i] + a[i]
    q = int(data[idx]); idx += 1
    out = []
    for _ in range(q):
        l = int(data[idx]); r = int(data[idx+1]); idx += 2
        s = pre[r] - pre[l-1]
        if s > 0:
            status = "SURPLUS"
        elif s < 0:
            status = "DEFICIT"
        else:
            status = "BALANCED"
        out.append(f"{s} {status}")
    sys.stdout.write("\n".join(out) + "\n")

main()
