"""
Problem   : Sequence of points (Codeforces 24C)
Link      : https://codeforces.com/problemset/problem/24/C
Date      : 2026-08-27
Difficulty: 1800
Topic     : Geometry, Implementation, Math

Approach:
    M_i is the reflection of M_{i-1} about A_{(i-1) mod n}. Reflecting a
    point M about a center A gives M' = 2*A - M. Since n is odd, applying
    2n consecutive reflections returns to the original point (each pair
    of reflections about A_i and A_{i+1} is equivalent to a translation
    by 2*(A_{i+1} - A_i), and these 2n/2 = n translation vectors around
    the odd cycle sum to zero). So the sequence of points is periodic
    with period 2n, and we only need to simulate j mod (2*n) reflections
    instead of up to j directly (j can be as large as 1e18).

Complexity:
    Time : O(n) to read input + O(n) to simulate up to 2n reflections
           (since j mod 2n < 2n) => O(n) overall.
    Space: O(n) to store the points A[0..n-1].
"""


# -------------------------- Solution -------------------------


import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    j = int(data[1])
    mx = int(data[2])
    my = int(data[3])
    A = []
    idx = 4
    for _ in range(n):
        A.append((int(data[idx]), int(data[idx+1])))
        idx += 2
    k = j % (2 * n)
    for i in range(k):
        ax, ay = A[i % n]
        mx = 2 * ax - mx
        my = 2 * ay - my
    print(f"{mx} {my}")

if __name__ == '__main__':
    main()
