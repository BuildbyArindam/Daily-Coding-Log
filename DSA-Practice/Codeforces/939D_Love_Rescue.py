"""
Problem   : Love Rescue
Platform  : Codeforces
Link      : https://codeforces.com/contest/939/problem/D
Date      : 2026-08-15
Difficulty: CF *1600
Topics    : DSU, Graphs, DFS and Similar, Greedy, Strings

Approach:
  Treat the 26 lowercase letters as nodes in a graph. For each position i,
  we need s1[i] and s2[i] to be interchangeable (directly or transitively)
  for the two strings to become equal via swaps. Union the two characters
  at each position using DSU. Whenever a union actually merges two
  different components (i.e. this pair isn't already connected), record
  it as a required "spell" (swap rule) — this greedily builds a spanning
  forest over the 26-letter alphabet using the minimum number of edges
  needed to connect all required character pairs.

Complexity:
  Time  : O(n * alpha(26)) ~ O(n)   -- n DSU union/find ops, alpha ~ constant
  Space : O(26) for the DSU parent array, O(n) worst case for spells list
"""


# ---------------------------- Solution ------------------------------


import sys

class DisjointSetUnion:
  def __init__(self, size=26):
    self.parent = list(range(size))

  def find(self, i):
    if self.parent[i] == i:
      return i
    self.parent[i] = self.find(self.parent[i])  
    return self.parent[i]

  def union(self, i, j):
    root_i = self.find(i)
    root_j = self.find(j)
    if root_i != root_j:
      self.parent[root_i] = root_j
      return True
    return False

def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  s1 = input_data[1]
  s2 = input_data[2]
  dsu = DisjointSetUnion(26)
  spells = []
  for i in range(n):
    c1 = ord(s1[i]) - ord("a")
    c2 = ord(s2[i]) - ord("a")
    if dsu.union(c1, c2):
      spells.append((s1[i], s2[i]))
  print(len(spells))
  for u, v in spells:
    print(f"{u} {v}")

if __name__ == "__main__":
  solve()
  
