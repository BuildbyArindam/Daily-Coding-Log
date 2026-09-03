"""
Problem   : The savior? [3]
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-savior-3/
Difficulty: Easy
Topics    : Ad-Hoc, Math, Open
Date      : 2026-09-03

Approach:
    Count how many unordered pairs (i, j) have a[i] and a[j] of the
    same parity (both even or both odd) — that's even*(even-1)/2 +
    odd*(odd-1)/2. Then subtract the pairs that are same parity AND
    same value (which shouldn't count), computed per distinct value
    via count*(count-1)/2 using a frequency map. The remainder is the
    count of pairs with same parity but different values.

Complexity:
    Time : O(N) per test case
    Space: O(N) for the frequency counter
"""


# --------------------------- Solution ----------------------------------


from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    freq = Counter(numbers)
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    total_pairs = even * (even - 1) // 2 + odd * (odd - 1) // 2
    same_value_pairs = 0
    for count in freq.values():
        same_value_pairs += count * (count - 1) // 2
    answer = total_pairs - same_value_pairs
    print(answer)
