# Problem: Furniture Transportation
# Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/furniture-transportation-2/
# Platform: HackerEarth | Difficulty: Easy | Topic: Ad-Hoc, Open
# Date: 2026-09-04
#
# Approach: Single pass over the array, tracking a running count of
# consecutive items with length <= l (fits without disassembly). Whenever
# this streak reaches m, one truck trip is counted; the streak resets to 0
# on any item exceeding l.
#
# Time Complexity: O(n)  — one linear scan
# Space Complexity: O(1) — only a running counter besides the input array


# -------------------------- Solution -------------------------------


n, l, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
consecutive = 0
for x in a:
    if x <= l:
        consecutive += 1
        if consecutive >= m:
            ans += 1
    else:
        consecutive = 0
print(ans)
