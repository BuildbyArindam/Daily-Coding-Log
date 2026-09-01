"""
Problem   : (Not Used) - Word Ladder
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/not-used-word-ladder_1062706?kunjiRedirection=true
Difficulty: Hard
Topics    : Graph, BFS, Hashing (Set), String Manipulation
Date      : 2026-09-01

Approach:
    Treat each word as a node; an edge exists between two words that differ
    by exactly one character. Run BFS from beginWord, generating all
    possible one-letter transformations at each step and checking them
    against the dictionary (hash set) for O(1) lookup. The first time
    endWord is reached, the current BFS depth + 1 is the answer (shortest
    transformation sequence length). Standard shortest-path-in-unweighted-
    graph pattern via BFS.

Complexity:
    Let L = word length, N = number of words in dictionary.
    Time  : O(N * L^2)  -> for each word popped, we try L positions * 26
             letters, and slicing/building each candidate word costs O(L).
    Space : O(N * L)    -> wordSet + visited set + queue, each holding up
             to N words of length L.
"""


# --------------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *

def minTransformSequence(beginWord, endWord, dictionary):
    if beginWord == endWord:
        return 1
    wordSet = set(dictionary)
    if endWord not in wordSet:
        return 0
    queue = deque()
    queue.append((beginWord, 1))
    visited = set()
    visited.add(beginWord)
    while queue:
        currentWord, steps = queue.popleft()
        for i in range(len(currentWord)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == currentWord[i]:
                    continue
                newWord = (
                    currentWord[:i] +
                    ch +
                    currentWord[i + 1:]
                )
                if newWord == endWord:
                    return steps + 1
                if newWord in wordSet and newWord not in visited:
                    visited.add(newWord)
                    queue.append((newWord, steps + 1))
    return 0
