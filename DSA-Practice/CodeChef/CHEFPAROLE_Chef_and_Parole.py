"""
Problem   : Chef and Parole
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHEFPAROLE
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Chef is granted parole if he has served X years, with the cutoff
    being 7 years. Simple threshold check: if X >= 7, print "Yes",
    otherwise print "No".

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# --------------------- Solution ----------------------------


X = int(input())
if X >= 7:
    print("Yes")
else:
    print("No")
