"""
Problem: Pacifist Frogs
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/39/F
Difficulty: *1300
Topic: Implementation
Date: 2026-09-06

Approach:
For each possible jump length d, count how many mosquito positions
are divisible by d (i.e., landed on and "smashed"). Track the minimum
smashed count across all frogs, keeping every jump length that ties
for that minimum.

Time Complexity: O(n * m) — n jump lengths, m mosquitoes checked per jump
Space Complexity: O(n) — for the answer list
"""


# ------------------------- Solution --------------------------------


n, m, k = map(int, input().split())
jumps = list(map(int, input().split()))
mosquitoes = list(map(int, input().split()))
best = k + 1
answer = []
for i, d in enumerate(jumps):
    smashed = 0
    for x in mosquitoes:
        if x % d == 0:
            smashed += 1
    if smashed < best:
        best = smashed
        answer = [i + 1]
    elif smashed == best:
        answer.append(i + 1)
print(len(answer))
print(*answer)
