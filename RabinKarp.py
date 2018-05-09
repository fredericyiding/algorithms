import random

class RabinKarp:

	def strStr2(self, source, target):
		if source is None or target is None:
			return -1

		m = len(target)
		if m == 0:
			return 0

		n = len(source)
		if n == 0:
			return -1


		RM = 1
		h = 0
		R = 256
		Q = random.randint(1000000, 2000000) # LEGB rule

		for i in range(m - 1):
			RM = (R * RM) % Q

		def Horner(str, m):
			# Horner's method to compute hash for string with m char's
			for i in range(m):
				h = (R * h + ord(str[i])) % Q
			return h

		patHash = Horner(target, m)

		txtHash = Horner(source, m) # start with first m char's
		if patHash == txtHash:
			return 0
		for i in range(m, n):
			txtHash = (txtHash + Q - RM * ord(source[i - m]) % Q) % Q
			txtHash = (txtHash * R + ord(source[i])) % Q
			if patHash == txtHash:
				return i - m + 1

		return -1