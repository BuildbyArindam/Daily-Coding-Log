"""
Problem   : Next Level (NLVEL)
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY023/problems/NLVEL
Date      : 2026-10-05
Difficulty: Easy
Topics    : Implementation, Math

Approach  : A level unlocks once the player has collected at least 60 stars.
            Integer division stars // 60 is > 0 exactly when stars >= 60,
            so the check reduces to one comparison. Print YES or NO.

Time      : O(1)
Space     : O(1)
"""


# ------------------------------------- Solution -------------------------------------------------


import sys

def can_unlock(stars, needed=60):
    return ("NO", "YES")[stars // needed > 0]

def main():
    data = sys.stdin.read().split()
    collected = int(data[0])
    sys.stdout.write(can_unlock(collected) + "\n")

if __name__ == "__main__":
    main()
