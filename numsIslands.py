from Queue import Queue

class Solution:
	"""This is to calculate the number of Islands based on 
	binary list of lists.

	Attributes:
	"""

	def numsIslands(self, grid, method = 'bfs'):
		"""This function calculates the number of Islands.
		Both BFS and DFS implementations were presented.
		Note that BFS can be implemented by both Queue.Queue or collections.deque

		Args:
			grid (list of lists): boolean input, 1 as island and 0 as sea.
			method (string): bfs or dfs

			example for generating a m x n grid:
			>>> from random import randint
			>>> m, n = 8, 7
			>>> grid = [[randint(0, 2) for y in range(n)] for x in range(m)]

		Returns:
			An integer that is the number of islands, defined as segregated 1's.
		

		"""
		if method != 'bfs' or 'dfs':
			raise ValueError("Please enter 'bfs' or 'dfs'")
		self.grid = grid
		self.m = len(grid)
		if self.m == 0:
			return 0
		self.n = len(grid[0])
		self.visited = [[False for y in range(self.n)] for x in range(self.m)]

		count = 0
		for row in range(self.m):
			for col in range(self.n):
				if self.check(row, col):
					if method.lower() == 'bfs':
						self.bfs(row, col)
					elif method.lower() == 'dfs':
						self.dfs(row, col)
					count += 1

		return count

	def check(self, x, y):

			return x >= 0 and x < self.m and y >= 0 and y < self.n and self.grid[x][y] and not self.visited[x][y]

	def bfs(self, x, y):
			q = Queue(maxsize = self.m * self.n)
			q.put((x, y))
			self.visited[x][y] = True
			nbrow = [0, 1, 0, -1]
			nbcol = [1, 0, -1, 0]

			while not q.empty():
				x_q, y_q = q.get()
				for i in range(4):
					newx, newy = x_q + nbrow[i], y_q + nbcol[i]
					if self.check(newx, newy):
						q.put((newx, newy))
						self.visited[newx][newy] = True

	def dfs(self, x, y):
			self.visited[x][y] = True
			nbrow = [0, 1, 0, -1]
			nbcol = [1, 0, -1, 0]

			for i in range(4):
				newx, newy = x + nbrow[i], y + nbcol[i]
				if self.check(newx, newy):
					self.visited[newx][newy] = True
					self.dfs(newx, newy)



