"""
Problem: Array Chunks
Platform: FreeCodeCamp — Daily Coding Challenge (07-15)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-15
Date: 2026-09-02
Difficulty: Easy
Topics: Arrays, Slicing, Iteration

Approach:
Iterate over the array in steps of `size`, using Python slicing (arr[i:i+size])
to carve out each chunk and append it to the result list. Slicing naturally
handles the trailing partial chunk when len(arr) isn't a multiple of size.

Time Complexity: O(n) — each element is visited/copied exactly once across all slices
Space Complexity: O(n) — output list holds all n elements, just regrouped into chunks
"""


# ---------------------- Solution ------------------------------


def chunk_array(arr, size):
    chunks = []
    for i in range(0, len(arr), size):
        chunks.append(arr[i:i + size])
    return chunks
