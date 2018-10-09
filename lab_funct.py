def armn(x):
	sum1=0
	a=x
	while (a>0):
		l=a%10
		sum1 += l**3
		a=a//10
	if sum1==x:
		return "armstrong no"
	else:
		return 'NOT armstrong no'
x=int(input())
print(armn(x))
