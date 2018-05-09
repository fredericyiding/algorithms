class LSD:
	def __init__(self, filename):
		# a is list of strings with fixed length W
		self.a = []
		with open(filename) as f:
			for line in f:
				for string in line.split():
					self.a.append(string)
		self.W = len(self.a[0])
		self.R = 256  # can also be global variable
		self.N = len(self.a)
		self.aux = [None] * self.N


	def sort(self):

		for d in reversed(range(self.W)):
			count = [0] * (self.R + 1)  
			# Very important: tne count has to be initiated inside the for loop
			for i in range(self.N):
				count[ord(self.a[i][d]) + 1] += 1

			for r in range(self.R):
				count[r + 1] += count[r]
			print count

			for i in range(self.N):
				print 'a[i][d]: ' + str(self.a[i][d])
				print 'ord:' + str(ord(self.a[i][d]))  
				print 'count: ' + str(count[ord(self.a[i][d])])
				print 'aux: ' + str(self.aux[count[ord(self.a[i][d])]])
				self.aux[count[ord(self.a[i][d])]] = self.a[i]
				count[ord(self.a[i][d])] += 1

		self.a = self.aux
		
		return self.a