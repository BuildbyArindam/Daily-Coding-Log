"""
Problem   : Bubble Sort
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/bubble-sort-15-8064c987/
Date      : 2026-10-16
Difficulty: Easy
Topics    : Algorithms, Sorting, Bubble Sort, Fenwick Tree (BIT)

Approach:
    In each bubble sort pass, an element moves at most one position left,
    so the number of passes needed equals the largest count of bigger
    elements that appear before any single element. A Fenwick tree (BIT)
    over values 1..n gives that count for each element in O(log n):
    bigger_before = i - (number of earlier elements <= val).
    The answer is max(bigger_before) + 1, the extra pass being the one
    that confirms the array is sorted.

Complexity:
    Time  : O(n log n)  (vs O(n^2) for simulating bubble sort)
    Space : O(n)        (Fenwick tree)

Assumption: values lie in the range 1..n, as the BIT is indexed by value.
"""


# ----------------------------------------------- Solution -------------------------------------------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))
    tree = [0] * (n + 2)
    worst = 0
    for i, val in enumerate(arr):
        smaller_or_equal = 0
        j = val
        while j > 0:
            smaller_or_equal += tree[j]
            j -= j & -j
        bigger_before = i - smaller_or_equal
        if bigger_before > worst:
            worst = bigger_before
        j = val
        while j <= n:
            tree[j] += 1
            j += j & -j
    print(worst + 1)

solve()
