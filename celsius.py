j=int(input("enter temp"))                                              #Takes the user input for temp
k=int(input("if temp enteted is in celcius enter 1 or else press 2"))   #Takes the user input of whether the temp is in C or F       
if k==1:
 a=(9*j +160)/5
 print("temp in farenheit is",a)
else:
 a=(5*j -160)/9
 print("temp in celcius is:",a)
