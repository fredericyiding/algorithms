class LSD:
	def __init__(self, filename):
		# a is list of strings with fixed length W
		self._a = []
		with open(filename) as f:
			for line in f:
				for string in line.split():
					self._a.append(string)
		self.W = len(self._a[0])
		self.R = 256  # can also be global variable
		self.N = len(self._a)
		self._aux = [None] * self.N


	def sort(self):

		for d in reversed(range(self.W)):
			count = [0] * (self.R + 1)  
			# Very important: tne count has to be initiated inside the for loop
			for i in range(self.N):
				count[ord(self._a[i][d]) + 1] += 1

			for r in range(self.R):
				count[r + 1] += count[r]

			for i in range(self.N):
				self._aux[count[ord(self._a[i][d])]] = self._a[i]
				count[ord(self._a[i][d])] += 1

		self._a = self._aux
		
		return self._a