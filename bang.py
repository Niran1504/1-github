def a(b):
	for c in b:
		yield (c * c)
d = a([1, 2, 3])
# print(d)
for e in d:
	print(e)