"""
Problem: Alice's Sweets
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/alices-sweets-02b1336a/
Date: 2026-09-19
Difficulty: Medium
Topics: Binary Search, Sorting, Algorithms

Approach:
Sort each of the three candy-count arrays independently. Use a three-pointer
sweep: at each step, look at the current elements A[i], B[j], C[k] and track
the (max - min) spread among them, keeping the minimum spread seen. Advance
the pointer belonging to the current minimum value, since increasing it is
the only way to potentially shrink the spread further. This mimics the
classic "smallest range covering elements from k lists" technique.

Time Complexity: O(N log N) — dominated by sorting the three arrays.
Space Complexity: O(1) additional (in-place sort; pointers only).
"""


# --------------------------------- Solution ------------------------------------------


def minimumValue(N, A, B, C):
    A.sort()
    B.sort()
    C.sort()
    i = j = k = 0
    ans = float('inf')
    while i < N and j < N and k < N:
        a = A[i]
        b = B[j]
        c = C[k]
        mn = min(a, b, c)
        mx = max(a, b, c)
        ans = min(ans, 2 * (mx - mn))
        if mn == a:
            i += 1
        elif mn == b:
            j += 1
        else:
            k += 1
    return ans

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
out_ = minimumValue(N, A, B, C)
print(out_)
