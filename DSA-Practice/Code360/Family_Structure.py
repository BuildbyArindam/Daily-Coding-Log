"""
Problem   : Family Structure
Platform  : Coding360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/family-structure_981243?kunjiRedirection=true
Date      : 2026-08-27
Difficulty: Easy
Topics    : Bit Manipulation, Recursion, Number Theory

Approach:
    The gender of the k-th child in the n-th generation depends only on
    the number of "1" bits in (k-1)'s binary representation. Each set
    bit represents a gender flip from the root (Male). If the count of
    such flips is even -> Male, if odd -> Female.

Time Complexity : O(log k)  -> bin(k-1) and bit counting take time
                                proportional to the number of bits in k.
Space Complexity: O(1)      -> no extra data structures used.
"""


# ------------------------ Solution ---------------------------


def kthChildNthGeneration(n, k):
    flips = bin(k - 1).count('1')
    if flips % 2 == 0:
        return "Male"
    else:
        return "Female"
