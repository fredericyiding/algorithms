class MSD:
	def __init__(self, filename):
		# a is list of strings with fixed length W
		self._a = []
		with open(filename) as f:
			for line in f:
				for string in line.split():
					self._a.append(string)
		self.R = 256  # can also be global variable
		self._aux = [None] * len(self._a)


	def sort(self, a, aux, lo, hi, d):
		if hi <= lo:
			return
		count = [0] * (self.R + 2)  		

		for i in range(lo, hi + 1):
			if d > len(a):
				count[1] += 1
			print len(a), d
			count[ord(a[i][d]) + 2] += 1

		for r in range(self.R + 1):
			count[r + 1] += count[r]

		for i in range(lo, hi + 1):
			if d > len(a):
				aux[count[0]] = a[i]
			aux[count[ord(a[i][d]) + 1]] = a[i]
			count[ord(a[i][d]) + 1] += 1
		for i in range(lo, hi + 1):
			a[i] = aux[i - lo]
		
		for r in range(R):
			self.sort(a, aux, lo + count[r], lo + count[r + 1] - 1, d + 1)
	
	def main(self):
		self.sort(self._a, self._aux, 0, len(self._a), 0)
		return self._a