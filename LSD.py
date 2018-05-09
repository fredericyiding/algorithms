class LSD:
	def __init__(self, a, W):
		# a is list of strings with fixed length W
		self.a = []
		self.W = W
		self.R = 256
		self.N = len(a)
		self.aux = [0] * self.N
		self.count = [0] * (R + 1)

	def sort(self):
		for d in reversed(range(self.W - 1)):

			for i in range(self.N):
				self.count[self.a[i] + 1] += 1

			for r in range(self.R):
				self.count[r + 1] += self.count[r]

			for i in range(self.N):
				self.aux[self.count[self.a[i]]] = self.a[i]
				self.count[self.a[i]] += 1

			self.a = self.aux
		
		return self.a