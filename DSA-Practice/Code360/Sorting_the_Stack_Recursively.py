"""
Problem   : Sorting the Stack Recursively
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/sorting-the-stack-recursively_1868989
Date      : 2026-08-23
Difficulty: Easy
Topics    : Recursion, Stacks

Approach:
    Recursively pop all elements off the stack until it's empty (base case).
    As the recursion unwinds, insert each popped element back into its
    correct sorted position using a helper function `insertSorted`, which
    itself recursively pops elements greater than the current value,
    inserts, then pushes them back.

Time complexity : O(n^2)  — each of the n insertions can take O(n) pops/pushes
Space complexity: O(n)    — recursion call stack depth (both functions combined)
"""


# ---------------------------- Solution --------------------------------


def sortStack(s):
    if len(s) <= 1:
        return s
    top = s.pop()
    sortStack(s)
    insertSorted(s, top)
    return s


def insertSorted(s, x):
    if not s or s[-1] <= x:
        s.append(x)
        return
    top = s.pop()
    insertSorted(s, x)
    s.append(top)
