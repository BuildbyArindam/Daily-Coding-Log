"""
Problem: Swap
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/swap_7118168?kunjiRedirection=true
Difficulty: Hard
Date solved: 2026-09-02
Topics: Greedy, Permutation, Constructive Algorithms, Sorting

Approach:
- For each pair (x, y) in a/b: if y != 0, position x is forced to value y
  (must satisfy y >= x - k, else impossible; also reject duplicate y's).
- Positions with y == 0 are free slots to be filled with the remaining
  unused values, each also constrained to be >= x - k.
- Process free positions from largest x to smallest. For each, count how
  many still-unused values v >= (x - k) remain (via a suffix count array
  over "used"), subtract values already committed to a later-processed
  (larger x) free position, and multiply that count into the answer.
- This greedy ordering works because a value usable for a smaller x
  (tighter/looser bound) is also usable for larger x's threshold in the
  order processed, so counting "choices remaining" suffix-wise is valid.

Time complexity: O(n) per test case (single pass + suffix array build)
Space complexity: O(n) for used/is_zero/suffix arrays
"""


# -------------------------- Solution ----------------------------------


MOD = 10**9 + 7

def numberOfWays(n: int, k: int, a: list, b: list) -> int:
    used = [False] * (n + 1)
    is_zero = [False] * (n + 1)
    for x, y in zip(a, b):
        if y == 0:
            is_zero[x] = True
        else:
            if used[y]:
                return 0
            used[y] = True
            if y < x - k:
                return 0
    suffix = [0] * (n + 2)
    for v in range(n, 0, -1):
        suffix[v] = suffix[v + 1] + (0 if used[v] else 1)
    ans = 1
    assigned = 0
    for x in range(n, 0, -1):
        if not is_zero[x]:
            continue
        low = max(1, x - k)
        choices = suffix[low] - assigned
        if choices <= 0:
            return 0
        ans = (ans * choices) % MOD
        assigned += 1
    return ans

def main():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(numberOfWays(n, k, a, b))

if __name__ == "__main__":
    main()
