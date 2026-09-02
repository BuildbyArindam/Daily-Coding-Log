# Problem: Sort String
# Platform: HackerEarth
# Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/sort-string-2-18accdb0/
# Difficulty: Easy
# Topic: Algorithms, Greedy, Linear Search
# Date: 2026-09-02
#
# Approach:
# We want the minimum number of swaps to sort a binary string so all 0s
# come before all 1s. Equivalently, we choose a split point p: positions
# [0, p) should be all 0s and [p, N) should be all 1s. For each split
# point, mismatches = (1s in the prefix) + (0s in the suffix). Swapping
# a mismatched 1 with a mismatched 0 fixes both at once, so the answer
# for a given split is mismatches // 2. We scan all N+1 split points,
# maintaining prefix_ones and suffix_zeros incrementally (O(1) update
# per step), and take the minimum. The parity check (N - p) % 2 ==
# total_ones % 2 restricts to splits where the suffix length has the
# same parity as total_ones (this mirrors the fact that valid target
# arrangements must be reachable — filters splits, doesn't change
# complexity).
#
# Time Complexity: O(N) per test case  ->  O(sum(N)) overall
# Space Complexity: O(1) extra (excluding input storage)


# ------------------------ Solution ----------------------------


name = input()             
T = int(name)
answers = []
for _ in range(T):
    N = int(input())
    S = input().strip()
    total_ones = S.count('1')
    prefix_ones = 0
    suffix_zeros = N - total_ones
    min_mismatches = float('inf')
    for p in range(N + 1):
        if (N - p) % 2 == total_ones % 2:
            mismatches = prefix_ones + suffix_zeros
            min_mismatches = min(min_mismatches, mismatches)
        if p < N:
            if S[p] == '1':
                prefix_ones += 1
            else:
                suffix_zeros -= 1
    answers.append(str(min_mismatches // 2))
print('\n'.join(answers))
