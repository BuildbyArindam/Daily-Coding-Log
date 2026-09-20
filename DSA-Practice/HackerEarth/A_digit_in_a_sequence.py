"""
Problem: A Digit in a Sequence
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/k-th-digit-fa018b0f/
Date: 2026-09-20
Difficulty: Medium
Topics: Implementation, Binary Search, Math

Approach:
Elements of the sequence (a, a+b, a+2b, ...) are grouped by digit-length,
since all numbers with the same number of digits contribute the same
digit-count each. For each digit-length group, compute how many terms of
the sequence fall in that range and how many total digits they contribute.
Skip whole groups by subtracting their digit count from k until the group
containing the k-th digit is found, then locate the exact term and digit
position within it via direct offset arithmetic.

Time Complexity: O(D) where D = number of digit-length groups spanned by
                  the sequence up to the term containing the k-th digit
                  (effectively O(log(max_value)) since digit-length grows
                  logarithmically)
Space Complexity: O(1)
"""


# ----------------------------------- Solution ---------------------------------------------


T = int(input())
for _ in range(T):
    a, b, k = map(int, input().split())
    start_index = 0
    while True:
        current = a + start_index * b
        digits = len(str(current))
        limit = 10 ** digits - 1
        last_index = (limit - a) // b
        if last_index < start_index:
            start_index += 1
            continue
        count = last_index - start_index + 1
        total_digits = count * digits
        if k > total_digits:
            k -= total_digits
            start_index = last_index + 1
        else:
            number_offset = (k - 1) // digits
            digit_position = (k - 1) % digits
            number = a + (start_index + number_offset) * b
            answer = str(number)[digit_position]
            print(answer)
            break
