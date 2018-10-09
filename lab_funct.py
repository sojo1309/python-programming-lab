def armn(x):						#Defines the function
	sum1=0						#assings sum1 the value 0
	a=x
	while (a>0):					#starts while loop
		l=a%10					#extracts last digit
		sum1 += l**3				#cube of extracted digit
		a=a//10					#gives quotient of input
	if sum1==x:					#checks if sum equals the input 
		return "armstrong no"			#if sum1 equals input exiots the func and prints output
	else:
		return 'NOT armstrong no'
x=int(input())
print(armn(x))
