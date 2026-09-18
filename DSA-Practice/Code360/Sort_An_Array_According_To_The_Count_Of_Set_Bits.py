"""
Problem   : Sort An Array According To The Count Of Set Bits
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382140
Date      : 2026-09-18
Difficulty: Medium
Topics    : Bit Manipulation, Sorting, Set Bits Count

Approach:
    For each element, count its set bits using bin(x).count('1'),
    then sort the array in descending order of set-bit count.
    Python's sort is stable, so elements with equal set-bit counts
    retain their original relative order.

Time Complexity : O(n log n) — n for computing set bits per element
                   (each count is O(log(max_val))), dominated by the
                   O(n log n) sort itself.
Space Complexity: O(n) — auxiliary space used by Timsort.
"""


# ------------------------------ Solution -----------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)

def sortSetBitsCount(arr, size):
    arr[:] = sorted(arr, key=lambda x: bin(x).count('1'), reverse=True)

def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr

tc = int(input())
while tc > 0:
    N, arr = takeInput()
    sortSetBitsCount(arr, N)
    for i in arr:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
