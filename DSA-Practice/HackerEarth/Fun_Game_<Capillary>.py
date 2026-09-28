"""
Problem   : Fun Game <Capillary>
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/
Difficulty: Easy
Topics    : Data Structures, Stacks, Queue
Date      : 2026-09-28

Approach  : Two pointers, one at each end of the array. Compare arr[a] and arr[b]:
            - arr[a] > arr[b]: record 1 and move the right pointer inward (b -= 1)
            - arr[a] < arr[b]: record 2 and move the left pointer inward (a += 1)
            - equal          : record 0 and move both pointers inward
            Repeat while both pointers are in range.

Time      : O(n), since every iteration moves at least one pointer
Space     : O(n) for the output list (O(1) extra beyond that)
"""


# --------------------------------------- Solution ------------------------------------------------


def funGame(arr):
    arr = list(arr)
    n = len(arr)
    a = 0
    b = n - 1 
    out = []
    while a < n and b >= 0:
        if arr[a] > arr[b]:
            out.append(1)
            b -= 1
        elif arr[a] < arr[b]:
            out.append(2)
            a += 1
        else:
            out.append(0)
            a += 1
            b -= 1
    return out

n = int(input())
arr = map(int, input().split())
out_ = funGame(arr)
print(' '.join(map(str, out_)))
