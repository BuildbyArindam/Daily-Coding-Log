"""
Problem   : XOR Equal (CodeChef)
Link      : https://www.codechef.com/problems/PALINT
Date      : 2026-10-08
Difficulty: 1731
Topics    : Hash Map, Bitwise XOR, Counting

Approach  : Applying XOR with X twice restores the original value, so each element
            can only ever be v or v ^ X. For a target value v, the elements equal
            to v already match, and the elements equal to v ^ X each need exactly
            one operation. Count frequencies, and for each distinct v take
            total = freq[v] + freq[v ^ X] and ops = freq[v ^ X]. Keep the maximum
            total, breaking ties by the fewest operations. If X == 0, no operation
            changes anything, so the answer is (max frequency, 0).

Time      : O(N) per test case
Space     : O(N)
"""


# --------------------------------------- Solution -----------------------------------------------------


import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        freq = Counter(A)
        if X == 0:
            mx = max(freq.values())
            print(mx, 0)
            continue
        max_equal = 0
        min_operations = N
        for v, c in freq.items():
            other = v ^ X
            total = c + freq.get(other, 0)
            operations = freq.get(other, 0)
            if total > max_equal:
                max_equal = total
                min_operations = operations
            elif total == max_equal:
                min_operations = min(min_operations, operations)
        print(max_equal, min_operations)

if __name__ == "__main__":
    solve()
