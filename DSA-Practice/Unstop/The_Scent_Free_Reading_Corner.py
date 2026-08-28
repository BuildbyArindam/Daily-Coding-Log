"""
Problem: The Scent-Free Reading Corner
Platform: Unstop
Link: https://unstop.com/code/practice/657851
Date: 2026-08-28
Difficulty: Medium
Topics: Sliding Window, Two Pointers, Hash Map, Frequency Counting, Subarray

Approach:
Variable-size sliding window with a frequency map tracking distinct values
in the current window. Expand `right` each step, incrementing the count for
arr[right]. Whenever the number of distinct elements exceeds k, shrink from
`left` until distinct <= k again, decrementing/removing counts as needed.
Track the max window length (right - left + 1) seen at each step — this
gives the longest subarray containing at most k distinct values.

Time Complexity: O(n) — each index enters/leaves the window at most once
Space Complexity: O(k) — frequency map holds at most k+1 distinct values
"""


# ---------------------------- Solution -------------------------------------


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = map(int, input().split())
arr = list(map(int, input().split()))
freq = {}
left = 0
distinct = 0
max_len = 0
for right in range(n):
    value = arr[right]
    if value not in freq:
        freq[value] = 0
        distinct += 1
    freq[value] += 1
    while distinct > k:
        left_value = arr[left]
        freq[left_value] -= 1
        if freq[left_value] == 0:
            del freq[left_value]
            distinct -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)
