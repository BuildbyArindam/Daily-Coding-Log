"""
Problem   : Partitioning
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/
            basics-of-implementation/practice-problems/algorithm/partitioning-bd4c9574/
Difficulty: Easy
Topics    : Basic Programming, Basics of Implementation, Implementation
Date      : 2026-08-18

Approach:
- Convert C and P to their binary string forms (cb, pb). If either needs more
  than 25 bits, no valid partition can exist, so answer is 0.
- Build two helper arrays over the input binary string s:
    zero_before[i] -> length of the run of consecutive '0's ending
                       immediately before index i
    zero_after[i]  -> length of the run of consecutive '0's starting
                       at index i
- Slide over every position j where the substring s[j-LC:j] matches cb
  (i.e., a candidate spot where C's binary pattern ends):
    - left_ways: number of ways to extend that match backwards using the
      zero-run directly before it (extra leading-zero padding for C),
      capped so the padded length never exceeds 25 bits.
    - zeros = zero_after[j]: the zero-run right after the C match, treated
      as leading-zero padding for P.
    - Check that pb fits immediately after that zero run and matches
      exactly; if so it contributes right_ways = 1.
    - Add left_ways * right_ways to the running answer.
- Print the total number of valid partitions.

Time complexity : O(N) for the prefix/suffix zero arrays, plus O(N * 25)
                   for the scan (each candidate j does an O(LC)+O(LP)
                   slice comparison, LC, LP <= 25) -> effectively O(N)
Space complexity : O(N) for zero_before / zero_after arrays
"""


# --------------------- Solution ---------------------------


s = input().strip()
C, P = map(int, input().split())
N = len(s)
cb = bin(C)[2:]
pb = bin(P)[2:]
LC = len(cb)
LP = len(pb)
if LC > 25 or LP > 25:
    print(0)
    raise SystemExit
zero_before = [0] * (N + 1)
for i in range(1, N + 1):
    if s[i - 1] == '0':
        zero_before[i] = zero_before[i - 1] + 1
zero_after = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if s[i] == '0':
        zero_after[i] = zero_after[i + 1] + 1
answer = 0
for j in range(N + 1):
    if j < LC or s[j - LC:j] != cb:
        continue
    left_extra = min(zero_before[j - LC], 25 - LC)
    left_ways = left_extra + 1
    zeros = zero_after[j]
    if zeros + LP > N - j:
        continue
    start = j + zeros
    if zeros > 25 - LP:
        continue
    if start + LP > N or s[start:start + LP] != pb:
        continue
    right_ways = 1
    answer += left_ways * right_ways

print(answer)
