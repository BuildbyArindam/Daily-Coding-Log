"""
Problem: Tara's Call Sign Archive
Platform: Unstop
Link: https://unstop.com/code/practice/659451
Date: 2026-09-12
Difficulty: Medium
Topic: String, Trie, Prefix Matching

Approach:
Insert each call sign into a trie one at a time. Before inserting a new
string, walk down the trie along its characters to find the length of
the longest prefix of the string that already terminates at a complete
word ("$" marker) — this gives the "reusable" prefix length. The score
for the string is (len(s) - longest_prefix), i.e. the number of new
characters that had to be added. If the string is an exact duplicate
of a previously inserted string, mark it as -1 instead of scoring it.
After scoring, insert the string into the trie.

Time Complexity:  O(total length of all strings)   -> O(sum(len(s_i)))
                  each string does 3 trie walks (prefix scan, duplicate
                  check, insert), all linear in len(s_i).
Space Complexity: O(total length of all strings) for the trie nodes.
"""


# --------------------------------- Solution ----------------------------------------


N = int(input())
root = {}
total = 0
answers = []
for _ in range(N):
    s = input().strip()
    node = root
    longest_prefix = 0
    for i, ch in enumerate(s):
        if ch not in node:
            break
        node = node[ch]
        if "$" in node:
            longest_prefix = i + 1
    node = root
    duplicate = True
    for ch in s:
        if ch not in node:
            duplicate = False
            break
        node = node[ch]
    if duplicate and "$" in node:
        answers.append("-1")
        continue
    score = len(s) - longest_prefix
    answers.append(str(score))
    total += score
    node = root
    for ch in s:
        if ch not in node:
            node[ch] = {}
        node = node[ch]
    node["$"] = True
print("\n".join(answers))
print("Total:", total)
