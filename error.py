try:
	a=int(input("enter the number:"))
	if a<4:
		raise NameError
	elif a==4:
		raise TypeError
	else:
		raise ValueError
except 	NameError:
	print("ooooooooppppppsssss... name error occured")
except TypeError:
	print("type error occured")
except ValueError:
	print("value error occured")
else:
	print("no error")
finally:
		print("Execution finished......")				
