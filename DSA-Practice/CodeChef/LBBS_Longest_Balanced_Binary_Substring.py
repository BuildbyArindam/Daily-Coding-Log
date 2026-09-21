"""
Problem   : Longest Balanced Binary Substring
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY021/problems/LBBS
Difficulty: Medium
Topics    : Prefix Sums, Hashing, Sliding Window / Two Pointers, Array Manipulation
Date      : 2026-09-21

Approach  :
  - Convert the binary string into a running "balance" prefix sum,
    treating '1' as +1 and '0' as -1.
  - For every pair of indices (start, end), the substring is valid if
    its length is even AND the absolute difference of prefix sums
    (imbalance) is within 2 * limit.
  - Brute force over all (start, end) pairs, tracking the max valid
    even-length span.

Complexity:
  Time  : O(n^2)  — nested loop over all substrings
  Space : O(n)    — prefix sum array
"""


# ------------------------------------------- Solution ------------------------------------------------


import sys

def read_input():
    data = sys.stdin.read().split()
    text = data[0]
    limit = int(data[1])
    return text, limit

def diff_prefix(text):
    running = 0
    prefix = [0]
    for ch in text:
        running += 1 if ch == '1' else -1
        prefix.append(running)
    return prefix

def best_length(text, limit):
    n = len(text)
    prefix = diff_prefix(text)
    answer = 0
    for start in range(n):
        for end in range(start + 1, n + 1):
            span = end - start
            if span % 2 != 0:
                continue
            imbalance = abs(prefix[end] - prefix[start])
            if imbalance <= 2 * limit and span > answer:
                answer = span
    return answer

def main():
    text, limit = read_input()
    print(best_length(text, limit))

if __name__ == "__main__":
    main()
