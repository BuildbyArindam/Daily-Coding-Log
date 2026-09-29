"""
Problem   : Min Steps by Knight
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/steps-by-knight5927/1
Difficulty: Medium
Topics    : Graph, BFS, Queue
Date      : 2026-09-29

Approach:
    Treat each board cell as a graph node and each of the 8 knight moves as an
    edge. Since every move costs 1, BFS from the start gives the shortest path.
    Positions are converted to 0-indexed, a visited grid prevents revisits, and
    the queue is a list with a front pointer (avoids O(n) pop(0)). Returns as
    soon as the target is discovered; -1 if unreachable.

Complexity:
    Time : O(n^2)  - each cell is enqueued at most once, with 8 moves checked per cell
    Space: O(n^2)  - visited grid + queue
"""


# ------------------------------------- Solution --------------------------------------------


class Solution:
	def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
		#Code here
		start_x = knightPos[0] - 1
		start_y = knightPos[1] - 1
		target_x = targetPos[0] - 1
		target_y = targetPos[1] - 1
		if (start_x, start_y) == (target_x, target_y):
			return 0
		moves = [
			(2, 1), (2, -1),
			(-2, 1), (-2, -1),
			(1, 2), (1, -2),
			(-1, 2), (-1, -2)
		]
		visited = [[False] * n for _ in range(n)]
		queue = [(start_x, start_y, 0)]
		visited[start_x][start_y] = True
		front = 0
		while front < len(queue):
			x, y, steps = queue[front]
			front += 1
			for dx, dy in moves:
				nx = x + dx
				ny = y + dy
				if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
					if nx == target_x and ny == target_y:
						return steps + 1
					visited[nx][ny] = True
					queue.append((nx, ny, steps + 1))
		return -1
