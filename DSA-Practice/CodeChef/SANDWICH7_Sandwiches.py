"""
Problem   : Sandwiches (SANDWICH7)
Platform  : CodeChef, Starters 258
Link      : https://www.codechef.com/START258B/problems/SANDWICH7
Date      : 2026-09-30
Difficulty: Easy
Topics    : Math, Greedy

Approach  : Each sandwich needs 2 slices of bread and 1 filling (ham or cheese).
            Bread limits us to bread_count // 2 sandwiches, and fillings limit
            us to ham_count + cheese_count. The answer is the smaller of the two.

Complexity: Time  O(1)
            Space O(1)
"""


# ------------------------------------- Solution -----------------------------------------------


import sys

def fetch_input():
    data = sys.stdin.read().split()
    return data

def compute_result(vals):
    bread_count, ham_count, cheese_count = vals[0], vals[1], vals[2]
    fillings_available = ham_count + cheese_count
    bread_pairs = bread_count // 2
    result = bread_pairs if bread_pairs < fillings_available else fillings_available
    return result

def main():
    raw = fetch_input()
    nums = list(map(int, raw[:3]))
    ans = compute_result(nums)
    print(ans)

if __name__ == "__main__":
    main()
