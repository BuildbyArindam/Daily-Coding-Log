"""
Platform   : Code360 (Coding Ninjas)
Problem    : Largest Number in Binary Tree
Link       : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381524
Difficulty : Medium
Topics     : Binary Tree, Tree Traversal, Greedy, Sorting, Custom Comparator, Strings
Date       : 2026-10-02

Approach:
    1. Traverse the tree iteratively (stack-based DFS) and collect every
       node value as a string.
    2. Sort the strings with a custom comparator: a comes before b if
       a + b > b + a (concatenation order decides priority).
    3. Join the sorted strings. If the first character is '0', every value
       is 0, so return "0" to avoid a result like "000".

Time Complexity  : O(N + N log N * L), where N = number of nodes and
                   L = max digits in a value (each comparison costs O(L)).
Space Complexity : O(N * L) for the string list, plus O(H) for the stack,
                   where H is the tree height (O(N) worst case).
"""


# ------------------------------------------- Solution -----------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from functools import cmp_to_key

class BinaryTreeNode:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None

def printLargest(root):
    # Write your code here.
    if root is None:
        return ""
    values = []
    stack = [root]
    while stack:
        node = stack.pop()
        values.append(str(node.data))
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0
    values.sort(key=cmp_to_key(compare))
    result = "".join(values)
    if result and result[0] == '0':
        return "0"
    return result
