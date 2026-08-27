"""
Problem: IQ Test
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/25/A
Date Solved: 2026-08-27
Difficulty: *1300
Topic: Brute Force

Approach:
Among n numbers, exactly one has different parity from the rest.
Split numbers into two lists by parity (even/odd) while tracking
their 1-based index. Since one group will always have exactly one
element, print its index.

Time Complexity: O(n)  -> single pass through the array
Space Complexity: O(n) -> storing indices in evens/odds lists
"""


# ----------------------- Solution ---------------------------


n = int(input())
numbers = list(map(int, input().split()))
evens = []
odds = []
for index, num in enumerate(numbers, start=1):
    if num % 2 == 0:
        evens.append(index)
    else:
        odds.append(index)
if len(evens) == 1:
    print(evens[0])
else:
    print(odds[0])
