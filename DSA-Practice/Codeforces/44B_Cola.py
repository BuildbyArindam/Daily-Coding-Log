# Problem: Cola (Codeforces 44B)
# Link: https://codeforces.com/problemset/problem/44/B
# Date: 2026-09-11
# Difficulty: *1500 | Topic: Implementation
#
# Approach:
#   Bottles come in 0.5L (a available), 1L (b available), 2L (c available).
#   Fix z = number of 2L bottles used (0 <= z <= min(c, n//2)).
#   Remaining volume m = n - 2z must be made from 1L bottles (count y) and
#   0.5L bottles. For a given y: leftover (m - y) liters need (m - y) * 2
#   half-liter bottles, so (m - y) <= a // 2  =>  y >= m - a // 2.
#   Also 0 <= y <= min(b, m). Count valid y's for each z and sum.
#
# Time complexity: O(n) - single loop over z, up to n//2 + 1 iterations
# Space complexity: O(1)


# -------------------------- Solution -----------------------------------


n, a, b, c = map(int, input().split())
ans = 0
for z in range(min(c, n // 2) + 1):
    m = n - 2 * z
    low = max(0, m - a // 2)
    high = min(b, m)
    if low <= high:
        ans += high - low + 1
print(ans)
