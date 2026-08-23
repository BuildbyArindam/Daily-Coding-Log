"""
Problem: In an Array
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/in-an-array-9fbe4c12/
Difficulty: Easy
Topic: 1-D Array, Arrays, Data Structures
Date: 2026-08-23

Approach:
Count pairs (i, j) with i < j such that (A[i] + A[j]) % K == X and
(A[i] * A[j]) % K == Y. Group values by frequency using a Counter, then
compare each pair of DISTINCT values once (multiplying by their frequencies
to account for duplicates), and separately handle pairs formed from two
equal values using nC2 = f*(f-1)/2.

Time Complexity: O(D^2) where D = number of distinct values in A (worst case O(N^2) if all elements are distinct)
Space Complexity: O(D) for the frequency counter
"""


# --------------------------- Solution -----------------------------


from collections import Counter
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    X = int(data[2])
    Y = int(data[3])
    A = list(map(int, data[4 : 4 + N]))
    freq = Counter(A)
    unique_vals = list(freq.keys())
    count = 0
    for i in range(len(unique_vals)):
        v1 = unique_vals[i]
        for j in range(i + 1, len(unique_vals)):
            v2 = unique_vals[j]
            if (v1 + v2) % K == X and (v1 * v2) % K == Y:
                count += freq[v1] * freq[v2]
    for v in unique_vals:
        if (2 * v) % K == X and (v * v) % K == Y:
            count += (freq[v] * (freq[v] - 1)) // 2
    print(count)

if __name__ == "__main__":
    solve()
