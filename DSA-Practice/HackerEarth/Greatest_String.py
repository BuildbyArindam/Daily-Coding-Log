"""
Problem   : Greatest String
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/greatest-string-fcf3e37c/
Difficulty: Easy
Topic     : Basic Programming, Implementation, String Manipulation
Date      : 2026-08-16

Approach:
For each test case, read string s and integer Q (max allowed increments).
Scan s left to right; whenever a vowel is found, bump it to the next
character (e.g. 'a' -> 'b') and consume one unit of Q. Stop early once
Q hits 0 (greedy left-to-right consumption keeps leftmost vowels changed
first, which maximizes the resulting string lexicographically since
earlier-position increases dominate string comparison).

Time complexity : O(N) per test case, O(sum of N) overall
                   (single left-to-right scan, early break on Q == 0)
Space complexity : O(N) per test case (list conversion of the string)
"""


# ---------------------- Solution ---------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    vowels = {'a', 'e', 'i', 'o', 'u'}
    out = []
    for _ in range(T):
        s = list(data[idx])
        Q = int(data[idx + 1])
        idx += 2
        for i in range(len(s)):
            if Q == 0:
                break
            if s[i] in vowels:
                s[i] = chr(ord(s[i]) + 1)
                Q -= 1
        out.append("".join(s))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
