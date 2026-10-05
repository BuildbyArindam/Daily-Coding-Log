"""
Problem   : Superior Substring
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/superior-substring-dec-circuits-e51b3c27/
Difficulty: Medium
Topics    : Algorithms, Binary Search, Hash Maps, Searching, Sorting, String Manipulation
Date      : 2026-10-05

Approach:
    Find the longest substring in which some character occurs at least
    floor(len/2) times.
    1. If any character already has frequency >= n // 2, the whole string works.
    2. Otherwise, for a candidate character c, map it to +1 and every other
       character to -1. A substring qualifies iff its sum is >= -1.
    3. With prefix sums, for each end index i we need the earliest start k with
       prefix[k] <= prefix[i] + 1. Prefix sums move by +-1 from 0, so the first
       time each negative value is reached (stored in first[]) gives that k in O(1).
    4. Try characters in descending frequency order and stop early once
       2 * freq[c] + 1 <= best, since c cannot beat the current answer.

Complexity:
    Time  : O(26 * n) per test case, O(n) in the common case thanks to pruning.
    Space : O(n) for the first-occurrence array, plus O(26) for frequencies.
"""


# ------------------------------------- Solution ------------------------------------------------


import sys

def longest_for_char(s, target, n):
    first = [-1] * (n + 1)
    first[0] = 0
    prefix = 0
    ans = 0
    for j in range(n):
        if s[j] == target:
            prefix += 1
        else:
            prefix -= 1
        i = j + 1
        if prefix >= -1:
            if i > ans:
                ans = i
        else:
            start = first[-prefix - 1]

            if start != -1:
                length = i - start
                if length > ans:
                    ans = length
        if prefix < 0:
            x = -prefix
            if first[x] == -1:
                first[x] = i
    return ans

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    output = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        freq = [0] * 26
        for ch in s:
            freq[ch - 97] += 1
        if max(freq) >= n // 2:
            output.append(str(n))
            continue
        ans = 1
        order = sorted(range(26), key=freq.__getitem__, reverse=True)
        for c in order:
            if 2 * freq[c] + 1 <= ans:
                break
            length = longest_for_char(s, 97 + c, n)
            if length > ans:
                ans = length
            if ans == n:
                break
        output.append(str(ans))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
