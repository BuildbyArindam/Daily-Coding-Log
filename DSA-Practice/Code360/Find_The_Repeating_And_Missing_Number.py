"""
Problem   : Find The Repeating And Missing Number
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/find-the-repeating-and-missing-number_1062727
Date      : 2026-08-30
Difficulty: Easy
Topics    : Arrays, Hashing, Frequency Counting

Approach:
    Build a frequency array of size (n+1) over the input (which should
    contain numbers 1..n but has one duplicate and one missing value).
    Scan 1..n: the number with freq == 2 is the repeating number,
    the number with freq == 0 is the missing number.

Time Complexity : O(n)   -> one pass to build freq, one pass to scan it
Space Complexity: O(n)   -> extra freq array of size n+1
                  (can be optimized to O(1) space using sum/sum-of-squares
                  math or XOR tricks — worth revisiting)
"""


# ---------------------- Solution ----------------------------


def findRepeatingAndMissingNumbers(nums):
    n = len(nums)
    freq = [0] * (n + 1)
    for num in nums:
        freq[num] += 1

    repeating = -1
    missing = -1
    for i in range(1, n + 1):
        if freq[i] == 2:
            repeating = i
        elif freq[i] == 0:
            missing = i

    return repeating, missing
