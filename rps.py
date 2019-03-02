import random
r=["r","p","s"]
d={'r':"rock",'p':"paper",'s':"scissor",'q':"quit"}
i=0
a=0
while True:
	l=input("enter your choice:")
	if l=='q':
		print("user score",a)
		print("computer score",i)
		if i>a:
			print("computer won with",i,"points")
		elif i==a:
			print("match draw")
		else:
			print("user won with",a,"points")	
		exit()
	print("user has choosen",d[l])
	x=random.choice(r)
	print("computer has choosen",d[x])
	if l==x:
		print("match draw")

	elif l=="r" and x=="p" or l=="s" and x=="p" or l=="s" and x=="r":
		print("computer wins")
		i=i+1

	else:
		print("you winsss")
		a=a+1