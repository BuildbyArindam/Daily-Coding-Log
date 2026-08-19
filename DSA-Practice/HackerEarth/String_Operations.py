"""
Problem   : String Operations
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/string-operations-1-cd102cb6/
Difficulty: Easy
Topic     : Basic Programming, Implementation, String Manipulation
Date      : 2026-08-19

Approach:
- Read the string, apply Q point-update operations (1-indexed -> convert to 0-indexed),
  join to get the string after updates (s_str).
- Apply M reverse-range operations on a copy of that string (1-indexed inclusive ranges),
  using slice reversal to get the final string (s_fin).
- Compare s_str and s_fin position-by-position to count how many characters
  stayed the same after the reversals.

Time complexity : O(N + Q + M * K)  where K is the average length of reversed ranges
                   (each reversal costs O(range length); everything else is O(1) or O(N)).
Space complexity: O(N) for the character lists.
"""


# --------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = list(input_data[0])
    ptr = 1
    q = int(input_data[ptr])
    ptr += 1
    for _ in range(q):
        ind = int(input_data[ptr]) - 1
        ch = input_data[ptr + 1]
        s[ind] = ch
        ptr += 2
    s_str = "".join(s)
    fin_list = list(s_str)
    m = int(input_data[ptr])
    ptr += 1
    for _ in range(m):
        a = int(input_data[ptr]) - 1
        b = int(input_data[ptr + 1]) - 1
        fin_list[a:b + 1] = fin_list[a:b + 1][::-1]
        ptr += 2
    s_fin = "".join(fin_list)
    same_count = sum(1 for c1, c2 in zip(s_str, s_fin) if c1 == c2)
    print(s_str)
    print(s_fin)
    print(same_count)

if __name__ == '__main__':
    solve()
