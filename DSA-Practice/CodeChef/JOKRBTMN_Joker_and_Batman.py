"""
Problem   : Joker and Batman (JOKRBTMN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/JOKRBTMN
Difficulty: 1816
Topics    : Arrays, Implementation
Date      : 2026-10-13

Approach:
    Label every element with the index of the group it belongs to (0 if it
    belongs to none). Then scan the strip once and count a new segment each
    time two adjacent elements have different group labels. The answer is
    1 + the number of adjacent label changes.

Complexity:
    Time  : O(sum of k_i + L) per test case
    Space : O(N) for the group-label array
"""


# -------------------------------------------------- Solution ----------------------------------------------------------


t = int(input())

for _ in range(t):
    n, m, l = map(int, input().split())
    group = [0] * (n + 1)
    for i in range(1, m + 1):
        data = list(map(int, input().split()))
        k = data[0]
        for j in range(1, k + 1):
            group[data[j]] = i
    strip = list(map(int, input().split()))
    segments = 1
    for i in range(1, l):
        if group[strip[i]] != group[strip[i - 1]]:
            segments += 1
    print(segments)
