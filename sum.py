s=[2,5,6,4]
def func(s):
	d=0
	for i in s:
		d=i+d
	return d
d=func(s)
print("the sum of elements in list is",d)