"""
Problem   : Monk and Nice Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/practice-problems/algorithm/monk-and-nice-strings-3/
Difficulty: Easy
Topics    : Sorting, Binary Search, Strings
Date      : 2026-10-22

Approach:
    The niceness of a string is the number of strictly smaller strings that
    appeared before it. Keep a sorted list of the strings seen so far. For
    each new string, bisect_left gives the count of strictly smaller strings
    (equal strings are not counted). Then insort places the string in order.

Complexity (N strings, max length L):
    Time : O(N log N * L) for the binary-search comparisons, plus O(N^2)
           worst-case for list insertion shifts (a fast memmove in practice).
    Space: O(N * L)
"""


# ---------------------------------------------- Solution --------------------------------------------------------------


from bisect import bisect_left, insort
import sys

def niceness_values(words):
    seen = []        
    result = []
    for w in words:
        result.append(bisect_left(seen, w)) 
        insort(seen, w)
    return result

def main():
    tokens = sys.stdin.read().split()
    count = int(tokens[0])
    words = tokens[1:1 + count]
    print("\n".join(map(str, niceness_values(words))))

if __name__ == "__main__":
    main()
