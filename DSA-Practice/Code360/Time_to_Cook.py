"""
Problem   : Time to Cook
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/time-to-cook_2538043?kunjiRedirection=true
Difficulty: Easy
Topics    : Arrays, Hashing/Frequency Counting, Simulation
Date      : 2026-08-30

Approach:
  - For each order (food_id, amount), accumulate total quantity ordered
    per dish using a frequency array `quantity` of size n.
  - For each dish i, compute total_time = quantity[i] * time[i]
    (time to cook all units of that dish, since units are cooked one after another).
  - Track the dish with the maximum total_time; that dish finishes last,
    so its 1-indexed id is the answer.

Time Complexity : O(n + m)  where n = number of dishes, m = number of orders
Space Complexity: O(n)      for the quantity array
"""


# ------------------------ Solution -------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *
from builtins import open

def timeToCook(time: List[int], order: List[List[int]]) -> int:
    n = len(time)
    quantity = [0] * n
    for food_id, amount in order:
        quantity[food_id - 1] += amount
    max_time = -1
    answer = 1
    for i in range(n):
        total_time = quantity[i] * time[i]
        if total_time > max_time:
            max_time = total_time
            answer = i + 1
    return answer
