"""
Problem: Median Marks
Platform: Code360
Link: https://www.naukri.com/code360/problems/median-marks_5848799?kunjiRedirection=true
Difficulty: Hard
Date Solved: 2026-08-31
Topics: Binary Search, Greedy, Sorting, Arrays

Approach:
    Binary search on the answer (candidate median value m).
    For a fixed m, check feasibility greedily:
      - Students already at/above m via their minimum score l[i] count for free.
      - Students who can reach m within their range [l[i], r[i]] but aren't
        there yet incur a cost (m - l[i]) to raise them to m.
      - Sort these costs and greedily pay for the cheapest ones first until
        we have k = (n+1)//2 students at or above m, checking against the
        extra budget (x - sum(l)).
    Binary search over m in [0, max(r)] to find the largest feasible median.

Time Complexity:  O(n log n log(max(r)))
    - Binary search over the value range: O(log(max(r)))
    - Each feasibility check sorts costs: O(n log n)

Space Complexity: O(n) for the costs array per feasibility check
"""


# ------------------------------ Solution ------------------------------------


from typing import *

def medianMarks(x: int, l: List[int], r: List[int]) -> int:
    n = len(l)
    k = (n + 1) // 2
    base = sum(l)
    extra_budget = x - base
    def possible(m: int) -> bool:
        already = 0
        costs = []
        for i in range(n):
            if l[i] >= m:
                already += 1
            elif r[i] >= m:
                costs.append(m - l[i])
        need = k - already
        if need <= 0:
            return True
        if len(costs) < need:
            return False
        costs.sort()
        required = sum(costs[:need])
        return required <= extra_budget
    lo, hi = 0, max(r)
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer
