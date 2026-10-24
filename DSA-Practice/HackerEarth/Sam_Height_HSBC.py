"""
Problem   : Sam Height <HSBC>
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/alice-and-marks-hsbc-b18d5d01/
Difficulty: Easy
Topics    : Algorithms, Implementation, Merge Sort, Sorting
Date      : 2026-10-24

Approach:
    For each test case, compare every height with Sam's height. Add 1 for
    each taller person and subtract 1 for each shorter one. The answer is the
    absolute value of that balance. Sorting (the merge-sort tag) isn't needed,
    since one linear scan gives the answer.

Complexity:
    Time  : O(N) per test case, O(sum of N) overall
    Space : O(N) per test case for the split line, O(1) beyond that
            (O(T) for the buffered output)
"""


# -------------------------------------------------- Solution -----------------------------------------------------------


import sys

def imbalance(sam_h, line):
    bal = 0
    for tok in line.split():
        h = int(tok)
        if h > sam_h:
            bal += 1
        elif h < sam_h:
            bal -= 1
    return abs(bal)

def run():
    rd = sys.stdin.readline
    cases = int(rd())
    out = []
    for _ in range(cases):
        head = rd().split()
        while not head:  
            head = rd().split()
        sam_h = int(head[1])
        out.append(imbalance(sam_h, rd()))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

if __name__ == "__main__":
    run()
