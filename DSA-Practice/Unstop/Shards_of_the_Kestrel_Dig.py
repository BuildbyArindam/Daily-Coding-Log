"""
Problem   : Shards of the Kestrel Dig
Platform  : Unstop
Link      : https://unstop.com/code/practice/661018
Difficulty: Medium
Topics    : String, Trie, Hashing, Prefix Queries, Frequency Counting
Date      : 2026-09-24

Approach:
    Build a Trie over all inserted strings. Each node stores a hash map
    (`eras`) counting how many inserted strings passing through that node
    belong to each era. An ADD walks/creates the path and increments
    eras[era] at every node along it. A query walks the prefix and reads
    eras[era] at the final node, or returns 0 if the path breaks.

Complexity (L = total characters across all operations):
    Time  : O(L). Each ADD or query costs O(len(text)) with O(1) average
            dict operations.
    Space : O(A), where A is the total characters across ADD operations.
            Each character adds at most one node and one era entry.
"""


# --------------------------------------------- Solution -------------------------------------------------------


import sys

class TrieNode:
    __slots__ = ("children", "eras")
    def __init__(self):
        self.children = {}
        self.eras = {}

def solve():
    input = sys.stdin.readline
    Q = int(input())
    root = TrieNode()
    output = []
    for _ in range(Q):
        parts = input().split()
        operation = parts[0]
        text = parts[1]
        era = int(parts[2])
        node = root
        if operation == "ADD":
            for ch in text:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.eras[era] = node.eras.get(era, 0) + 1
        else:  
            found = True
            for ch in text:
                if ch not in node.children:
                    found = False
                    break
                node = node.children[ch]
            if found:
                output.append(str(node.eras.get(era, 0)))
            else:
                output.append("0")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
