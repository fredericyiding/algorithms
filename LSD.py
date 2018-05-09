class LSD:
	def __init__(self, filename):
		# a is list of strings with fixed length W
		self.a = []
		with open(filename) as f:
			for line in f:
				for string in line.split():
					self.a.append(string)
		self.W = len(self.a[0])
		self.R = 256
		self.N = len(self.a)
		self.aux = [0] * self.N


	def sort(self):
		count = [0] * (self.R + 1)
		for d in reversed(range(self.W - 1)):

			for i in range(self.N):
				count[ord(self.a[i][d]) - ord('a') + 1] += 1

			for r in range(self.R):
				count[r + 1] += count[r]

			for i in range(self.N):
				self.aux[count[ord(self.a[i][d]) - ord('a')]] = self.a[i]
				count[ord(self.a[i][d]) - ord('a')] += 1

			self.a = self.aux
		
		return self.a