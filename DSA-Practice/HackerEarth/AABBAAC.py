"""
Problem   : AABBAAC
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/aabbaac/
Difficulty: Medium
Topics    : Approved, Implementation, Open, String Manipulation

Approach:
  Each string S[i] (i > 0) implicitly represents a much longer string built
  as: rev(virtual_string(i-1)) + virtual_string(i-1) + S[i]
  (i.e. length doubles via a mirrored copy of the previous level, plus the
  new literal chars). Rather than materializing this recursively-doubling
  string, precompute cumulative lengths[i] = 2*lengths[i-1] + len(S[i]).
  For each query index x, walk down from level N-1 to 1: if x falls in the
  literal S[i] segment, answer directly; if it falls in the mirrored half,
  reflect x; otherwise recurse into the smaller previous level. Falls
  through to S[0][x] at the base case.

Complexity:
  Time : O(N) per query -> O(N*M) total per test case (each query walks at
         most N levels down).
  Space: O(N) for the lengths array (excluding O(total input length) for
         storing the strings themselves).
"""


# ----------------------------- Solution -----------------------------------


name = input() 
T = int(name)
answers = []
for _ in range(T):
    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    lengths = [0] * N
    lengths[0] = len(S[0])
    for i in range(1, N):
        lengths[i] = 2 * lengths[i - 1] + len(S[i])
    result = []
    for _ in range(M):
        x = int(input())
        for i in range(N - 1, 0, -1):
            prev_len = lengths[i - 1]
            if x < prev_len:
                pass
            elif x < 2 * prev_len:
                x = 2 * prev_len - 1 - x
            else:
                x -= 2 * prev_len
                result.append(S[i][x])
                break
        else:
            result.append(S[0][x])
    answers.append(''.join(result))
print('\n'.join(answers))
