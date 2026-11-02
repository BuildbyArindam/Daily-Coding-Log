"""
Problem   : Chandu and his Girlfriend Returns
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/chandu-and-his-girlfriend-returns/
Difficulty: Easy
Topics    : Sorting, Merge Sort, Two Pointers, Arrays
Date      : 2026-11-02

Approach:
    Both input arrays are already sorted in non-increasing order, so the
    answer is the merge step of merge sort. Keep one pointer per array,
    repeatedly append the larger of the two current elements, then append
    whatever remains of the array that was not exhausted. There is no need
    to re-sort the combined list.

Complexity:
    Time  : O(N + M) per test case
    Space : O(N + M) for the merged output
"""


# -------------------------------------------------- Solution ---------------------------------------------------------------


import sys

def combine(first, second):
    p = q = 0
    size_a, size_b = len(first), len(second)
    result = []
    put = result.append
    while p < size_a and q < size_b:
        if second[q] > first[p]:
            put(second[q])
            q += 1
        else:
            put(first[p])
            p += 1
    if p < size_a:
        result.extend(first[p:])
    if q < size_b:
        result.extend(second[q:])
    return result

def read_case(data, pos):
    n = int(data[pos])
    m = int(data[pos + 1])
    pos += 2
    arr1 = list(map(int, data[pos:pos + n]))
    pos += n
    arr2 = list(map(int, data[pos:pos + m]))
    pos += m
    return arr1, arr2, pos

def main():
    data = sys.stdin.read().split()
    cases = int(data[0])
    cursor = 1
    answers = []
    for _ in range(cases):
        arr1, arr2, cursor = read_case(data, cursor)
        merged = combine(arr1, arr2)
        answers.append(" ".join(map(str, merged)))
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
