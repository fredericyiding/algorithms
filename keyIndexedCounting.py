import random

class keyIndexedCounting:
	"""
	Sort an array a[] of N integers between 0 and R - 1
	1. Count frequencies of each letter using key as index 
	2. Compute frequency cumulates which specify destinations
	3. Access cumulates using key as index to move items
	4. Copy back into original array
	"""
	def __init__(self, N, R):
		self.a = []
		for i in range(N):
			self.a.append(random.randint(0, R - 1)) 

		self.count = [0] * (R + 1)
		self.aux = [0] * N
		self.N = N
		self.R = R

	def __repr__(self):
		return "Key-indexed counting instance: " + str(self.a)

	def getArray(self):
		return self.a
	
	def main(self):
		for i in range(self.N):
			self.count[self.a[i] + 1] += 1

		for r in range(self.R):
			self.count[r + 1] += self.count[r]

		for i in range(self.N):
			self.aux[self.count[self.a[i]]] = self.a[i]
			self.count[self.a[i]] += 1

		self.a = self.aux
		# or we can use:
		#	for i in range(N):
		#  		a[i] = aux[i]

		return self.a
