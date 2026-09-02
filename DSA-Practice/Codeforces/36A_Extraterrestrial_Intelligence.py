"""
Problem   : Extra-terrestrial Intelligence
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/36/A
Difficulty: *1300
Date      : 2026-09-03
Topic     : Implementation

Approach:
    Collect the indices of all '1's in the binary string. If the signal
    is genuinely coming from evenly spaced antennas, these indices must
    form an arithmetic progression (constant gap between consecutive
    '1' positions). Compute the gap between the first two positions,
    then verify every subsequent consecutive pair matches that gap.

Time Complexity : O(n)      -> single pass to collect positions + single pass to verify
Space Complexity: O(k)      -> k = number of '1's stored in `positions`
"""


# --------------------------- Solution ------------------------------------


with open("input.txt", "r") as f:
    n = int(f.readline())
    s = f.readline().strip()
positions = []
for i in range(n):
    if s[i] == '1':
        positions.append(i)
distance = positions[1] - positions[0]
answer = "YES"
for i in range(2, len(positions)):
    if positions[i] - positions[i - 1] != distance:
        answer = "NO"
        break
with open("output.txt", "w") as f:
    f.write(answer)
