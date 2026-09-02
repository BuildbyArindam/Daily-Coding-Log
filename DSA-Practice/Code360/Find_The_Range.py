"""
Problem   : Find The Range
Platform  : Code360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/find-the-range_1081477?kunjiRedirection=true
Difficulty: Easy
Date      : 2026-09-02
Topic     : Binary Search, Arrays

Approach:
    Two independent binary searches on the sorted array to locate the
    first and last occurrence of `key`.
    - find_start: on finding key, record index and search left half (high = mid - 1)
    - find_end:   on finding key, record index and search right half (low = mid + 1)
    If key is absent, find_start returns -1 and we short-circuit to [-1, -1].

Time Complexity : O(log n) per query — two binary searches, no recursion overhead
Space Complexity: O(1) auxiliary (excluding input array)
"""


# ----------------------  Solution -----------------------------


def find_start(arr, key):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            ans = mid
            high = mid - 1   
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return ans

def find_end(arr, key):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            ans = mid
            low = mid + 1  
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return ans

def firstAndLastPosition(arr, n, key):
    start = find_start(arr, key)
    if start == -1:
        return [-1, -1]
    end = find_end(arr, key)
    return [start, end]

T = int(input())
for _ in range(T):
    n, key = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = firstAndLastPosition(arr, n, key)
    print(ans[0], ans[1])
