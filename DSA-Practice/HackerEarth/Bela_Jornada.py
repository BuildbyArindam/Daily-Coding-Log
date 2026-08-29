# Problem: Beautiful Journey
# Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/beautiful-journey-1/
# Platform: HackerEarth | Difficulty: Easy | Topic: Data Structures, One-dimensional
# Date: 2026-08-29
#
# Approach: Split the array at every possible index i (0..n-2) into a prefix
# [0..i] and suffix [i+1..n-1]. Track running prefix_sum and derive suffix_sum
# as total_sum - prefix_sum, then take the max of prefix_sum * suffix_sum
# across all split points.
#
# Time complexity: O(n) — single pass after computing total_sum
# Space complexity: O(n) — for storing the input array


# --------------------------- Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n + 1]]
    total_sum = sum(a)
    prefix_sum = 0
    max_product = 0
    for i in range(n - 1):
        prefix_sum += a[i]
        suffix_sum = total_sum - prefix_sum
        product = prefix_sum * suffix_sum
        if product > max_product:
            max_product = product
    print(max_product)

if __name__ == '__main__':
    solve()
