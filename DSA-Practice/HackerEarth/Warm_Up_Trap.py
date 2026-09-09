"""
Problem   : Warm-Up Trap
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/warm-up-trap/
Date      : 2026-09-09
Difficulty: Easy
Topic     : Number Theory (GCD)

Approach:
    Read N integers and compute the GCD of the entire array by
    iteratively applying math.gcd() to a running result, starting
    with the first element.

Time Complexity : O(N log(max(arr)))  -- each gcd() call is O(log(min(a,b)))
Space Complexity: O(N) for storing the array, O(1) extra
"""


# ------------------------- Solution ---------------------------------------


name = input() 
N = int(name)
import math
arr = list(map(int, input().split()))
gcd = arr[0]
for i in range(1, N):
    gcd = math.gcd(gcd, arr[i])
print(gcd)
