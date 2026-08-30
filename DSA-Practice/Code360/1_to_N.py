"""
Problem   : 1 to N
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/1-to-n_6682735?kunjiRedirection=true
Difficulty: Hard
Date      : 2026-08-30
Topics    : Greedy, Arrays, Sorting

Approach:
    Sort the array. Maintain `reach`, the largest value such that all
    integers in [1, reach] can currently be formed using array elements
    processed so far (plus added numbers). For each array element:
      - If it's <= reach + 1, it extends the reachable range without a gap
        (reach += arr[i]).
      - If it creates a gap (arr[i] > reach + 1), greedily insert the
        largest useful number, reach + 1, which doubles the reachable
        range (reach += reach + 1) and costs one insertion.
    Repeat until reach >= n (target range covered).

Time complexity : O(n log n)  -- dominated by the initial sort
Space complexity: O(1)        -- excluding sort's internal space
"""


# -------------------- Solution --------------------------


def minAdd(arr: list) -> int:
    arr.sort()
    n = len(arr)
    reach = 0
    added = 0
    i = 0
    while reach < n:
        if i < n and arr[i] <= reach + 1:
            reach += arr[i]
            i += 1
        else:
            reach += reach + 1
            added += 1
    return added
