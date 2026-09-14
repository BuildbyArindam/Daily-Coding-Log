"""
Problem   : Ice Cream Flavours
Platform  : CodeChef (DSAMONDAY020)
Link      : https://www.codechef.com/DSAMONDAY020/problems/ICFLA
Date      : 2026-09-14
Difficulty: Hard
Topics    : Binary Search, Math/Combinatorics

Approach  :
    - We need the minimum number of ice cream balls (flavours) required
      so that the number of achievable unordered flavour-pairs is at
      least `target`.
    - Binary search on k (number of flavours) to find the largest k such
      that C(k, 2) = k*(k-1)/2 <= target. This gives the largest "full"
      set of flavours we can use without exceeding the target pair count.
    - Any remaining pairs needed (leftover_types) are covered by adding
      one extra ball per remaining pair, since each new single ball adds
      exactly one new achievable pair when combined with one existing one.
    - Answer = flavours used (k) + leftover balls needed.

Time complexity  : O(log(2 * 10^9)) per query  ->  effectively O(1)/O(log N)
Space complexity : O(1)
"""


# ---------------------------- Solution ---------------------------------------


import sys

def largest_k_within_budget(target: int) -> int:
    left, right = 1, 2 * 10 ** 9
    while left < right:
        mid = (left + right + 1) // 2
        pairs_possible = mid * (mid - 1) // 2
        if pairs_possible <= target:
            left = mid
        else:
            right = mid - 1
    return left

def minimum_balls_needed(types_wanted: int) -> int:
    flavours = largest_k_within_budget(types_wanted)
    already_covered = flavours * (flavours - 1) // 2
    leftover_types = types_wanted - already_covered
    return flavours + leftover_types

def main() -> None:
    raw = sys.stdin.read().strip()
    n = int(raw)
    print(minimum_balls_needed(n))

if __name__ == "__main__":
    main()
