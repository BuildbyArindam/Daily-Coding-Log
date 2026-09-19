"""
Problem: Customer and Discount (Pirates and Swords)
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/pirates-and-swords-89e51e63/
Date Solved: 2026-09-19
Difficulty: Medium
Topics: Binary Search, Greedy Algorithms

Approach:
Sort both the customer budgets (arr) and item costs (cost). Binary search on
the answer k (number of customers served) — for a fixed k, greedily pair the
k cheapest costs with the k most expensive budgets (to make the shortfall as
small as possible) and check whether the total shortfall (sum of cost[i] -
arr[i] where positive) fits within the discount budget d. possible(k) is
monotonic in k, so binary search over k in [0, min(N, M)] finds the maximum
feasible k. Minimum spend is prefix_cost[k] - d, floored at 0.

Time Complexity: O((N + M) log(N + M)) for sorting + O(min(N,M) log(min(N,M)))
                 for the binary search (each possible(k) check is O(k))
Space Complexity: O(min(N, M)) for the prefix cost array
"""


# ------------------------------------ Solution -------------------------------------------


def maxCustomers(N, M, d, arr, cost):
    arr.sort()
    cost.sort()
    limit = min(N, M)
    prefix_cost = [0] * (limit + 1)
    for i in range(limit):
        prefix_cost[i + 1] = prefix_cost[i] + cost[i]
    def possible(k):
        start = N - k  
        required_discount = 0
        for i in range(k):
            diff = cost[i] - arr[start + i]
            if diff > 0:
                required_discount += diff
                if required_discount > d:
                    return False
        return True
    low, high = 0, limit
    while low < high:
        mid = (low + high + 1) // 2
        if possible(mid):
            low = mid
        else:
            high = mid - 1
    k = low
    minimum_spent = max(0, prefix_cost[k] - d)
    return [k, minimum_spent]

N, M, d = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))
out_ = maxCustomers(N, M, d, arr, cost)
print(' '.join(map(str, out_)))
