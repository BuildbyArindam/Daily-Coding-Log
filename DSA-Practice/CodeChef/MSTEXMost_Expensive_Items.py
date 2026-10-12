"""
Problem   : Most Expensive Items (MSTEX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MSTEX
Difficulty: 635
Date      : 2026-10-12
Topics    : Greedy, Heap, Sorting

Approach  : To maximise the total, take the k most expensive items.
            Use heapq.nlargest to pick the k largest prices and sum them.

Complexity: Time  - O(N log K) per test case
            Space - O(N) for the input list, O(K) extra for the heap
"""


# -------------------------------------------- Solution --------------------------------------------------


import sys
from heapq import nlargest

def best_total(prices, k):
    return sum(nlargest(k, prices))

def main():
    data = sys.stdin.read().split()
    ptr = 0
    tests = int(data[ptr])
    ptr += 1
    answers = []
    while tests:
        tests -= 1
        n = int(data[ptr])
        k = int(data[ptr + 1])
        ptr += 2
        prices = [int(x) for x in data[ptr:ptr + n]]
        ptr += n
        answers.append(best_total(prices, k))
    sys.stdout.write("\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    main()
