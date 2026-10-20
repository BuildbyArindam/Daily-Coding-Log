"""
Platform   : CodeChef
Problem    : Chef and Secret Password (SECPASS)
Link       : https://www.codechef.com/problems/SECPASS
Difficulty : 2007
Date       : 2026-10-20
Topics     : Strings, Z-Algorithm, Prefix Counting

Approach:
    1. Build the Z-array of the string. z[i] is the length of the longest
       common prefix between s and s[i:], and z[0] is set to n.
    2. A prefix of length L occurs at position i exactly when z[i] >= L, so
       the number of occurrences of the length-L prefix equals the count of
       indices with z[i] >= L. Count how many times each z-value appears,
       then take a suffix sum to get occurrences for every L.
    3. Scan lengths 2..n and keep the length with the highest occurrence
       count. Using ">=" means ties go to the longer prefix.

Complexity:
    Time  : O(n) per test case (Z-function + counting + one scan)
    Space : O(n) for the Z-array and frequency array
"""


# ----------------------------------------------------- Solution ----------------------------------------------------------


def z_function(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    z[0] = n
    return z

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        z = z_function(s)
        freq = [0] * (n + 1)
        for value in z:
            freq[value] += 1
        for length in range(n - 1, 0, -1):
            freq[length] += freq[length + 1]
        best_length = 1
        for length in range(2, n + 1):
            if freq[length] >= freq[best_length]:
                best_length = length
        print(s[:best_length])

if __name__ == "__main__":
    solve()
