p=int(input("enter any number"))
if p>1:		#prime numbers are always greater than 1 
	for i in range(2,p):
		if p%i==0:
			print(p,"is not a prime number")
			break
	else:
			print(p,"is a prime number")
else:
	print(p,"is not a prime number") # if p<=1 it is not prime number
