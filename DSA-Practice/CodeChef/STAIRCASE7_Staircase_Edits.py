"""
Problem   : Staircase Edits
Platform  : CodeChef (START258B)
Link      : https://www.codechef.com/START258B/problems/STAIRCASE7
Date      : 2026-09-30
Difficulty: Easy
Topics    : Hashing, Frequency Counting, Observation 

Approach  : The goal is to make the array a "staircase" where A[i] = A[0] + i.
            That holds exactly when A[i] - i is the same for every index.
            Compute d[i] = A[i] - i and count how often each value occurs.
            Elements sharing the most common d can stay untouched, so the
            minimum number of edits is N - (max frequency).

Time      : O(N) per test case (single pass with a hash map)
Space     : O(N) for the frequency map
"""


# ------------------------------------ Solution --------------------------------------------------


import sys
from collections import defaultdict

def run():
    fast_input = sys.stdin.buffer.read().split()
    ptr = 0
    t_cases = int(fast_input[ptr]); ptr += 1
    out_lines = []
    for _ in range(t_cases):
        n_val = int(fast_input[ptr]); ptr += 1
        arr = fast_input[ptr:ptr + n_val]
        ptr += n_val
        diff_counts = defaultdict(int)
        best_freq = 0
        idx = 0
        while idx < n_val:
            current_diff = int(arr[idx]) - idx
            diff_counts[current_diff] += 1
            if diff_counts[current_diff] > best_freq:
                best_freq = diff_counts[current_diff]
            idx += 1
        result = n_val - best_freq
        out_lines.append(str(result))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    run()
