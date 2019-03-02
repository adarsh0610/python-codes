for i in range(1,8):
	r = input("press r to roll, q to quit")

	if r == "r":
		if i == 1 or i == 2 or i == 5:
			print("you got ",6)

		elif i == 3 or i == 6:
			print("you got ",2)
		elif i == 4 or i == 7:
			print("you got ",3)
	elif r == "q":
		print("Bye!")
		exit()
print("Hurray, you won!")			