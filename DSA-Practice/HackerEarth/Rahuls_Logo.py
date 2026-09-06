"""
Problem   : Rahul's Logo
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/rahuls-logo/
Difficulty: Easy
Topics    : Algorithms, Basic Programming, Implementation
Date      : 2026-09-06

Approach:
    Build the logo as two nested diamond patterns (size n and n+1) drawn
    onto a 2D character canvas. make_diamond() recursively draws concentric
    diamond rings using '/' and '\' edges that alternate direction and
    swap character sides once the ring's midpoint (cur == size-1) is
    reached, then recurses inward on a shrunk sub-diamond (size - 2) two
    rows down until size <= 0. print_logo() sizes the canvas, fills it,
    then prints each row with trailing spaces stripped.

Time complexity : O(n^2)  — each of the O(n) concentric rings touches
                   O(n) cells, and the canvas itself is O(n) x O(n).
Space complexity: O(n^2)  — full character canvas held in memory.
"""


# ------------------------ Solution --------------------------------


name = input() 
n = int(name)

def make_diamond(canvas, row, col, size):
    if size <= 0:
        return
    front = col
    back = col + 1
    directions = [-1, 1]
    chars = ['/', '\\']
    cur = 0
    left_char = 0
    right_char = 1
    offset = 0
    while front < back:
        canvas[row + cur][front + offset] = chars[left_char]
        canvas[row + cur][back + offset] = chars[right_char]
        if cur == size - 1:
            left_char, right_char = right_char, left_char
            cur += 1
            offset = 2
            canvas[row + cur][front + offset] = chars[left_char]
            canvas[row + cur][back + offset] = chars[right_char]
        front += directions[left_char]
        back += directions[right_char]
        cur += 1
    make_diamond(canvas, row + 2, col, size - 2)

def print_logo(size):
    height = 2 * size
    width = 2 * size + 2
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    make_diamond(canvas, 0, size - 1, size)
    for row in canvas:
        print(''.join(row).rstrip())
print_logo(n)
print_logo(n + 1)
