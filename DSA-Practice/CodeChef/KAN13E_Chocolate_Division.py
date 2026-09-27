"""
Problem: Chocolate Division
Platform: CodeChef
Link: https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13E
Date solved: 2026-09-27
Difficulty: Hard
Topics: Graph Theory, Split Graphs, Erdős–Gallai / Threshold Sequences, Greedy, Sorting

Approach:
    For each test case, build the degree sequence of the given graph.
    A graph is a "split graph" (can be partitioned into a clique + an
    independent set) iff, when degrees are sorted in non-increasing
    order d_1 >= d_2 >= ... >= d_n, and m is the largest index with
    d_m >= m - 1, the following holds:
        sum_{i=1}^{m} d_i  ==  m*(m-1) + sum_{i=m+1}^{n} d_i
    This is the Hammer–Ibarra-Simon / split-graph degree criterion.
    We compute prefix sums of the sorted degree sequence, find m via
    a single linear scan, then check the equality above.

Time complexity:  O(n log n) per test case (dominated by sorting degrees)
Space complexity: O(n) for the degree array and prefix sums
"""


# -------------------------------------- Solution ---------------------------------------------


import sys

def _read_all_tokens():
    data = sys.stdin.buffer.read().split()
    return iter(data)

def _next_int(token_iter):
    return int(next(token_iter))

def check_split_feasible(deg_seq):
    ordered = sorted(deg_seq, reverse=True)
    total = len(ordered)
    running_prefix = 0
    prefix_at = [0] * (total + 1)
    for idx in range(total):
        running_prefix += ordered[idx]
        prefix_at[idx + 1] = running_prefix
    threshold_m = 0
    for pos in range(1, total + 1):
        if ordered[pos - 1] >= pos - 1:
            threshold_m = pos
        else:
            continue
    left_side = prefix_at[threshold_m]
    right_side = threshold_m * (threshold_m - 1) + (prefix_at[total] - prefix_at[threshold_m])
    return left_side == right_side

def solve_one_case(token_iter):
    n_spheres = _next_int(token_iter)
    m_sticks = _next_int(token_iter)
    degree_of = [0] * (n_spheres + 1)
    for _ in range(m_sticks):
        u = _next_int(token_iter)
        v = _next_int(token_iter)
        degree_of[u] += 1
        degree_of[v] += 1
    verdict = check_split_feasible(degree_of[1:])
    return "YES" if verdict else "NO"

def main():
    tokens = _read_all_tokens()
    total_cases = _next_int(tokens)
    outputs = []
    for _ in range(total_cases):
        outputs.append(solve_one_case(tokens))
    sys.stdout.write("\n".join(outputs) + "\n")

if __name__ == "__main__":
    main()
