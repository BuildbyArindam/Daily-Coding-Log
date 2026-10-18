"""
Problem   : Shortest Path From 1 To n
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/shortest-path-from-1-to-n0156/1
Difficulty: Easy
Topics    : Mathematics, Graph, Shortest Path
Date      : 2026-10-18

Approach:
    From 1 the allowed moves are x -> x + 1 and x -> x * 3. Work backwards
    from n instead: if n is divisible by 3, divide by 3 (the biggest possible
    jump back toward 1); otherwise subtract 1. Count the steps until n == 1.
    Greedy works because dividing by 3 whenever possible never costs more
    steps than subtracting 1.

Complexity:
    Time : O(log n). Each division by 3 shrinks n sharply, and at most 2
           subtractions are needed between consecutive divisions.
    Space: O(1)
"""


# ----------------------------------------- Solution --------------------------------------------------------


class Solution:
    def minimumStep (self, n):
        # code here
        steps = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            steps += 1
        return steps
