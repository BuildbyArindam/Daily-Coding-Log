"""
Problem   : Count Even Odd
Platform  : CodeChef (via Code360)
Link      : https://www.naukri.com/code360/problems/count-even-odd_757508?kunjiRedirection=true
Date      : 2026-09-06
Difficulty: Easy
Topics    : Hashing, Frequency Counting, Arrays

Approach:
    - Build a frequency map of all elements using collections.Counter.
    - For each distinct element's frequency, check parity:
        - even frequency -> increment 'even' counter
        - odd frequency  -> increment 'odd' counter
    - Return [odd_count, even_count].

Time Complexity : O(N) per test case (Counter build + single pass over freq map)
Space Complexity: O(N) for the frequency map in the worst case (all distinct elements)
"""


# ------------------------ Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def countEvenOdd(arr, n):
    freq = Counter(arr)
    odd = 0
    even = 0
    for count in freq.values():
        if count % 2 == 0:
            even += 1
        else:
            odd += 1
    return [odd, even]
def printAns(ans):
    print(ans[0], end=" ")
    print(ans[1])
def takeInput() :
    n = int(input().strip())
    if n == 0 :
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n
t = int(input().strip())
for i in range(t) :
    arr, n= takeInput()
    ans = countEvenOdd(arr,n)
    printAns(ans)
