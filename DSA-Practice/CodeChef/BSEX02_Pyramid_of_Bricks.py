"""
Problem   : Pyramid of Bricks
Platform  : CodeChef (DSAMONDAY023 / BSEX02)
Link      : https://www.codechef.com/DSAMONDAY023/problems/BSEX02
Date      : 2026-10-05
Difficulty: Medium
Topics    : Math, Triangular Numbers

Approach:
    A pyramid with k full layers needs k(k+1)/2 bricks. The answer is the
    largest k with k(k+1)/2 <= bricks. Solving the quadratic gives
    k ~ (sqrt(8n + 1) - 1) / 2. Using integer isqrt avoids float precision
    errors, and two small while-loops correct any off-by-one at the boundary.

Complexity:
    Time  : O(T) overall, O(1) per test case (isqrt on big ints is ~O(log n))
    Space : O(T) for storing the answers before printing
"""


# ------------------------------------ Solution ------------------------------------------------


from math import isqrt

def layers_for(bricks):
    guess = (isqrt(8 * bricks + 1) - 1) >> 1
    while guess * (guess + 1) // 2 > bricks:
        guess -= 1
    while (guess + 1) * (guess + 2) // 2 <= bricks:
        guess += 1
    return guess

def main():
    # Write your code here
    data = open(0).read().split()
    cases = int(data[0])
    answers = [layers_for(int(v)) for v in data[1:1 + cases]]
    print("\n".join(map(str, answers)))

if __name__ == "__main__":
    main()
