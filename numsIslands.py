from Queue import Queue

class Solution:
	"""This is to calculate the number of Islands based on 
	binary list of lists.

	Attributes:
	"""

	def numsIslands(self, grid):
		"""This function calculates the number of Islands.
		Both BFS and DFS implementations were presented.

		BFS can be implemented by both Queue.Queue or collections.deque

		Args:
			grid: a list of lists with boolean input.

			example to generate a m x n grid:
			>>> from random import randint
			>>> m, n = 8, 7
			>>> grid = [[randint(0, 2) for y in range(n)] for x in range(m)]

		Returns:
			An integer that is the number of islands, defined as segregated 1's.
		"""

		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])

		visited = [[False for y in range(n)] for x in range(m)]

		def check(x, y):
			return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] and not visited[x][y]

		def bfs(x, y):
			q = Queue(maxsize = m * n)
			q.put((x, y))
			visited[x][y] = True
			nbrow = [0, 1, 0, -1]
			nbcol = [1, 0, -1, 0]

			while not q.empty():
				x_q, y_q = q.get()
				for i in range(4):
					newx, newy = x_q + nbrow[i], y_q + nbcol[i]
					if check(newx, newy):
						q.put((newx, newy))
						visited[newx][newy] = True

		def dfs(x, y):
			visited[x][y] = True
			nbrow = [0, 1, 0, -1]
			nbcol = [1, 0, -1, 0]

			for i in range(4):
				newx, newy = x + nbrow[i], y + nbcol[i]
				if check(newx, newy):
					visited[newx][newy] = True
					dfs(newx, newy)

		count = 0
		for row in range(m):
			for col in range(n):
				if check(row, col):
					dfs(row, col) # or dfs(row, col)
					count += 1

		return count

