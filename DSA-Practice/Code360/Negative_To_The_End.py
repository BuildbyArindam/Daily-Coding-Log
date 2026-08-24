"""
Problem   : Negative To The End
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/negative-to-the-end_7088763?kunjiRedirection=true
Date      : 2026-08-24
Difficulty: Easy
Topics    : Arrays, Two-Pointer / Partitioning

Approach  : Single pass, two auxiliary lists. Iterate once, bucket each
            element into `positive` or `negative` (non-positive) based on
            sign, then concatenate positive + negative. Preserves relative
            order within each group (stable partition).

Time      : O(n)  — one pass to bucket, O(n) to concatenate
Space     : O(n)  — two auxiliary lists of total size n
"""


# ----------------------- Solution ---------------------------


def negativeToTheEnd(v: [int]) -> [int]:
    positive = []
    negative = []
    for num in v:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)
    return positive + negative
