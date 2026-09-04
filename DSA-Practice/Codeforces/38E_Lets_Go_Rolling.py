"""
Problem: Let's Go Rolling! (CF 38E)
Link: https://codeforces.com/problemset/problem/38/E
Date: 2026-09-04
Difficulty: *1800
Topics: DP, Sortings

Approach:
Sort marbles by coordinate. dp[i] = min cost when marble i is the
rightmost "pinned" marble so far, with all marbles before it having
already rolled to some earlier pinned marble. Transition cost from
pinned i -> next pinned j (marbles i+1..j-1 roll to i, then j is
pinned) simplifies to a linear function of j:

    dp[j] = c[j] + pref[j-1] + min over i<j of (dp[i] - pref[i] + (i+1)*x[i] - j*x[i])

The min-of-linear-functions term is optimized with a monotonic
Convex Hull Trick (slopes -x[i] strictly decreasing as i increases,
query points j strictly increasing), giving O(n) after the O(n log n)
sort. Final answer takes the best choice of last pinned marble, with
all remaining marbles rolling to it.

Time complexity: O(n log n)  (dominated by the initial sort; CHT is O(n))
Space complexity: O(n)
"""


# ------------------------ Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    marbles = [tuple(map(int, input().split())) for _ in range(n)]
    marbles.sort()
    x = [0] * (n + 1)
    c = [0] * (n + 1)
    for i, (xi, ci) in enumerate(marbles, 1):
        x[i] = xi
        c[i] = ci
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + x[i]
    dp = [0] * (n + 1)
    slopes = []
    intercepts = []
    head = 0
    def add_line(m, b):
        while len(slopes) - head >= 2:
            m1, b1 = slopes[-2], intercepts[-2]
            m2, b2 = slopes[-1], intercepts[-1]
            if (b2 - b1) * (m2 - m) >= (b - b2) * (m1 - m2):
                slopes.pop()
                intercepts.pop()
            else:
                break
        slopes.append(m)
        intercepts.append(b)
    def query(q):
        nonlocal head
        while (
            head + 1 < len(slopes)
            and slopes[head + 1] * q + intercepts[head + 1]
            <= slopes[head] * q + intercepts[head]
        ):
            head += 1
        return slopes[head] * q + intercepts[head]
    dp[1] = c[1]
    add_line(
        -x[1],
        dp[1] - pref[1] + 2 * x[1]
    )
    for j in range(2, n + 1):
        dp[j] = c[j] + pref[j - 1] + query(j)
        add_line(
            -x[j],
            dp[j] - pref[j] + (j + 1) * x[j]
        )
    answer = 10**30
    for i in range(1, n + 1):
        movement = pref[n] - pref[i] - (n - i) * x[i]
        answer = min(answer, dp[i] + movement)
    print(answer)

if __name__ == "__main__":
    solve()
