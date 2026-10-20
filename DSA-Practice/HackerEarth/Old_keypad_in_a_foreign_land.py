"""
Problem   : Old keypad in a foreign land
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/practice-problems/algorithm/old-keypad-in-a-foreign-land-24/
Date      : 2026-10-20
Difficulty: Medium
Topics    : Greedy, Sorting

Approach  : Greedy. A key with size s gives 1 press to its first character,
            2 to its second, and so on. Sort frequencies in descending order
            and fill the cheapest slots first, one "press level" at a time
            across all keys. Keys that are full are skipped. If the total
            capacity is below N, the answer is -1.

Time      : O(N log N + N*K) worst case (sort, plus up to N passes over K keys)
Space     : O(N + K)
"""


# ------------------------------------------------------ Solution ----------------------------------------------------------------


N = int(input())
frequencies = list(map(int, input().split()))
K = int(input())
keySize = list(map(int, input().split()))
if sum(keySize) < N:
    print(-1)
else:
    frequencies.sort(reverse=True)
    keystrokes = 0
    position = 0
    presses = 1
    while position < N:
        for i in range(K):
            if position < N and keySize[i] > 0:
                keystrokes += frequencies[position] * presses
                position += 1
                keySize[i] -= 1
        presses += 1
    print(keystrokes)
