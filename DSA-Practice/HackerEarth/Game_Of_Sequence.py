"""
Problem   : Game of Sequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bracket-balancer-b9f56e12/
Date      : 2026-08-19
Difficulty: Easy
Topic     : Arrays, Basic Programming

Approach:
    The game reduces to removing duplicate values from the array one 
    at a time until all elements are unique. The number of moves 
    possible equals (count of distinct elements - 1), since players 
    alternately pick one occurrence of a repeated value to remove 
    until no duplicates remain. Whoever makes the last valid move wins.
    - If total_moves is odd  -> Q wins (second player made the last move)
    - If total_moves is even -> P wins (first player made the last move)

Time Complexity : O(N) per test case - building the set of elements
Space Complexity: O(N) - storing unique elements in a set
"""


# -------------------- Solution -------------------------


def find_the_winner(A):
    # Write your code here
    unique_count = len(set(A))
    total_moves = unique_count - 1
    if total_moves % 2 == 1:
        return 'Q'
    else:
        return 'P'

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        A = list(map(int, data[idx + 1: idx + 1 + n]))
        idx += 1 + n
        print(find_the_winner(A))

if __name__ == '__main__':
    main()
