"""
Problem   : Random Generator
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/random-generator/
Difficulty: Medium
Topics    : Algorithms, Binary Search, Greedy, Sorting
Date      : 2026-10-09

Approach:
    Sort the array. Any group of K values that can be covered by a window of
    width 2P makes the answer "NO". In sorted order, the best candidate for
    such a group is K consecutive elements, so slide a window of size K and
    check arr[i + K - 1] - arr[i] <= 2 * P. If any window satisfies it,
    print "NO", otherwise "YES".

Complexity (per test case):
    Time  : O(N log N) for sorting + O(N) for the window scan
    Space : O(N) for the array (O(1) extra beyond the input)
"""


# -------------------------------------- Solution ----------------------------------------------------


T = int(input())

for _ in range(T):
    N, K, P = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    fails = False
    for i in range(N - K + 1):
        if arr[i + K - 1] - arr[i] <= 2 * P:
            fails = True
            break
    if fails:
        print("NO")
    else:
        print("YES")
