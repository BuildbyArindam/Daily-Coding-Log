"""
Problem   : Roy and Cipher Disk
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-cipher-disk/
Difficulty: Easy
Topic     : Ad-Hoc, Implementation, Data Structures
Date      : 2026-09-09

Approach:
  Simulate a rotating cipher disk with pointers 0-25 (a-z).
  For each character, compute the clockwise and anticlockwise
  distance from the current pointer to the target letter, and
  pick whichever is shorter (clockwise = positive, anticlockwise
  = negative). Update the pointer to the new position and repeat.

Time complexity : O(N) per test case, where N = len(string)
Space complexity: O(N) for the result list
"""


# ---------------------------- Solution ----------------------------------------


T = int(input())
for _ in range(T):
    s = input().strip()
    current = 0
    result = []
    for ch in s:
        target = ord(ch) - ord('a')
        clockwise = (target - current) % 26
        anticlockwise = (current - target) % 26
        if clockwise <= anticlockwise:
            move = clockwise
        else:
            move = -anticlockwise
        result.append(str(move))
        current = target
    print(" ".join(result))
