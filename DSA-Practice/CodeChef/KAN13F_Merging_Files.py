"""
Problem: Merging Files
Platform: CodeChef
Link: https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13F
Date Solved: 2026-09-27
Difficulty: Hard
Topics: Greedy, Heap/Priority Queue, K-way Merge

Approach:
Generalized Huffman-merge problem. When merging K files at a time (cost =
sum of sizes merged), pad the file list with dummy (0-length) files so that
(n - 1) % (K - 1) == 0 — this guarantees every merge step combines exactly K
files until only one remains, which is required for the greedy strategy to
be optimal. Then repeatedly pop the K smallest values from a min-heap, sum
them (adding to total cost), and push the merged value back, until one
element remains.

Time Complexity:  O(n log n) — each of the ~n/(K-1) merges does K heap pops
                   and 1 push, each O(log n).
Space Complexity: O(n) — heap holds the (padded) file list.
"""


# -------------------------------------- Solution -------------------------------------------------


import heapq
import sys

def pad_with_dummy_files(file_lengths, max_merge):
    count = len(file_lengths)
    remainder = (count - 1) % (max_merge - 1)
    if remainder != 0:
        extra_needed = (max_merge - 1) - remainder
        file_lengths = file_lengths + [0] * extra_needed
    return file_lengths

def compute_min_merge_cost(file_lengths, max_merge):
    working_set = pad_with_dummy_files(file_lengths, max_merge)
    heapq.heapify(working_set)
    total_cost = 0
    while len(working_set) > 1:
        group_size = min(max_merge, len(working_set))
        merged_value = 0
        for _ in range(group_size):
            merged_value += heapq.heappop(working_set)
        total_cost += merged_value
        heapq.heappush(working_set, merged_value)
    return total_cost

def run():
    data = sys.stdin.read().split()
    idx = 0
    test_count = int(data[idx]); idx += 1
    results = []
    for case_num in range(1, test_count + 1):
        n = int(data[idx]); k = int(data[idx + 1]); idx += 2
        lengths = [int(data[idx + i]) for i in range(n)]
        idx += n
        cost = compute_min_merge_cost(lengths, k)
        results.append(f"Case {case_num}: {cost}")
    print("\n".join(results))

if __name__ == "__main__":
    run()
