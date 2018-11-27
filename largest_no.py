def max(a,b,c):
 if(a>b) and (a>c):
	largest=a
 elif(b>a) and (b>c):
	largest=b
 else:
	largest=c
 return largest
a=12
b=45
c=23
print(max(a,b,c))

