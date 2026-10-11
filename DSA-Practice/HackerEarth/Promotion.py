# =============================================================================
# Problem   : Promotion
# Platform  : HackerEarth 
# Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/promotion-1/
# Date      : 2026-10-11
# Difficulty: Medium
# Topics    : Binary Search, Greedy, Sorting, Math
#
# Approach  : Binary search on the answer (total time t).
#             - Time t allows k = (t + 1) // 2 trips per carrier.
#             - Sort weights and capacities in descending order. If the heaviest
#               item exceeds the largest capacity, the answer is -1.
#             - Feasibility check: give each carrier, strongest first, up to k of
#               the heaviest remaining items it can carry. Since weights are
#               descending, if a carrier can lift the next item it can lift all
#               later ones, so it takes exactly k items (or whatever is left).
#             - If all n items are delivered, t is feasible. Search lo=1, hi=2n-1
#               for the smallest feasible t.
#
# Time      : O(n log n + m log m) for sorting + O((n + m) log n) for the search
# Space     : O(n + m)
# =============================================================================


# -------------------------------------------- Solution ----------------------------------------------


n, m = map(int, input().split())
weights = list(map(int, input().split()))
capacity = list(map(int, input().split()))

weights.sort(reverse=True)
capacity.sort(reverse=True)

if weights[0] > capacity[0]:
    print(-1)
else:
    usable = [c for c in capacity if c >= weights[-1]]
    def possible(t):
        trips = (t + 1) // 2
        delivered = 0
        for c in usable:
            while delivered < n and weights[delivered] <= c:
                delivered += 1
                if delivered % trips == 0:
                    break
        return delivered == n
    lo, hi = 1, 2 * n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)
