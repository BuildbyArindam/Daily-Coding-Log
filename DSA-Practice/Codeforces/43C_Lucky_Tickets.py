"""
Problem: Lucky Tickets
Link: https://codeforces.com/problemset/problem/43/C
Date: 2026-09-11
Difficulty: *1300
Topic: Greedy

Approach:
Ticket pairs balance out only via digit sums mod 3. Count how many
numbers fall into each residue class (0, 1, 2) mod 3. Numbers with
residue 0 can pair with each other; numbers with residue 1 pair with
residue 2 (since 1 + 2 = 3 ≡ 0). Answer = cnt[0] // 2 + min(cnt[1], cnt[2]).

Time Complexity: O(n)
Space Complexity: O(1) (excluding input storage)
"""


# ---------------------------- Solution -----------------------------------


import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
cnt = [0, 0, 0]
for x in a:
    cnt[x % 3] += 1
answer = cnt[0] // 2 + min(cnt[1], cnt[2])
print(answer)
