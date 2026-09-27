"""
Problem: Rich Rhyme
Platform: CodeChef
Link: https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13C
Date Solved: 2026-09-27
Difficulty: Hard
Topics: KMP, Strings, Prefix Function 

Approach:
    For each input string, compute the KMP "failure function" (prefix
    function), where result[i] = length of the longest proper prefix
    of word[0..i] that is also a suffix of word[0..i]. Built using the
    standard KMP preprocessing technique with a running pointer `k`
    that reuses previously computed border lengths, avoiding recomputation.

Time Complexity:  O(n) per string (amortized, standard KMP prefix-function bound)
Space Complexity: O(n) per string, for the `result` array
"""


# ----------------------------------------- Solution ------------------------------------------


import sys

def compute_prefix_border(word):
    n = len(word)
    result = [0] * n
    k = 0
    for i in range(1, n):
        ch = word[i]
        while k > 0 and word[k] != ch:
            k = result[k - 1]
        if word[k] == ch:
            k += 1
        result[i] = k
    return result
    
def solve():
    data = sys.stdin.buffer.read().decode()
    lines = data.splitlines()
    answers = []
    for entry in lines:
        token = entry.strip() 
        if token == "End":
            break
        if token == "":
            continue
        borders = compute_prefix_border(token)
        answers.append(' '.join(map(str, borders)))
    sys.stdout.write('\n'.join(answers))
    if answers:
        sys.stdout.write('\n')

if __name__ == "__main__":
    solve()
