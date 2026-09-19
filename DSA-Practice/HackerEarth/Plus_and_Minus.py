"""
Problem: Plus and Minus
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/plus-and-minus-0f3ab24f/
Date Solved: 2026-09-19
Difficulty: Medium
Topics: Binary Search, Algorithms

Approach:
Given a shuffled array that should contain two "seed" values (a1, a2) followed
by a Fibonacci-like sequence built from them (with some values appearing twice
depending on position), reverse-engineer the seeds by sorting the array and
working backwards from the two largest elements using subtraction (the inverse
of Fibonacci addition). Reconstruct the expected multiset of values from the
recovered seeds and verify it matches the given array exactly (accounting for
duplicated entries near the middle of the sequence).

Time Complexity: O(n log n) — dominated by sorting the array.
Space Complexity: O(n) — storing the array and the reconstructed "small"/sequence lists.
"""


# ---------------------------------- Solution -----------------------------------------------------


import sys

def possible(arr):
    n = len(arr)
    k = n // 2 - 1
    arr.sort()
    x = arr[-1]  
    y = arr[-2]   
    for _ in range(k - 1):
        if x < y:
            return False, 0, 0
        x, y = y, x - y
    a1 = y
    a2 = x - y
    if a1 < a2 or a2 < 0:
        return False, 0, 0
    pos = 0
    small = [a2, a1 - a2]
    if k >= 2:
        small.append(a2)
    small.sort()
    for v in small:
        if pos >= n or arr[pos] != v:
            return False, 0, 0
        pos += 1
    p0 = a1
    p1 = a1 + a2
    for i in range(k + 1):
        if i == 0:
            p = p0
        elif i == 1:
            p = p1
        else:
            p0, p1 = p1, p0 + p1
            p = p1
        count = 2 if k >= 3 and i <= k - 3 else 1
        for _ in range(count):
            if pos >= n or arr[pos] != p:
                return False, 0, 0
            pos += 1
    if pos != n:
        return False, 0, 0
    return True, a1, a2

def main():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ok, a1, a2 = possible(arr)
        if ok:
            out.append("YES")
            out.append(f"{a1} {a2}")
        else:
            out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
