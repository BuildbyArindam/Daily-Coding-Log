"""
Problem: Minimum Cost Path via an Intermediate Node
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/minimum-cost-path-via-an-intermediate-node_873190
Date Solved: 2026-09-11
Difficulty: Easy
Topic: Graphs — Multi-source Dijkstra / Shortest Path

Approach:
Run Dijkstra's algorithm three times, once each from source, destination,
and intermediate as the starting node, to get single-source shortest
distances to every other vertex. Since the path must pass through the
intermediate node, the optimal route decomposes into two shortest-path
segments joined at some pivot vertex v: source -> v -> intermediate -> v
is not needed explicitly; instead, for every vertex v, the cheapest way
to satisfy "visit source, destination, and intermediate" is
dist_source[v] + dist_destination[v] + dist_intermediate[v], minimized
over all v. This works because the three shortest-path trees meeting at
v is equivalent to finding the best "junction point" that connects all
three required nodes.

Time Complexity: O(3 * (M log N)) ~ O(M log N), for 3 Dijkstra runs on
a graph with N nodes and M edges (using a binary heap).
Space Complexity: O(N + M), for the adjacency list, distance arrays,
and heap.
"""


# ------------------------ Solution -----------------------------------


from os import *
from sys import *
from collections import *
from math import *
from heapq import heappush, heappop

import sys 
sys.setrecursionlimit(10**7)
def minimumCostPath(N, M, source, destination, intermediate, edges):
	graph = [[] for _ in range(N + 1)]
	for u, v, w in edges:
		graph[u].append((v, w))
		graph[v].append((u, w))
	INF = 10**30
	def dijkstra(start):
		dist = [INF] * (N + 1)
		dist[start] = 0
		pq = [(0, start)]
		while pq:
			d, u = heappop(pq)
			if d != dist[u]:
				continue
			for v, w in graph[u]:
				new_dist = d + w
				if new_dist < dist[v]:
					dist[v] = new_dist
					heappush(pq, (new_dist, v))
		return dist
	dist_source = dijkstra(source)
	dist_destination = dijkstra(destination)
	dist_intermediate = dijkstra(intermediate)
	answer = INF
	for v in range(1, N + 1):
		cost = (
			dist_source[v]
			+ dist_destination[v]
			+ dist_intermediate[v]
		)
		answer = min(answer, cost)
	return answer
def takeInput():
	data = list(map(int, sys.stdin.buffer.read().split()))
	idx = 0
	t = data[idx]
	idx += 1
	result = []
	for _ in range(t):
		n = data[idx]
		m = data[idx + 1]
		src = data[idx + 2]
		dest = data[idx + 3]
		inter = data[idx + 4]
		idx += 5
		edges = []
		for _ in range(m):
			u = data[idx]
			v = data[idx + 1]
			w = data[idx + 2]
			idx += 3
			edges.append([u, v, w])
		result.append((n, m, src, dest, inter, edges))
	return result

tests = takeInput()
for n, m, src, dest, inter, edges in tests:
	ans = minimumCostPath(n, m, src, dest, inter, edges)
	print(ans)
