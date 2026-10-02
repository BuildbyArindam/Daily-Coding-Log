"""
Problem   : Candies
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/palindromic-substring-2-a3d45c46/
Date      : 2026-10-02
Topics    : Binary Search, Two Pointers, String Manipulation

Approach:
  For each query K, find the shortest substring of length >= K from which
  a palindrome of length K can be built.
  - A palindrome of length K needs K // 2 character pairs (plus one spare
    character if K is odd, which window length >= K guarantees).
  - Slide a window with two pointers, tracking per-character frequencies
    and the total pair count (a pair forms when a frequency becomes even).
  - Once the window is valid (length >= K and pairs >= K // 2), record its
    length and shrink from the left to look for a shorter one.
  - If K > n, the answer is -1; if no valid window exists, also -1.

Complexity (per query):
  Time  : O(n), since each pointer moves at most n times; O(T * n) overall
  Space : O(1), a fixed 26-entry frequency array
"""


# --------------------------------------- Solution -----------------------------------------


S = input().strip()
n = len(S)
T = int(input())
for _ in range(T):
    K = int(input())
    if K > n:
        print(-1)
        continue
    need_pairs = K // 2
    freq = [0] * 26
    pairs = 0
    left = 0
    best = n + 1
    for right in range(n):
        idx = ord(S[right]) - ord('a')
        freq[idx] += 1
        if freq[idx] % 2 == 0:
            pairs += 1
        while left <= right:
            window_len = right - left + 1
            if window_len >= K and pairs >= need_pairs:
                best = min(best, window_len)
                remove_idx = ord(S[left]) - ord('a')
                if freq[remove_idx] % 2 == 0:
                    pairs -= 1
                freq[remove_idx] -= 1
                left += 1
            else:
                break
    print(-1 if best == n + 1 else best)
