"""
Problem   : Empty arrays
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/empty-array-31ed638c/
Difficulty: Easy
Topics    : Data Structures, Queues, Basics of Queues
Date      : 2026-09-29

Approach:
    Simulate the queue. For each target value in b (in order), find its
    position in a, rotate a so that value is at the front (cost = its index),
    then remove it (cost = 1). Repeat until a is empty.

Complexity (n = length of the array):
    Time  : O(n^2), since index(), slicing and pop(0) are each O(n) and run n times
    Space : O(n), since slicing creates a new list each iteration
"""


# ------------------------------------ Solution ---------------------------------------------


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
time = 0
while a:
    pos = a.index(b[0])
    a = a[pos:] + a[:pos]
    time += pos
    a.pop(0)
    b.pop(0)
    time += 1
print(time)
