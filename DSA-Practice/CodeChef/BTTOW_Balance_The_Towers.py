"""
Problem   : Balance the Towers
Link      : https://www.codechef.com/problems/BTTOW
Date      : 2026-09-09
Difficulty: Medium (CodeChef 3-star, ~1500-1600 CF-equivalent)
Topics    : Sorting, Greedy, Arrays

Approach:
    Sort the tower heights. Once sorted, for any split index i, consider
    raising all towers before i by +K and lowering all towers from i
    onward by -K (only valid where a[i] >= K, so heights stay non-negative).
    For each valid split, compute the resulting (max - min) and take the
    minimum over all splits, plus the original range as a baseline.

Time Complexity : O(N log N)  -- dominated by the sort; the scan is O(N)
Space Complexity: O(N)        -- storing the input array (sort is in-place)
"""


# ---------------------------- Solution -----------------------------------


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    a.sort()
    ans = a[-1] - a[0]
    for i in range(1, n):
        if a[i] < k:
            continue
        new_min = min(a[0] + k, a[i] - k)
        new_max = max(a[i - 1] + k, a[-1] - k)
        ans = min(ans, new_max - new_min)
    print(ans)

if __name__ == "__main__":
    solve()
