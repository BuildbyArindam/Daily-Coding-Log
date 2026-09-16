"""
Problem   : Sharing Cookies
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/SHARING
Date      : 2026-09-16
Difficulty: Beginner (~800-1000, unconfirmed - verify on problem page)
Topics    : Basic Math, Ad-hoc

Approach:
    Alice and Bob have alice_count and bob_count cookies respectively.
    For an equal split, total cookies must be even; if odd, output -1.
    Otherwise, target = total // 2, and the number Alice must give
    (or receive, if negative) is simply alice_count - target.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------------- Solution ------------------------------------------


def fetch_input():
    raw = input().split()
    return int(raw[0]), int(raw[1])

def compute_share(alice_count, bob_count):
    combined = alice_count + bob_count
    if combined % 2 != 0:
        return -1
    target = combined // 2
    diff = alice_count - target
    return diff

def main():
    a_val, b_val = fetch_input()
    result = compute_share(a_val, b_val)
    print(result)

if __name__ == "__main__":
    main()
