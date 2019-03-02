import random

d=0
p=0
snl = {8:37,13:34,40:68,52:81,76:97,38:9,11:2,25:4,65:46,89:70,93:64}
def rolldice():
	return random.randint(1,6)
while True:
	r = input ("Press r to roll, q to quit : ")
	elif r == 'q':
		exit()	
	if r == 'r':
		d = random.randint(1,6)
		print("you got :",d)
		if d == 6:
			print("Congratulations, you can play now.")
			break
		else:
			print("Roll again, till you get 6.")

while True:
	r = input("Press r to roll, q to quit : ")

	if r == 'r':
		d = rolldice()
		print("you got :",d)
		p = p+d
		print("your new position is :",p)

		if p > 100:
			p = p-d
			print("wait till you get", 100-p,"or less.")
		if p == 100:
			print("you won!")
			exit()
		if p in snl:
			if p < snl[p]:
				print("wow, you go a ladder.")
			else:
				print("oooooopppppssss, you got bitten by a snake.")

			p = snl[p]
			print("move to ",p)
	elif r == 'q':
		exit()	