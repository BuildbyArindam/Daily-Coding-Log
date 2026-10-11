"""
Problem   : Double or Append (DOUBLEARR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DOUBLEARR
Difficulty: 1811
Topics    : Math, Combinatorics 
Date      : 2026-10-11

Approach:
  Track three values instead of building the array:
    length - current array length
    inv    - current inversion count (printed after every operation)
    cross  - cross-pair term used when the array is doubled
  Op 1 (append): inv += length, cross += length, length += 1
  Op 2 (double): inv = 2*inv + cross, cross *= 4, length *= 2
  Each operation is an O(1) update, and inv is recorded after each one.

Complexity (per test case, M = number of operations):
  Time : O(M) arithmetic operations
  Space: O(M) for the output list
  Note : no modulo is applied, so values grow exponentially. Python big ints
         handle this, but the real cost is higher than O(M) bit-operations.
         If the statement asks for a modulo, apply it after each update.
"""


# --------------------------------------------- Solution ---------------------------------------------------


T = int(input())

for _ in range(T):
    M = int(input())
    ops = list(map(int, input().split()))
    length = 1
    inv = 0
    cross = 0
    ans = []
    for t in ops:
        if t == 1:
            inv += length
            cross += length
            length += 1
        else:
            inv = 2 * inv + cross
            cross *= 4
            length *= 2
        ans.append(inv)
    print(*ans)
