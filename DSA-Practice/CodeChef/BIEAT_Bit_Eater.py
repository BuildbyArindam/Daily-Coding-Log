"""
Problem   : Bit Eater
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BIEAT
Date      : 2026-09-09
Topics    : Bit Manipulation, Arrays
Difficulty: ~800-1000 (Beginner)

Approach:
    For each element in the array, perform a right bit-shift by M positions
    (equivalent to integer division by 2^M, discarding the lower M bits).
    Read N, read the array, read M, shift every element, print the result.

Complexity:
    Time  : O(N)      -- one shift operation per element
    Space : O(N)      -- storing the input array (O(1) extra space)
"""


# -------------------------- Solution ---------------------------------


N = int(input())
A = list(map(int, input().split()))
M = int(input())
for i in range(N):
    A[i] = A[i] >> M
print(*A)
