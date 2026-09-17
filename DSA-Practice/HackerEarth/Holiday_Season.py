"""
Problem   : Holiday Season
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/holiday-season-ab957deb/
Date      : 2026-09-17
Difficulty: Medium
Topics    : Searching, DP, Prefix Counting

Approach:
  Count subsequences of length 4 matching pattern A-B-A-B (positions 1&3 same
  character, positions 2&4 same character) using layered prefix-count DP:
    - dp1[c]      : count of character c seen so far
    - dp2[a][b]   : count of "a...b" pairs (a before b) seen so far
    - dp3[a][b]   : count of "a...b...a" triples seen so far
  For each new character x at the current position:
    1. answer += sum(dp3[a][x] for a in 0..25)   -> extends every existing
       "a...b...a" triple with b == x into a full "a-x-a-x" quadruple
    2. dp3[x][b] += dp2[x][b] for all b            -> new triples ending in x
    3. dp2[a][x] += dp1[a] for all a                -> new pairs ending in x
    4. dp1[x] += 1

Time complexity : O(26 * n)  ->  O(n)
Space complexity: O(26^2)    ->  O(1) (fixed-size dp2/dp3 tables) + O(26) dp1
"""


# --------------------------------- Solution -----------------------------------------


n = int(input())
s = input().strip()
dp1 = [0] * 26
dp2 = [[0] * 26 for _ in range(26)]
dp3 = [[0] * 26 for _ in range(26)]
answer = 0
for ch in s:
    c = ord(ch) - ord('a')
    for a in range(26):
        answer += dp3[a][c]
    for b in range(26):
        dp3[c][b] += dp2[c][b]
    for a in range(26):
        dp2[a][c] += dp1[a]
    dp1[c] += 1
print(answer)
