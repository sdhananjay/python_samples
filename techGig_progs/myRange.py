class MyRange(object):
	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value
		self.value += 1
		return current

num = MyRange(1,4)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
