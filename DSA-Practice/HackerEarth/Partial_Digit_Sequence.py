"""
Problem: Partial Digit Sequence
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/partial-digit-sequence-34fa8391/
Difficulty: Easy
Topic: Basic Programming, Basics of Implementation, Implementation
Date Solved: 2026-08-17

Approach:
Treat this as a longest-chain / DAG-style DP over digits (0-9) instead of
over array indices. For each number, look at its set of unique digits and
find the best existing chain length among those digits (dp[digit]).
The current number extends that chain by 1. Update dp[digit] for every
digit present in the number to this new chain length (taking the max with
any existing value). The answer is the max value in dp after processing
all numbers.

Time Complexity: O(n * d), where n = number of elements, d = avg digits per number (d <= 10)
Space Complexity: O(1) extra (dp array is fixed size 10), O(d) per number for the digit set
"""


# ------------------------- Solution -------------------------


import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = input_data[1:n+1]
    dp = [0] * 10
    for num_str in arr:
        unique_digits = set(num_str)
        best_len = 0
        for ch in unique_digits:
            digit = int(ch)
            if dp[digit] > best_len:
                best_len = dp[digit]
        current_len = best_len + 1
        for ch in unique_digits:
            digit = int(ch)
            dp[digit] = max(dp[digit], current_len)
    print(max(dp))

if __name__ == '__main__':
    main()
