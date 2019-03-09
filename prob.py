s=[2,5,5]
def func(s):
	d=1
	for i in s:
		d=i*d
	return d
d=func(s)
print("the multiplication of elements in list is",d)