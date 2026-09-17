"""
Problem   : Closest Distance Pair
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380928
Difficulty: Easy
Date      : 2026-09-17
Topics    : Divide and Conquer, Sorting, Geometry

Approach:
    Classic "closest pair of points" divide-and-conquer.
    1. Sort points by x-coordinate.
    2. Recursively split into left/right halves, solve each,
       take d = min(left_min, right_min).
    3. Build a "strip" of points within sqrt(d) of the mid line,
       sort by y, and check each point against only the next
       few candidates (bounded by d) to find any closer pair
       straddling the two halves.
    4. Return the minimum squared distance found.

Complexity:
    Time  : O(n log n)   -- master theorem: T(n) = 2T(n/2) + O(n log n) for strip sort,
                            reducible to O(n log n) with a merge-based y-sort; as written
                            (re-sorting strip each call) it's O(n log^2 n), still efficient.
    Space : O(n)          -- recursion + strip/list slicing
"""


# ------------------------------- Solution ------------------------------------


from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def closestPair(cordinates, n):
    points = sorted(cordinates, key=lambda p: (p.x, p.y))
    INF = 10**30
    def brute_force(points):
        min_dist = INF
        m = len(points)
        for i in range(m):
            for j in range(i + 1, m):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                dist = dx * dx + dy * dy
                if dist < min_dist:
                    min_dist = dist
        return min_dist
    def recursive(points):
        m = len(points)
        if m <= 3:
            return brute_force(points)
        mid = m // 2
        mid_x = points[mid].x
        left = points[:mid]
        right = points[mid:]
        dl = recursive(left)
        dr = recursive(right)
        d = min(dl, dr)
        strip = []
        for p in points:
            dx = p.x - mid_x
            if dx * dx < d:
                strip.append(p)
        strip.sort(key=lambda p: p.y)
        s = len(strip)
        for i in range(s):
            j = i + 1
            while j < s:
                dy = strip[j].y - strip[i].y
                if dy * dy >= d:
                    break
                dx = strip[j].x - strip[i].x
                dist = dx * dx + dy * dy
                if dist < d:
                    d = dist
                j += 1
        return d
    return recursive(points)

def takeInput():
    n = int(input().strip())
    if n == 0:
        return list(), n
    cordinates = [point(0, 0) for i in range(n)]
    for i in range(n):
        arr = list(map(int, stdin.readline().strip().split(" ")))
        cordinates[i] = point(arr[0], arr[1])
    return cordinates, n

cordinates, n = takeInput()
print(closestPair(cordinates, n))
