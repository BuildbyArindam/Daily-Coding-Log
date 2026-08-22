"""
Problem: Optimization Game
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/optimization-game/
Date Solved: 2026-08-22
Difficulty: Easy
Topic: Implementation

Approach:
For each test case, iterate through the array while carrying forward the
"overflow" from each element the way binary addition propagates carry bits.
At each element, add the incoming carry to the current value, take mod 2 to
extract the bit contributed to the total, and integer-divide by 2 to compute
the new carry. After processing all elements, drain any remaining carry bit
by bit. The accumulated count of "1" bits produced this way is the answer
for that test case.

Time Complexity: O(N) per test case, O(sum of N) overall — single pass plus
                  O(log(carry)) drain step at the end, which is negligible.
Space Complexity: O(N) for storing the input array (O(1) extra beyond input).
"""


# ----------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    t = int(input_data[idx])
    idx += 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        total_sum = 0
        carry = 0
        for val in arr:
            current = val + carry
            total_sum += current % 2
            carry = current // 2
        while carry > 0:
            total_sum += carry % 2
            carry //= 2
        out.append(str(total_sum))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
