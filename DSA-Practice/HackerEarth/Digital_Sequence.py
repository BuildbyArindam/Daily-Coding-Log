"""
Problem   : Digital Sequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/digitial-sequence-ee0ea080/
Difficulty: Easy
Topic     : 1-D Array, Arrays, Data Structures
Date      : 2026-08-29

Approach:
For each number (given as a string), take its set of unique digits and
increment a global count for each distinct digit that appears in that
number. The answer is the digit with the highest count across all numbers
(i.e., the digit that appears in the most numbers, counted once per number).

Time complexity : O(N * L) where N = number of elements, L = avg string length
Space complexity: O(1) extra (fixed-size digit_counts array of 10)
"""


# ------------------------ Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = input_data[1:n + 1]
    digit_counts = [0] * 10
    for num_str in arr:
        unique_digits = set(num_str)
        for digit_char in unique_digits:
            digit = int(digit_char)
            digit_counts[digit] += 1
    print(max(digit_counts))

if __name__ == '__main__':
    solve()
