# Problem  : Maximum Value (MVALUE)
# Platform : CodeChef
# Link     : https://www.codechef.com/problems/MVALUE
# Date     : 2026-10-09
# Rating   : 1738
# Topics   : Math, Greedy, Arrays 
#
# Approach : Maximize A_i * A_j + |A_i - A_j| over pairs i != j.
#            The optimal pair is always either the two smallest values
#            (large positive product when both are negative) or the two
#            largest values. A mixed-sign pair gives at most 1, so it never
#            beats these. A single pass tracks the two smallest and two
#            largest values, then takes the max of both candidates.
#
# Time     : O(N) per test case
# Space    : O(1)


# ----------------------------------------- Solution --------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    for x in A:
        if x <= smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest:
            second_smallest = x
        if x >= largest:
            second_largest = largest
            largest = x
        elif x > second_largest:
            second_largest = x
    ans1 = smallest * second_smallest + abs(smallest - second_smallest)
    ans2 = largest * second_largest + abs(largest - second_largest)
    print(max(ans1, ans2))
